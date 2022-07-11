from django.shortcuts import render, HttpResponse, Http404
from random import choice

# Create your views here.


def home(request):
    return render(request, 'home.html')


def random_string(request):
    strng = ''
    letters = [chr(i) for i in list(range(65, 91)) + list(range(97, 123))]
    digs = '1234567890'
    specs = '!"№;%:?*()_+'
    length = request.GET.get('length')
    digits = request.GET.get('digits')
    specials = request.GET.get('specials')
    try:
        if int(length) in range(1, 101) and int(digits) in (0, 1) and int(specials) in (0, 1):
            if int(digits) == 1:
                letters += digs
            if int(specials) == 1:
                letters += specs
            for i in range(int(length)):
                strng += choice(letters)
            return render(request, 'random_string.html', {'strng': strng})
    except ValueError:
        return render(request, 'random_string_error.html')
    return render(request, 'random_string_error.html')

