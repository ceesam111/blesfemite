from django.urls import path
from . import views

#urlpatterns = [
#	path('' , views.index, name= 'index')
#]

#from django.urls import path
#from app_users import views


# app_name = 'app_users'
urlpatterns = [
    path('',views.HomeView.as_view(),name='index'),
    path('register/', views.register, name='register'),
    path('user_login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('blog/', views.blog, name='blog'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.ContactView.as_view(), name="contact"),
    
]