import datetime
from django.contrib.sitemaps import Sitemap
from apps.blog.models import BlogPost

class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 1.0

    def items(self):
        now = datetime.datetime.now
        return BlogPost.objects.filter(date_published__lte=now)

    def lastmod(self, obj):
        return obj.date_last_modified
