from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('stream/<int:pk>/', views.get_streaming_video, name='stream'),
    path('<int:pk>/', views.get_video, name='player'),
    path('login', views.LoginUser.as_view(), name='login'),
    path('register', views.RegisterUser.as_view(), name='register'),
    path('logout', views.logout_user, name='logout'),
    path('delete/<int:pk>', views.delete_video, name='delete'),
    path('image_edit/<int:pk>', views.edit_video, name='edit'),
]
