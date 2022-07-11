from django.shortcuts import render
from datetime import datetime


# Create your views here.
def about(request):
    return render(request, 'about.html')


def whoami(request):
    browser = request.META.get('HTTP_USER_AGENT')
    ip_address = request.META.get('REMOTE_ADDR')
    server_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render(request, 'whoami.html', {'browser': browser, 'ip_address': ip_address, 'server_time': server_time})
