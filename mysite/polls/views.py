from django.shortcuts import render
from polls.forms import EventForm, TicketTypeFormSet
from polls.models import Category,SubCategory, Event
from django.http import HttpResponseRedirect
from django.contrib.auth import logout

from .forms import Register
from .forms import EventSubmit

from django.shortcuts import render
from polls.forms import EventForm
from polls.models import Category,SubCategory
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from polls.models import UserProfile
from django.contrib.auth.models import User



from .forms import Register
from .forms import EventSubmit

def register(request):

    categories = Category.objects.all()
    subcats = SubCategory.objects.all()


    user = UserProfile()
    if request.method== 'POST':
        print('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy')
        form=Register(request.POST)
        if form.is_valid():
           # valid = True
            if form.cleaned_data['password'] != form.cleaned_data['passwordRetype']:
                form._errors["password"] = ErrorList([u"Passwords do not match"])
            user.user=User.objects._create_user(form.cleaned_data['userName'],form.cleaned_data['email'],form.cleaned_data['password'],False,False,first_name=form.cleaned_data['name'],last_name=form.cleaned_data['lastName'])

           # user.user.first_name=form.cleaned_data['name']
          #  user.user.last_name=form.cleaned_data['lastName']
            user.birthday=form.cleaned_data['birthday']
            #user.photo=None
            #user.follower=[]
            #user.following=[]
            user.save()
            return HttpResponseRedirect('/main/')
    else:
        print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
        form=Register()


    context = {'form': form,'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}
    return render(request, 'register.html', context)


def eventSubmit(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    sub_cats_list = {}
    for cat in Category.objects.all():
        l = {}
        subcats = cat.subcategory_set.all()
        for s in subcats:
            l[s.id] = str(s.name)
        sub_cats_list[cat.id] = l

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            formset = TicketTypeFormSet(request.POST, request.FILES, instance=event)
            #event.user_id = request.user.userprofile.id
            if formset.is_valid():
                event.save()
                formset.save()
            return HttpResponseRedirect('/manage/')
    else:
        form = EventForm()
        formset = TicketTypeFormSet()

    if request.user.is_superuser:
         context = {'form': form, 'formset': formset,'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats, 'sub_cats_list': sub_cats_list}
    else:
        if request.user.is_authenticated():
            context = {'form': form, 'formset': formset, 'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats, 'sub_cats_list': sub_cats_list}
        else:
            context = {'form': form, 'formset': formset, 'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats, 'sub_cats_list': sub_cats_list}

    return render(request, 'eventSubmit.html', context)






def buy(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()

    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
        else:
            context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'buy.html', context)



def about(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()

    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats}
    else:
        if request.user.is_authenticated():
         context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
        else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'AboutUs.html', context)



def log(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()

    error=None
    if request.user.is_authenticated():
       return HttpResponseRedirect('/main/')
    else:
        if request.method=="POST":
            usern=request.POST.get('username',None)
            passw=request.POST.get('password',None)
            user = authenticate(username=usern,password=passw)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/main/')
            else:
                error='Username or Password is wrong'

    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats , 'error':error}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats , 'error':error}

    return render(request, 'Login.html', context)

def manage(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    event = Event.objects.all()

    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','category': categories, 'subcategory': subcats, 'event': event}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','category': categories, 'subcategory': subcats, 'event': event}
        else:
         context = {'my_template': 'NotLoggedIn.html','category': categories, 'subcategory': subcats, 'event': event}

    return render(request, 'manage.html', context)



def main(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    event = Event.objects.all()
    popular = Event.objects.all().order_by('-score')
    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats ,'event': event}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats,'event': event}
        else:
         error='You must first login'
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats,'event': event,'error':error}

    return render(request, 'MainPage.html', context)

def mainFilter(request,category_name):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    event = Event.objects.filter(category__name = category_name)
    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats,'event': event}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats,'event': event}
        else:
            context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats,'event': event}

    return render(request, 'MainPage.html', context)

def mainFilterSub(request,category_name, subcategory_name):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    event = Event.objects.filter(category__name = category_name).filter(subCategory__name = subcategory_name)
    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats,'event': event}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats,'event': event}
        else:
            context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats,'event': event}

    return render(request, 'MainPage.html', context)

def home(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    newEvents = Event.objects.all().order_by('-date')
    popular = Event.objects.all().order_by('-score')
    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats,'new': newEvents, 'popular': popular}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats,'new': newEvents, 'popular': popular}
        else:
            error='You must first login'
            context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats,'new': newEvents, 'popular': popular , 'error' : error}

    return render(request, 'homepage.html', context)

def event(request, event_id):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    event = Event.objects.all().filter(id=event_id)
    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats, 'event': event}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats, 'event': event}
        else:
             context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats, 'event': event}

    return render(request, 'event.html', context)

def report(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
        else:
            context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'report.html', context)


def all_tickets(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()

    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
        else:
            context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'ticketHistory.html', context)


def contact(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
        else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'contact.html', context)


def event_report(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    if request.user.is_superuser:
         context = {'my_template': 'adminTemplate.html','categories': categories, 'subcats': subcats}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
        else:
            context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'EventReport.html', context)


def AddCategory(request,category_name):
    newCategory = Category()
    newCategory.name=category_name
    newCategory.save()
    return HttpResponseRedirect('/manage/')

def AddSubCategory(request,subcategory_name, subcategory_id):
    newSubCat= SubCategory()
    newSubCat.name=subcategory_name
    category = Category.objects.filter(id=subcategory_id)[0]
    newSubCat.daste=category
    newSubCat.save()
    return HttpResponseRedirect('/manage/')

def RemoveCategory(request, category_id):
    category=Category.objects.filter(id=category_id)[0]
    subcategory=SubCategory.objects.filter(daste=category)
    for subcat in subcategory:
        subcat.delete()
    if category is not None:
        category.delete()
    return HttpResponseRedirect('/manage/')

def RemoveSubCategory(request, subcategory_id):
    subcat = SubCategory.objects.filter(id=subcategory_id)[0]
    if subcat is not None:
        subcat.delete()
    return HttpResponseRedirect('/manage/')

def RemoveEvent(request, event_id):
    event = Event.objects.filter(id=event_id)[0]
    if event is not None:
        event.delete()
    return HttpResponseRedirect('/manage/')

def EditEvent(request,event_id):
    event = Event.objects.filter(id=event_id)
    if event is not None:
        event.delete()
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    sub_cats_list = {}
    for cat in Category.objects.all():
        l = {}
        subcats = cat.subcategory_set.all()
        for s in subcats:
            l[s.id] = str(s.name)
        sub_cats_list[cat.id] = l

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            #event.user_id = request.user.userprofile.id
            event.save()
            return HttpResponseRedirect('/manage/')
    else:
        form = EventForm()

    context = {'form': form, 'my_template': 'adminTemplate.html', 'sub_cats_list': sub_cats_list,'categories': categories,'subcats' : subcats}
    return render(request, 'eventSubmit.html',context)

def Logout(request):
 logout(request)
 return HttpResponseRedirect('/login/')