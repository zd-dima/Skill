from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='product_detail'),
    path('category/<int:pk>', CategoryDetail.as_view(), name='CategoryDetail'),
    path('search', PostsSearch.as_view(), name='product_search'),
    path('create', PostCreate.as_view(), name='product_create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='product_create'),
    path('delete/<int:pk>', PostDelete.as_view(), name='product_delete'),
    path('upgrade/', become_author, name='upgrade'),
    path('subscribe/<int:pk>', subscribe_category, name='subscribe_category'),
    path('unsubscribe/<int:pk>', unsubscribe_category, name='unsubscribe_category'),
]
