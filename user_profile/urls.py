from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'user_profile'

urlpatterns = [
    path('profile/', views.user_profile, name='user_profile'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),


]