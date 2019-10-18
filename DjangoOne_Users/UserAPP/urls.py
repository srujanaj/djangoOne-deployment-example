from django.conf.urls import url
from .import views

app_name = 'userapp'

urlpatterns=[
  url(r'users/',views.users,name='users'),
  url(r'signup/',views.signup,name='signup'),
  url(r'register/',views.register,name='register'),
  url(r'user_login/',views.user_login,name='user_login'),

]
