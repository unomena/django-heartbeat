import os

from django.http import HttpResponse
from django.views.decorators.cache import never_cache
from django.conf import settings


@never_cache
def status(request, *args, **kwargs):
    # check the file flag
    if getattr(settings, 'HEARTBEAT_FILENAME', False) and \
        os.path.exists(settings.HEARTBEAT_FILENAME) and \
        '0' in open(settings.HEARTBEAT_FILENAME).read():
        return HttpResponse('Server maintenance under way', status=503)
    
    # add checks here
    
    # all good
    return HttpResponse('OK')