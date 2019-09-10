from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('<int:pk>/', views.SinglePostView.as_view(), name='single_post')
]