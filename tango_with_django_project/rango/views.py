from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.shortcuts import render
from rango.models import Category, Page
from rango.forms1 import CategoryForm,UserForm,UserprofileForm


def index(request):
    category_list = Category.objects.order_by("-likes")
    pages_view = Page.objects.order_by("-views")
    context_dict = {"categories": category_list, "pages_view": pages_view}
    return render(request, "rango/index.html", context=context_dict)


def greet(request):
    print(request.method)
    print(request.user)
    return HttpResponse("<h1> thsis is greeting</h1>")

@login_required
def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        page = Page.objects.filter(category=category)
        context_dict["pages"] = page
        context_dict["category"] = category
    except Category.DoesNotExist:
        index(request)
        context_dict["category"] = None
        context_dict["pages"] = None

    return render(request, "rango/category.html", context_dict)

@login_required
def add_category(request):
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            form_error=form.errors
            print(form.errors)
    else:
        form = CategoryForm()

    return render(request, "rango/add_category.html", {"form": form})

def register(request):
    registered=False
    if request.method=='POST':
        print(request.POST)
        print(request.FILES)
        user_form=UserForm(data=request.POST)
        profile_form=UserprofileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            profile=profile_form.save(commit=False)
            profile.user=user
            if 'picture' in request.FILES:
                profile.picture=request.FILES['picture']
            profile.save()
            registered=True
        else:
            print (user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserprofileForm()
    
    return render(request,"rango/register.html",{"user_form":user_form,"profile_form":profile_form,"registered":registered})

def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return index(request)
            else:
                return HttpResponse("YOUR RANGO ACCOUNT IS DISABLED")
        else:
            print("invalid login details:{0},{1}".format(username,password))
            return render(request,"rango/login.html",{"errors":"Invalid login details"})
    else:
        return render(request,"rango/login.html",{})

@login_required
def user_logout(request):
    logout(request)
    return index(request)