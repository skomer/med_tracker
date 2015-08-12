from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf


# Create your views here.


def idontknowwhatyet(request):
	print "bluegreenred"
	return render('')


def load_registration_page(request):
	return render(request, 'med_tracker_app/main.html', {})


def create_user(request):
	username = request.POST.get('username')
	email  = request.POST.get('email')
	password = request.POST.get('password')
	user = User.objects.create_user(username,email,password)
	user.save()
	return render(request, 'med_tracker_app/user_dash.html', {})


def login_auth(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)
	if user is not None:
	    # the password verified for the user
	    login(request, user)
	    return render(request, 'med_tracker_app/user_dash.html', {'good_login': "Welcome back!"})
	else:
	    # the authentication system was unable to verify the username and password
		return render(request, 'med_tracker_app/main.html', {'failed_login': "The username or password was incorrect."})


def log_out(request):
	logout(request)
	return render(request, 'med_tracker_app/main.html', {'logout': "You have successfully logged out."})


# def lookup(request,num):
# 	p = Product.objects.get(pk=num)
# 	return render(request, 'ecommerce_app/singleproduct.html', {})



def user_account(request):
	return render('')


def user_dash(request):
	return render(request, 'med_tracker_app/user_dash.html')

