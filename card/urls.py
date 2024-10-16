from django.urls import path
from . import views

app_name = 'card'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/update/', views.update, name='update'),
    path('new-card/', views.new_card, name='new_card'),
]
