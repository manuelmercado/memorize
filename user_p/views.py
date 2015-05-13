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
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    return render_to_response('singin.html', context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

#def login_view(request):
#    form = LoginForm(request.POST or None)
#    if request.POST and form.is_valid():
#        user = form.login(request)
#        if user:
#            login(request, user)
#            return HttpResponseRedirect("/")# Redirect to a success page.
#    return render(request, 'login_2.html', {'login_form': form })
