from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.CreatePostView.as_view(), name='create_post'),
    path('<int:pk>/', views.ListUpdateDestroyPostView.as_view(), name='single_post')
]