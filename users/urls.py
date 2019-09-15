from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('', views.UsersView.as_view(), name='user_list'),
    path('<int:pk>/', views.RetrieveUpdateDeleteUserView.as_view(), name='user_details'),
    path('<int:pk>/posts/', views.RetrieveUserPostsView.as_view(), name='user_posts')
]
