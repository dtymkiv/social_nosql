from django.urls import path, include

from .views import view_profile, view_users

urlpatterns = [
    path('', view_users, name='view_users'),
    path('<str:username>/', view_profile, name='view_profile'),
    ]