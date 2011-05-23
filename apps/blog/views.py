import datetime
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.core.urlresolvers import reverse
from apps.blog.models import BlogPost, BlogCategory


class BlogPostListView(ListView):
    """
    Generic blog post list view.
    """
    paginate_by = 5
    model = BlogPost

    def get_queryset(self):
        """
        Only show BlogPost objects whose date_published is in the past.
        """
        now = datetime.datetime.now
        return BlogPost.objects.filter(date_published__lte=now)

    def get_context_data(self, **kwargs):
        context = super(BlogPostListView, self).get_context_data(**kwargs)
        context['rss_link'] = reverse('rss-latest-bpost')
        return context


class BlogPostSlugDetailView(DetailView):
    """
    Shows an individual blog post.
    """
    context_object_name = "bpost"
    model = BlogPost

    def get_object(self):
        now = datetime.datetime.now
        return get_object_or_404(BlogPost,
                                 date_published__year=self.kwargs.get('year'),
                                 date_published__month=self.kwargs.get('month'),
                                 date_published__day=self.kwargs.get('day'),
                                 slug=self.kwargs.get('slug'),
                                 date_published__lte=now)

    def get_context_data(self, **kwargs):
        context = super(BlogPostSlugDetailView, self).get_context_data(**kwargs)
        # Used for Intense Debate URLs.
        context['intense_debate_post_url'] = settings.URL_ROOT
        return context


class BlogPostIdDetailView(DetailView):
    """
    Maintain backwards compatibility with old URLs that referenced posts by
    ID instead of slug. Would love to get rid of this eventually.
    """
    context_object_name = "bpost"
    model = BlogPost

    def get_object(self):
        now = datetime.datetime.now
        return get_object_or_404(BlogPost,
                                 pk=self.kwargs.get('pk'),
                                 date_published__lte=now)

    def get_context_data(self, **kwargs):
        context = super(BlogPostIdDetailView, self).get_context_data(**kwargs)
        # Used for Intense Debate URLs.
        context['intense_debate_post_url'] = settings.URL_ROOT
        return context


class CategoryBlogPostListView(ListView):
    """
    Shows all blog posts within a given category. Based on slug.
    """
    paginate_by = 5
    model = BlogPost

    def get_queryset(self):
        now = datetime.datetime.now
        return BlogPost.objects.filter(category__slug=self.kwargs.get('slug'),
                                       date_published__lte=now)

    def get_context_data(self, **kwargs):
        context = super(CategoryBlogPostListView, self).get_context_data(**kwargs)
        context['rss_link'] = reverse('rss-bposts-category', args=[self.kwargs.get('slug')])
        return context
