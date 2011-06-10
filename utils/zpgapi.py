"""
zombiepygman API helper functions.
"""
from django.conf import settings
from zombiepygman.client import ZpmAPI

def is_zgp_api_enabled():
    """
    If the zombiepygman API is configured and enabled, returns ``True``.
    Otherwise, ``False``.

    :rtype: bool
    """
    return getattr(settings, 'ZPG_API', {}) != {}


def get_zpg_api_iface():
    """
    Returns a properly configured zombiepygman ZpmAPI instance.

    :rtype: zombiepygman.client.ZpmAPI
    """
    return ZpmAPI(api_host='http://smp.creeperslament.com:8001',
                  security_token=settings.ZPG_API['SECURITY_TOKEN'])

