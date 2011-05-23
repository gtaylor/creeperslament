"""
Blog-related tags.
"""
from django.template import Library

register = Library()

@register.inclusion_tag('blog/tags/blogpost_preview.html')
def blogpost_preview(bpost):
    """
    Shows a short preview of a blog post.
    """
    return {'bpost': bpost}
