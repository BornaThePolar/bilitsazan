from django.shortcuts import render
from polls.forms import EventForm
from polls.models import Category,SubCategory,Event
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout


from .forms import Register
from .forms import EventSubmit

def register(request):
    form=Register(request.POST or None)
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD

    if request.user.is_authenticated():
        context = {'form': form,'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'register.html', context)
=======
    return render(request, 'register.html', {'form':form, 'my_template': 'NotLoggedIn.html','categories': categories,'subcats' : subcats })
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389


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
            event.user_id = request.user.userprofile.id
            event.save()
            return HttpResponseRedirect('/manage/')
    else:
        form = EventForm()

<<<<<<< HEAD
    if request.user.is_authenticated():
        context = {'form': form,'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'eventSubmit.html', context)


=======
    context = {'form': form, 'my_template': 'LoggedInTemplate.html', 'sub_cats_list': sub_cats_list,'categories': categories,'subcats' : subcats}
    return render(request, 'eventSubmit.html',context)
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389




def buy(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD
    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'buy.html', context)


=======
    return render(request, 'buy.html', { 'my_template': 'LoggedIn.html',
                                           'categories': categories,'subcats' : subcats})
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

def about(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD

    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'about.html', context)


=======
    return render(request, 'AboutUs.html', { 'my_template': 'LoggedIn.html',
                                           'categories': categories,'subcats' : subcats})

def login(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
    return render(request, 'Login.html', { 'my_template': 'NotLoggedIn.html',
                                           'categories': categories,'subcats' : subcats})

def manage(request):
    category = Category.objects.all()
    subcat = SubCategory.objects.all()
    event = Event.objects.all()
    return render(request, 'manage.html', {'my_template': 'LoggedInTemplate.html', 'category': category, 'subcategory': subcat, 'event': event})
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

def log(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()

<<<<<<< HEAD
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
    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'manage.html', context)


=======
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

def main(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD
    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'MainPage.html', context)
=======
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'MainPage.html',context)
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

def home(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD

    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'homepage.html', context)
=======
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'homepage.html',context)
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

def event(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD
    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'event.html', context)
=======
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'event.html',context)
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

def report(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD
    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'report.html', context)
=======
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'Report.html',context)
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

def contact(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD
    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'contact.html', context)

=======
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'contact.html',context)
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

def event_report(request):
    categories = Category.objects.all()
    subcats = SubCategory.objects.all()
<<<<<<< HEAD
    if request.user.is_authenticated():
        context = {'my_template': 'LoggedInTemplate.html','categories': categories, 'subcats': subcats}
    else:
         context = {'my_template': 'NotLoggedIn.html','categories': categories, 'subcats': subcats}

    return render(request, 'EventReport.html', context)

=======
    context = {'my_template': 'NotLoggedIn.html'}
    return render(request,'EventReport.html',context)
>>>>>>> 115b76d3576eea38134c91ecb351464babcf3389

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

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
