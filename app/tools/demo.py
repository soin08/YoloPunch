import os, sys
import pprint

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yolopunch.settings")

import django
django.setup()

"""
from api.urls import users_router

pprint.pprint(users_router.urls)
"""
from yolopunch.urls import urlpatterns

pprint.pprint(urlpatterns)
