import os, sys
import pprint

sys.path.append("..")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "yolopunch.settings")

import django
django.setup()

from yolo.urls import router

pprint.pprint(router.urls)
