# Word Counter API

Counts all word occurence in a web page source. You can visit it [here](https://wordcounterapi.herokuapp.com).

## How to use

Just provide the API with the `url` and `word` parameter. The request should look like this:

https://wordcounterapi.herokuapp.com/wordcount?url=http://virtusize.jp&word=fit


### Note

Queries will be cached for an hour.
The database is broken as of right now in Heroku, but it works just fine if ran locally.
