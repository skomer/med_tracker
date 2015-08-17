from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.template.context_processors import csrf
from django.conf import settings
from django.contrib.auth.decorators import login_required
from models import Medication, Event


# Create your views here.


def load_home(request):
	return render(request, 'med_tracker_app/main.html')


def load_registration_page(request):
	return render(request, 'med_tracker_app/main.html', {})


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


def create_user(request):
	username = request.POST.get('username')
	email  = request.POST.get('email')
	password = request.POST.get('password')
	user = User.objects.create_user(username,email,password)
	user.save()
	user_login = authenticate(username=username, password=password)
	login(request, user_login)
	return render(request, 'med_tracker_app/user_dash.html', {})


# take request from website
# request will be something like, load all events for this med and this user in this date range.
# user id you will get via authenticate somehow
# med and associated units user will specify at the top of the page
# with this info, plus what you get back from the database, you could start to build a hash or something that you can then display?
# like taking json data and displaying it from a hash?


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
	# use redirect here
	return HttpResponseRedirect(reverse('med_tracker_app:user_dash'))
	# return render(request, 'med_tracker_app/user_dash.html', { 'new_med' : "You added a new medication."})


@login_required
def add_event(request):
	date = request.POST.get('date')
	event_type = request.POST.get('event_type')
	description = request.POST.get('description')
	dosage = request.POST.get('dosage')
	medication_id = int(request.POST.get('select_med'))
	user_id = request.user.pk
	new_event_entry = Event()
	new_event_entry.date = date
	new_event_entry.event_type = event_type
	new_event_entry.description = description
	new_event_entry.dosage = dosage
	new_event_entry.medication_id = medication_id
	new_event_entry.user_id = user_id
	new_event_entry.save()
	#return render(request, 'med_tracker_app/user_dash.html', { 'new_event' : "You added a new event." })
	return HttpResponseRedirect(reverse('med_tracker_app:user_dash'))



def log_out(request):
	logout(request)
	# use redirect here
	return render(request, 'med_tracker_app/main.html', {'logout': "You have successfully logged out."})


@login_required
def user_account(request):
	user_id = request.user.pk
	# can I use a request/query thing here, like in user_dash() below, rather than a for loop?
	for item in User.objects.values_list('username', 'id', 'email'):
		if item[1] == user_id:
			print item
			username = item[0]
			user_email = item[2]
	return render(request, 'med_tracker_app/account.html', { 'username' : username, 'user_email' : user_email })


@login_required#(redirect_field_name='/register/')
def user_dash(request):
	user_id = request.user.pk
	# if the med's foreign key is the same as the user_id of the user currently logged in, then get that med
	# use the following syntax for one-to-many queries, rather than using a for loop
	user_meds = request.user.medication_set.all()
	user_events = request.user.event_set.all()
	return render(request, 'med_tracker_app/user_dash.html', { 'your_meds' : user_meds, 'your_events' : user_events })



