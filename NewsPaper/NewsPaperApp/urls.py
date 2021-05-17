from django.urls import path
from .views import PostsList, PostDetail, PostsSearch, PostCreate, PostUpdate, PostDelete

urlpatterns = [
    path('', PostsList.as_view()),
    path('<int:pk>', PostDetail.as_view(), name='product_detail'),
    path('search', PostsSearch.as_view(), name='product_search'),
    path('create', PostCreate.as_view(), name='product_create'),
    path('update/<int:pk>', PostUpdate.as_view(), name='product_create'),
    path('delete/<int:pk>', PostDelete.as_view(), name='product_delete'),
]
