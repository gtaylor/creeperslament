import datetime
from django.contrib.syndication.views import Feed, FeedDoesNotExist
from apps.blog.models import BlogPost, BlogCategory

AUTHOR_NAME = "Greg Taylor"
AUTHOR_EMAIL = "gtaylor@gc-taylor.com"
COPYRIGHT = "Copyright (c) 2011, Gregory Taylor"

class LatestBposts(Feed):
    """
    A feed of all of the latest published BlogPost objects.
    """
    title = "Greg Taylor's Blog"
    description = "The latest posts from the blog of Greg Taylor."
    copyright = COPYRIGHT
    author_name = AUTHOR_NAME
    author_email = AUTHOR_EMAIL
    link = 'http://gc-taylor.com'

    def items(self):
        now = datetime.datetime.now
        return BlogPost.objects.filter(date_published__lte=now)[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_guid(self, item):
        return '%s' % item.id

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.date_published

    def item_categories(self, item):
        return [cat.name for cat in item.category.all()]

class BpostCatPosts(Feed):
    """
    Latest blog posts for a certain category.
    """
    author_name = AUTHOR_NAME
    author_email = AUTHOR_EMAIL
    copyright = COPYRIGHT

    def title(self, obj):
        return "Greg Taylor's Latest: %s" % obj.name

    def description(self, obj):
        return "The latest posts from the %s category of Greg Taylor's blog." % obj.name

    def link(self, obj):
        if not obj:
            raise FeedDoesNotExist
        return obj.get_absolute_url()

    def get_object(self, request, bcat_id):
        return BlogCategory.objects.get(id=bcat_id)

    def items(self, obj):
        now = datetime.datetime.now
        return BlogPost.objects.filter(category__in=[obj.id],
                                       date_published__lte=now)[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.body

    def item_guid(self, item):
        return '%s' % item.id

    def item_link(self, item):
        return item.get_absolute_url()

    def item_pubdate(self, item):
        return item.date_published

    def item_categories(self, item):
        return [cat.name for cat in item.category.all()]

class BpostCatPostsBySlug(BpostCatPosts):
    """
    Latest bog posts for a certain category, looked up by slug instead of PK.
    """
    def get_object(self, request, bcat_slug):
        return BlogCategory.objects.get(slug=bcat_slug)
