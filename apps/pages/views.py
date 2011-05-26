from django.views.generic import TemplateView
from django.core.cache import cache
from utils import zpgapi

class HomeView(TemplateView):
    """
    Front page view.
    """
    template_name = "pages/index.html"

    def get_context_data(self, **kwargs):
        return {
            'connected_players': self._get_connected_player_list()
        }

    def _get_connected_player_list(self):
        """Returns a list of the currently connected playes (on the MC server).
        
        * First tries to hit the cache to see if this has been checked recently.
        * If there is no cache entry, queries the Minecraft server's 
          zombiepygman API to get the list of currently connected players.
        """
        if not zpgapi.is_zgp_api_enabled():
            # API is not configured, skip this.
            print "BOOP"
            return []

        cache_key = 'api_connected_players'
        cache_val = cache.get(cache_key)

        if cache_val:
            return cache_val

        cache_val = zpgapi.call_zpg_api('/cmd/listconnected')['player_list']
        cache.set(cache_key, cache_val, 60)
        return cache_val
