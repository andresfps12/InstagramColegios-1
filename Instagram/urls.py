from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^Login/$', auth_views.LoginView.as_view(template_name='Login.html',redirect_authenticated_user=True),name='Login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(),name='logout'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^profile/$', views.profile, name= 'profile')
    ]
