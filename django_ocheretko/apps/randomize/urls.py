from django.urls import path, re_path
from apps.randomize.views import home, random_string

urlpatterns = [
    path('', home),
    re_path(r'^random/$', random_string),
]