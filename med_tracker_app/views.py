from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
from models import Medication, Event




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


# 	# take request from website
# 	# request will be something like, load all events for this med and this user in this date range.
# 	# user id you will get via authenticate somehow
# 	# med and associated units user will specify at the top of the page
# 	# with this info, plus what you get back from the database, you could start to build a hash or something that you can then display?
# 	# like taking json data and displaying it from a hash?


@login_required#(redirect_field_name='/register/')
def add_med(request):
	generic_name = request.POST.get('generic_name')
	units = request.POST.get('units')
	user = request.user.pk
	new_med_entry = Medication()	#.objects.create(generic_name=generic_name, units, user)
	new_med_entry.generic_name = generic_name
	new_med_entry.units = units
	new_med_entry.user = request.user
	new_med_entry.save()
	return render(request, 'med_tracker_app/landing.html', {})


def log_out(request):
	logout(request)
	return render(request, 'med_tracker_app/main.html', {'logout': "You have successfully logged out."})


def user_account(request):
	return render('')


@login_required#(redirect_field_name='/register/')
def user_dash(request):
	return render(request, 'med_tracker_app/user_dash.html')

