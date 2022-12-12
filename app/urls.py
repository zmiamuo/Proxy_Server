from django.urls import path
from . import views

urlpatterns = [
    path('', views.indexo, name='indexo'),
    path('login',views.login_view,name='login'),
    path('register',views.register_user,name='register'),
    path('logout',views.logout,name='logout')
    
]