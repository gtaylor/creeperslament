"""
URL direction module for the Blog module.
"""
from django.conf.urls.defaults import *
from apps.blog.views import BlogPostListView, BlogPostIdDetailView, BlogPostSlugDetailView, CategoryBlogPostListView

urlpatterns = patterns('apps.blog.views',
    (r'^$', BlogPostListView.as_view()),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>[-\w]+)/$',
        BlogPostSlugDetailView.as_view(),
        name='bpost-show-slug'),
    url(r'^post/(?P<pk>\d+)/$',
        BlogPostIdDetailView.as_view(),
        name='bpost-show-id'),
    url(r'^category/(?P<slug>[-\w]+)/$',
        CategoryBlogPostListView.as_view(),
        name='bpost-show_category'),
)
