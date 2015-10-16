from django.shortcuts import render_to_response,render,get_object_or_404, redirect  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_protect
from pprint import pprint
# from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegistrationForm
def my_login_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.is_authenticated()):
            return HttpResponseRedirect('/account/login')
        else:
            return function(request, *args, **kw)
    return wrapper
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/account/login/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'account/register.html',
    variables,
    )
@login_required
def logout(request):

    logout(request)
    return HttpResponseRedirect('account/index.html')
 
@login_required
def home(request):
    request.user.username = request.user.username.upper()
    return render_to_response(
    'account/index.html',
    { 'user': request.user }
    )

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('account/login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            # print(password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('http://127.0.0.1:8000/account/')
                # return render(request, 'account/index.html')
                # return render('account/index.html', RequestContext(request))
            else:
                return render(request, 'account/login.html', {'form': form}) 
                # render_to_response('account/login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render(request, 'account/login.html', {'form': form})
            # render_to_response('account/login.html', RequestContext(request, {'form': form,}))

def password_reset(request):
    response = "You're trying to reset your password"
    return HttpResponse(response)
