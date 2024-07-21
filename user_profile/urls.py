from django.urls import path

from .views import *




urlpatterns = [
    
    path('login/', login_user, name='login'),
    path('register_user/', register_user, name='register_user'),
    path('logout/', logout_user, name='logout'),
    path('profile/', profile, name='profile'),
    path('change_profile_picture/', change_profile_picture, name='change_profile_picture'),
    path('view_user_information/<str:username>/', view_user_information, name="view_user_information"),
    path('follow_or_unfollow/<int:user_id>/', follow_or_unfollow_user, name='follow_or_unfollow_user'),
]