from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.blogs, name='index'),
    path('blog-detail/<int:id>/', views.blog_detail, name='blog_detail'),
    path('comment/create/', views.comment_create, name='comment_create'),
    path('register-user', views.register_user, name='register_user'),
    path('dashboard/', include('main.dashboard.urls')),
    path('log-in', views.login_user, name='login_user'),
    path('log-out', views.log_out, name='log_out')
]