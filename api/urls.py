from django.urls import path, include, re_path
from .views import UserDetailView, UserListView, UserRegistrationView

app_name = 'api'


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user_register'),
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:id>/', UserDetailView.as_view(), name='user-_etail'), 
]
