from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login

from .forms import Register
from .forms import EventSubmit

def register(request):
    form=Register(request.POST or None)
    return render(request, 'register.html', {'form':form, 'my_template': 'NotLoggedIn.html'})


def eventSubmit(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request, 'eventSubmit.html',context)




def buy(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'buy.html',context)

def about(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'AboutUs.html',context)

def login(request):

    return render(request, 'Login.html', { 'my_template': 'LoggedInTemplate.html'})

def manage(request):
    return render(request, 'modiriat.html', {'my_template': 'NotLoggedIn.html'})


    """  error=None
    if request.user.is_authenticated():
        return HttpResponseRedirect('/main/'+request.user.username)
    else:
        if request.method=="POST":
            usern=request.POST.get('username',None)
            passw=request.POST.get('password',None)
            user = authenticate(username=usern,password=passw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/main/'+request.user.username)
            else:
                error='Username or Password is wrong'"""


def main(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'MainPage.html',context)

def home(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'homepage.html',context)

def event(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'event.html',context)

def report(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'Report.html',context)

def contact(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'contact.html',context)

def event_report(request):
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'EventReport.html',context)

