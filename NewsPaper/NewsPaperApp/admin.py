from django.contrib import admin
from .models import *


admin.site.register(Author)
admin.site.register(Subscriber)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(CategorySubscriber)
admin.site.register(PostCategory)
admin.site.register(Comment)
