from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.decorators import login_required
from myapp.models import Blogsite
from myapp.forms import *
from django.contrib import messages


# Create your views here.
def index(request):
  blogs = Blogsite.objects.order_by('-publish_date')
  return render(request,'myapp/home.html',{'data':blogs})  

def registerview(request):
  if request.method == 'POST':
    form = NewUserForm(request.POST)
    if form.errors:
      print(form.errors)
    if form.is_valid():
      form.save()
      return redirect('myapp:login_page')
  else:
    form = NewUserForm()
  context={'form':form,}
  return render(request,'myapp/register.html',context)
  
def loginview(request):
  if request.method =='POST':
    form = RegisteredUserForm(request.POST)
    uname=request.POST['username']
    upass=request.POST['password']
    user = authenticate(request,username=uname, password=upass)

    if user is not None:
      login(request,user)
      return redirect('myapp:index_page')     
    elif user is None:
      error_message='incorrect username or password'
      return render(request, 'myapp/login.html',{'form':form,'error':error_message })
    else:
      error_message='incorrect username or password'
      return render(request, 'myapp/login.html',{'form':form,'error':error_message })

  form=RegisteredUserForm()
  return render(request, 'myapp/login.html',{'form':form, })

def logoutview(request):
  logout(request)
  return redirect('myapp:index_page')



def writestory(request):
  if not request.user.is_authenticated:
    raise Http404

  if request.method == 'POST':
    form = BlogForm(request.POST or None, request.FILES or None)
    if form.errors:
      print(form.errors)
    if form.is_valid():
      instance = form.save(commit=False) 
      instance.author = request.user
      instance.save()
      messages.success(request,'created successfully')
      return redirect('myapp:user_blogs')
      
  form = BlogForm()
  return render(request,"myapp/user_page.html",{'form':form})

@login_required(login_url='/login_page')
def user_blogs(request):
  author = request.user
  data = Blogsite.objects.filter(author=author).order_by('-publish_date')
  return render(request,'myapp/user_blogs.html',{'data':data})


def EditBlogs(request, pk):

    blog_instance = Blogsite.objects.get(id=pk)
    fm = BlogForm(instance=blog_instance)
    if request.method=='POST':
      fm = BlogForm(request.POST, request.FILES, instance=blog_instance)
      if fm.is_valid():
        fm.save()
        
        return redirect('myapp:user_blogs')

    
    return render(request, 'myapp/user_page.html', {'form':fm})



def DeleteBlogs(request,pk):
  b = Blogsite.objects.get(id=pk)
  b.delete()

  return redirect ('myapp:user_blogs')


def authorBlogs(request,pk):
  blogs= Blogsite.objects.filter(author=pk).order_by('-publish_date')
  return render(request,'myapp/author_page.html',{'data':blogs})

