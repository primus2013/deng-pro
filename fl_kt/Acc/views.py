from django.shortcuts import render
from django.conf import settings
from models import *

import logging

# Create your views here.
logger=logging.getLogger('Acc.views')


def global_setting(request):
    return {'SITE_NAME': settings.SITE_NAME,
            'SITE_DESC': settings.SITE_DESC,}


def index(request):
    try:
        pass
    except Exception as e:
        logger.error(e)
    return render(request, 'index.html', locals())
