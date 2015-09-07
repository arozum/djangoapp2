import os
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View
from django.views.generic.list import ListView
import errno
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

from django.core.urlresolvers import get_callable

from importlib import import_module

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return redirect('/templado/')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/register.html', {'form': form,    })

def must_login(func):
	def _decorated(request, *args, **kwargs):
		if not request.user.is_authenticated():
			return redirect('/accounts/login/')
		else:
			if not request.user.is_active:
				return redirect(request, 'accounts/banned.html', {})
		return func(request,*args, **kwargs)
	return _decorated   

def getNameDecorators(value):
	mod = import_module('accounts')
	view_func = getattr(mod,settings.TEMPLADO_DECORATOR_AUTH)
	return get_callable(view_func())
	#return value
	
