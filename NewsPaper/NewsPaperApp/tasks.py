from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *


@shared_task
def notify_new_post(post_id, categories):
    post = Post.objects.get(id=post_id)
    for category in categories:
        subscribers = list(CategorySubscriber.objects.filter(subscriptions=category).values('subscriber__user'))
        users_id = [a['subscriber__user'] for a in subscribers]
        for id in users_id:
            user = User.objects.get(id=id)
            new_post_mailing(user, post)


@shared_task
def weekly_notify():
    subscribers, categories = Subscriber.objects.all(), Category.objects.all()
    d = timezone.now() - timezone.timedelta(days=7)
    for category in categories:
        posts = list(Post.objects.filter(date__gte=d, categories=category))
        for subscriber in subscribers:
            if CategorySubscriber.objects.filter(subscriptions=category.id, subscriber=subscriber).exists():
                user = subscriber.user
                weekly_mailing(user, posts, category)


def new_post_mailing(user, post):
    html_content = render_to_string(
        'account/email/new_posts_mailing.html',
        {
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


def weekly_mailing(user, posts, category):
    html_content = render_to_string(
        'account/email/last_week_posts_mailing.html',
        {
            'user': user,
            'posts': posts,
            'category': category,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Последние публикации из категории ' + category.position,
        body='',
        to=[user.email],
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()
