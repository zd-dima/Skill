from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from .models import *
import inspect


@receiver(post_save, sender=Post)
def notify_managers_post(sender, instance, created, **kwargs):
    for frame_record in inspect.stack():
        if frame_record[3] == 'get_response':
            request = frame_record[0].f_locals['request']
            break
    else:
        request = None
    if not request.POST.getlist('mailing'):
        return False
    post = Post.objects.get(id=instance.id)
    categories = request.POST.getlist('categories')
    for category in categories:
        subscribers = list(CategorySubscriber.objects.filter(subscriptions=category).values('subscriber__user'))
        users_id = [a['subscriber__user'] for a in subscribers]
        for id in users_id:
            user = User.objects.get(id=id)
            mailing(user, post, request)


def mailing(user, post, request):
    html_content = render_to_string(
        'account/email/new_posts_mailing.html',
        {
            'site': 'http://' + get_current_site(request).domain,
            'user': user,
            'post': post
        }
    )
    msg = EmailMultiAlternatives(
        subject=post.title,
        body=post.text,
        to=[user.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
