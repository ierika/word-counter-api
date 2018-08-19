import dj_database_url

from .base import *


DEBUG = False

ALLOWED_HOSTS.append('wordcounterapi.herokuapp.com')
ALLOWED_HOSTS.append('0.0.0.0')

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
