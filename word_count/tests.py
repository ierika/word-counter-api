from django.test import TestCase
from django.test import Client

from . import utils


class ApiTest(TestCase):
    c = Client()

    def test_invalid_query_returns_http_bad_request(self):
        """Should return correct status code in case of invalid URL"""
        res = self.c.get('/wordcount/',
                         {'url': 'invalidurl', 'word': 'random'})
        self.assertEquals(res.status_code, 400)

    def test_invalid_query_returns_correct_message(self):
        """Should return correct error message in case of invalid URL"""
        res = self.c.get('/wordcount/',
                         {'url': 'invalidurl', 'word': 'random'})
        self.assertIn('Enter a valid URL', res.content.decode('utf-8'))

    def test_valid_query_returns_http_ok(self):
        """Should return HTTP ok if everything was entered correctly"""
        res = self.c.get('/wordcount/',
                         {'url': 'virtusize.jp', 'word': 'fit'})
        self.assertEquals(res.status_code, 200)

    def test_missing_query_returns_http_bad_request(self):
        """Should return HTTP Bad Request if no params were supplied"""
        res = self.c.get('/wordcount/')
        self.assertEquals(res.status_code, 400)


class UtilsCountWordFrequencyTest(TestCase):
    def test_should_only_match_the_word_itself(self):
        """Checks the word frequency counter accuracy"""
        example = 'fitting room fit fit-cross fitt ---fit--- fitter'
        expected = 3
        actual = utils.count_word_frequency('fit', example)
        self.assertEquals(expected, actual)

    def test_should_be_case_insensitive(self):
        """Should be case-insensitive"""
        example = 'Fit fit Fit fIT FIT'
        expected = 5
        actual = utils.count_word_frequency('fit', example)
        self.assertEquals(expected, actual)
