from django.shortcuts import render_to_response,render,get_object_or_404, redirect  
from django.http import HttpResponse, HttpResponseRedirect  
from django.contrib.auth.models import User  
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext

from django.forms.formsets import formset_factory
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.decorators.csrf import csrf_protect
# from bootstrap_toolkit.widgets import BootstrapUneditableInput
from django.contrib.auth.decorators import login_required

from .forms import LoginForm, RegistrationForm

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
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'index.html',
    { 'user': request.user }
    )

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render_to_response('account/login.html', RequestContext(request, {'form': form,}))
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=username, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return redirect('login')
                return render(request, 'account/index.html')
                # return render('account/index.html', RequestContext(request))
            else:
                return render_to_response('account/login.html', RequestContext(request, {'form': form,'password_is_wrong':True}))
        else:
            return render_to_response('account/login.html', RequestContext(request, {'form': form,}))

def password_reset(request):
    response = "You're trying to reset your password"
    return HttpResponse(response)

# def home():
#     return render(request, 'account/index.html')