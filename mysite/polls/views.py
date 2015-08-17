from random import randint
from django.shortcuts import render
from polls.forms import EventForm, TicketTypeFormSet
from polls.models import Category,SubCategory, Event, EventTicketType, Order, Comment
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
from django.forms.utils import ErrorList
from django.db import IntegrityError
import datetime


from .forms import Register
from .forms import EventSubmit

def register(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/main/')
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()


    user = UserProfile()

    if request.method== 'POST':
        form=Register(request.POST)
        context = {'form': form,'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}


        if form.is_valid():

            if form.cleaned_data['password'] != form.cleaned_data['passwordRetype']:
                form._errors["password"] = ErrorList(["Passwords do not match"])
                return render(request, 'register.html', context)
            if User.objects.filter(username = form.cleaned_data['userName']).exists():
                form._errors["userName"] = ErrorList(["User already exists"])
                return render(request, 'register.html', context)
            form._errors["userName"] = ErrorList(["this user already exists"])
            user.user=User.objects._create_user(form.cleaned_data['userName'],form.cleaned_data['email'],form.cleaned_data['password'],False,False,first_name=form.cleaned_data['name'],last_name=form.cleaned_data['lastName'])
            user.gender=form.cleaned_data['gender']
            user.save()
            return HttpResponseRedirect('/login/')


    else:
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






def buy(request, event_id):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()

    event = Event.objects.get(id=event_id)

    typ = EventTicketType.objects.get(id=request.POST.get('type'))
    count = int(request.POST.get('numoftickets'))
    price = typ.price * count

    if count > typ.tickets:
        return HttpResponseRedirect('/event/%s?error=1' % event_id)

    if request.POST.get('done', 0):
        typ.tickets -= count
        typ.save()
        order = Order(user=request.user, event=event, cost=price, number=count, rahgiriCode=randint(1000000, 9999999),
                      ticket_type=typ)
        order.save()
        return HttpResponseRedirect('/event/%s?bought=%d' % (event_id, order.id)) # todo: change with receipt page

    if request.user.is_superuser:
        context = {'my_template': 'adminTemplate.html', 'categories': categories, 'subcats': subcats, 'event': event
            , 'typ': typ, 'count': count, 'price': price}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html', 'categories': categories, 'subcats': subcats,
                       'event': event, 'typ': typ, 'count': count, 'price': price}
        else:
            context = {'my_template': 'NotLoggedIn.html', 'categories': categories, 'subcats': subcats, 'event': event
                , 'typ': typ, 'count': count, 'price': price}

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
                error='Username and Password do not match'

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
    newEvents = Event.objects.all().order_by('-date')[:6]
    popular = Event.objects.all().order_by('-score')[:6]
    if request.user.is_superuser:
         context = {'superuser': True,'login': True,'categories': categories, 'subcats': subcats,'new': newEvents, 'popular': popular}
    else:
        if request.user.is_authenticated():
            context = {'login': True,'categories': categories, 'subcats': subcats,'new': newEvents, 'popular': popular}
        else:
            error='You must first login'
            context = {'login': False,'categories': categories, 'subcats': subcats,'new': newEvents, 'popular': popular , 'error' : error}

    return render(request, 'homepage.html', context)

def event(request, event_id):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    event = Event.objects.all().filter(id=event_id)[0]
    if request.method=='POST':
        commentContent=request.POST.get('content', None)
        userID = request.POST.get('user-id', None)
        user=UserProfile.objects.filter(id=userID)[0]
        newComment= Comment()
        newComment.content=commentContent
        newComment.author=user
        newComment.time=datetime.datetime.now()
        newComment.event=event
        newComment.save()
    error = request.GET.get('error', 0)
    bought = request.GET.get('bought', 0)
    comments= Comment.objects.all().filter(event = event).order_by('time')
    order = None
    if bought:
        order = Order.objects.get(id=bought)

    if request.user.is_superuser:
        context = {'my_template': 'adminTemplate.html', 'categories': categories, 'subcats': subcats, 'event': event,
                   'error': error, 'order': order, 'comments': comments}
    else:
        if request.user.is_authenticated():
            context = {'my_template': 'LoggedInTemplate.html', 'categories': categories, 'subcats': subcats,
                       'event': event, 'error': error, 'order': order, 'comments': comments}
        else:
            context = {'my_template': 'NotLoggedIn.html', 'categories': categories, 'subcats': subcats, 'event': event,
                       'error': error, 'order': order, 'comments': comments}

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
    event = Event.objects.get(id=event_id)

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
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save(commit=False)
            formset = TicketTypeFormSet(request.POST, request.FILES, instance=event)
            #event.user_id = request.user.userprofile.id
            if formset.is_valid():
                event.save()
                formset.save()
            return HttpResponseRedirect('/manage/')
        else:
            formset = TicketTypeFormSet(request.POST, request.FILES, instance=event)
    else:
        form = EventForm(instance=event)
        formset = TicketTypeFormSet(instance=event)

    context = {'form': form, 'my_template': 'adminTemplate.html', 'sub_cats_list': sub_cats_list,
               'categories': categories, 'subcats': subcats, 'formset': formset}
    return render(request, 'eventSubmit.html',context)

def Logout(request):
 logout(request)
 return HttpResponseRedirect('/login/')

def eventRate(request, event_id, rate):
    event=Event.objects.all().filter(id=event_id)[0]
    #user = UserProfile.objects.all().filter(id=user_id)[0]
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    if event.numberofScorers==0:
        event.score=rate
        event.numberofScorers+=1
    else:
        event.score=(event.score*event.numberofScorers+float(rate))/(event.numberofScorers+1)
        event.numberofScorers+=1
    event.save()
    print(event.score)
    print(rate)
    return HttpResponseRedirect('/event/'+event_id)