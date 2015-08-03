from django.shortcuts import render
from polls.models import Category,SubCategory
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
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    return render(request, 'manage.html', {'my_template': 'LoggedInTemplate.html', 'category': category, 'subcategory': subcat})


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

def AddCategory(request,category_name):
    newCategory = Category()
    newCategory.name=category_name
    newCategory.save()
    print('hello')
    return HttpResponseRedirect('/manage/')

def AddSubCategory(request,subcategory_name, subcategory_id):
    newSubCat= SubCategory()
    newSubCat.name=subcategory_name
    category = Category.objects.filter(id=subcategory_id)[0]
    newSubCat.daste=category
    newSubCat.save()
    return HttpResponseRedirect('/manage/')