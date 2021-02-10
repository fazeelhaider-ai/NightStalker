from django.urls import path
from .views import PostListView, PostDetailView
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='case-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='about-case'),
    path('admin/', views.login, name='login-admin'),
]
