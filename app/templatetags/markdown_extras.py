from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter
def markdown_to_html(value):
    """
    Convert markdown text to HTML.
    
    Usage: {{ some_text|markdown_to_html }}
    """
    if not value:
        return ""
    
    # Configure markdown with commonly used extensions
    md = markdown.Markdown(extensions=[
        'markdown.extensions.tables',
        'markdown.extensions.fenced_code',
        'markdown.extensions.codehilite',
        'markdown.extensions.nl2br',
        'markdown.extensions.toc',
    ])
    
    html = md.convert(value)
    return mark_safe(html)