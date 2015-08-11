from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template.context_processors import csrf


# Create your views here.


def idontknowwhatyet(request):
	return HttpResponse('')


def load_registration_page(request):
	return render(request, 'med_tracker_app/register.html', {})


def create_user(request):
	user_name = request.POST.get('username')
	email  = request.POST.get('email')
	password = request.POST.get('password')
	user = User.objects.create_user(user_name,email,password)
	user.save()
	print "blah"
	return render(request, 'med_tracker_app/test.html', {})


def authenticate(request):
	user = authenticate(username='username', password='password')
	if user is not None:
	    # the password verified for the user
	    if user.is_active:
	        print("User is valid, active and authenticated")
	    else:
	        print("The password is valid, but the account has been disabled!")
	else:
	    # the authentication system was unable to verify the username and password
	    print("The username and password were incorrect.")
	return HttpResponse('')


def user_account(request):
	return HttpResponse('')


def user_dash(request):
	return HttpResponse('')