from django.db import models
from django.core.urlresolvers import reverse
from tinymce import models as tinymce_models

class BlogCategory(models.Model):
    """
    A rough way to categorize blog posts. This is used in RSS feed generation,
    and a few other places.
    """
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255)

    def get_absolute_url(self):
        return reverse('bpost-show_category', args=[self.slug])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

class BlogPost(models.Model):
    """
    A blog post (surprise!).
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    body = tinymce_models.HTMLField()
    category = models.ManyToManyField(BlogCategory)
    date_added = models.DateTimeField(auto_now_add=True)
    date_last_modified = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('bpost-show-slug',
                       args=[self.date_published.year,
                             self.date_published.month,
                             self.date_published.day,
                             self.slug])

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_published']
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"
