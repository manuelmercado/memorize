# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.http import *
from django.shortcuts import render_to_response,redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from forms import *

def login_user(request):
    logout(request)
    username = password = ''
    error_m = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        else:
            error_m = 'El usuario o la contraseña no son correctos'
    return render_to_response('singin.html', {'error_m':error_m,}, context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')
