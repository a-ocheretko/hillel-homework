from django.urls import path
from apps.about.views import about, whoami

urlpatterns = [
    path('about/', about),
    path('about/whoami/', whoami)
]