from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.FloatField(max_length=10, default=0.0)

    def __str__(self):
        return f'{self.user.username} ~ {self.rating}'

    def update_rating(self):
        posts_r = Post.objects.filter(author=self.id).values('rating')
        comment_r = Comment.objects.filter(user=self.id).values('rating')
        posts = Post.objects.filter(author=self.id)
        posts_comm_r = []
        total = 0

        for post in posts:
            posts_comm_r.append(Comment.objects.filter(post=post).values('rating'))
        for r in posts_r:
            for key, value in r.items():
                total += value * 3
        for r in comment_r:
            for key, value in r.items():
                total += value
        for s in posts_comm_r:
            for r in s:
                for key, value in r.items():
                    total += value

        self.rating = total
        self.save()


class Category(models.Model):
    position = models.CharField(max_length=128, unique=True)
    description = models.CharField(max_length=512, default='Категория')

    def __str__(self):
        return f'{self.position}'


class Subscriber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subscriptions = models.ManyToManyField(Category, through='CategorySubscriber')

    def __str__(self):
        return f'{self.user}'


class CategorySubscriber(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    subscriptions = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subscriber} ~ {self.subscriptions}'


class Post(models.Model):
    article, news = 'A', 'N'
    POSITIONS = [
        (article, 'Статья'),
        (news, 'Новость')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    type = models.CharField(max_length=1, choices=POSITIONS, default=article)
    date = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=256)
    text = models.TextField()
    rating = models.FloatField(max_length=10, default=0.0)
    categories = models.ManyToManyField(Category, through="PostCategory")

    def __str__(self):
        return f'{self.title} ~ {self.text[:50]}...'

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:124] + '...'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.post} ~ {self.category}'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(max_length=10, default=0.0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
