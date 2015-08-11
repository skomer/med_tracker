from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^home/', views.idontknowwhatyet, name='idontknowwhatyet'),
	url(r'^register/', views.load_registration_page, name='register'),
	url(r'^firstsignin/', views.create_user, name='firstsignin'),
	url(r'^login/', views.idontknowwhatyet, name='idontknowwhatyet'),
	url(r'^logout/', views.idontknowwhatyet, name='idontknowwhatyet'),
	url(r'^/(\d+)/$', views.user_dash, name='user_dash'),
	url(r'^/(\d+)/dashboard/', views.user_dash, name='user_dash'),
	url(r'^/(\d+)/account/', views.user_account, name='user_account'),


]