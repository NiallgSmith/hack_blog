import arrow
from django import template
from django.core.urlresolvers import reverse
from django.shortcuts import redirect


register = template.Library()

@register.filter
def get_total_subject_posts(subject):
    total_posts = 0
    for thread in subject.threads.all():
        total_posts += thread.posts.count()
    return total_posts

@register.filter
def started_time(created_at):
    return arrow.get(created_at).humanize()

@register.filter
def last_posted_user_name(thread):
    if thread.posts.count() > 0:
        posts = thread.posts.all().order_by('-created_at')
        return posts[posts.count()-1].user.username

    else:
        return "This thread is empty"

