from django.conf.urls import url

from . import views

urlpatterns = [

	url(r'^home/', views.load_home, name='idontknowwhatyet'),
	url(r'^register/', views.load_registration_page, name='register'),
	url(r'^firstsignin/', views.create_user, name='firstsignin'),
	url(r'^login/', views.login_auth, name='login_auth'),
	url(r'^logout/', views.log_out, name='log_out'),
	url(r'^dashboard/', views.user_dash, name='user_dash'),
	url(r'^account/', views.user_account, name='user_account'),
	url(r'^add_med/', views.add_med, name='add_med'),
	# url(r'^add_event/', views.add_event, name='add_event'),


]