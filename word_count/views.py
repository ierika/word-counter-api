import http.client as http_client

import requests
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from django.views import generic

from . import forms
from . import utils


class IndexView(generic.FormView):
    """Index page

    Contains a form that can query the API
    """
    template_name = 'word_count/index.html'
    form_class = forms.WordCountForm


class WordCountView(APIView):
    """The word count API"""
    form_class = forms.WordCountForm
    renderer_classes = (JSONRenderer,)

    def get(self, request, *args, **kwargs):
        """Count the words in the given URL

        It should be case-insensitive. If the page and word has been -
        searched, save the information to the database so it can be -
        re-used if ever it gets queried again.
        """
        # Return cache if there is
        cache = self.request.session.get(request.get_full_path_info())
        if cache:
            return Response(cache)

        form = self.form_class(request.GET)
        if form.is_valid():
            url = form.cleaned_data.get('url')
            word = form.cleaned_data.get('word')

            json = self.parse_page(url, word)

            res = Response(json)
            res.status_code = 200
            return res
        else:
            res = Response(self.render_error_response(
                message=form.errors.get_json_data(),
            ))
            res.status_code = 400  # bad request
            return res

    def parse_page(self, url, word):
        """Gets the HTML source and find all the word occurrence in it."""
        # Find the word 'fit' in the given URL
        res = requests.get(url)
        if res.status_code == 200:
            source = res.content.decode()
            word_count = utils.count_word_frequency(word, source)

            # Get JSON and save to cache
            json = self.render_ok_response(word, url, word_count)
            self.request.session[self.request.get_full_path_info()] = json

            # Set the cache expiry for an hour
            self.request.session.set_expiry(60*60)

            return self.request.session.get(self.request.get_full_path_info())
        else:
            message = http_client.responses.get(res.status_code, 500)
            res = Response(self.render_error_response(
                message=message,
            ))
            res.status_code = res.status_code
            return res

    @staticmethod
    def render_ok_response(word, url, word_count):
        """Render a successful JSON response"""
        res = {
            'status': 'ok',
            'word': word,
            'url': url,
            'word_count': word_count,
        }
        return res

    @staticmethod
    def render_error_response(message=None):
        """Render an unsuccessful JSON response"""
        res = {
            'status': 'error',
            'message': message,
        }
        return res


class DocsView(generic.TemplateView):
    template_name = 'word_count/docs.html'
