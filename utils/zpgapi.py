"""
zombiepygman API helper functions.
"""
import socket
import logging
import urllib
import urllib2
from pprint import pformat
import simplejson

from django.conf import settings

logger = logging.getLogger('zpgapi')

def is_zgp_api_enabled():
    """
    If the zombiepygman API is configured and enabled, returns ``True``.
    Otherwise, ``False``.
    
    :rtype: bool
    """
    return getattr(settings, 'ZPG_API', {}) != {}

def call_zpg_api(method, **kwargs):
    """
    Make an API call to the zombiepygman instance configured in the site's
    settings. 
    
    Any keyword args provided become GET NVPs for the API request.
    
    :rtype: dict
    :returns: The un-serialized API results in dict form.
    """
    # Beware, this is a global setting.
    socket.setdefaulttimeout(5)
    zpgsettings = settings.ZPG_API

    logger.debug('ZPG API host: %s' % zpgsettings['HOST'])

    # This will store key/value pairs to be used as GET NVPs in the request.
    http_get_vals = {
        'security_token': zpgsettings['SECURITY_TOKEN']
    }
    # All values passed to PayPal API must be uppercase.
    for key, value in kwargs.iteritems():
        http_get_vals[key.upper()] = value

    # This shows all of the key/val pairs we're sending to PayPal.
    if logger.isEnabledFor(logging.DEBUG):
        logger.debug('ZPG API Query Key/Vals:\n%s' % pformat(http_get_vals))

    # Turn kwargs into GET NVPs.
    data = urllib.urlencode(http_get_vals)
    if data:
        data = '?%s' % data

    # Full Proto + Host + URL Path + GET NVPs for API Resource. 
    full_url = '%s%s%s' % (zpgsettings['HOST'], method, data)
    logging.debug('ZPG API Query URL: %s' % full_url)

    # Do work, son.
    req = urllib2.Request(full_url)
    response = urllib2.urlopen(req).read()
    response_dict = simplejson.loads(response)

    logging.debug('ZPG API Response:\n%s' % pformat(response_dict))
    return response_dict
