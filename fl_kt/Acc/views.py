from django.shortcuts import render

import logging
# Create your views here.


def index(request):
    return render(request, 'index.html', locals())
