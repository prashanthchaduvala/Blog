import datetime

from django.shortcuts import render, redirect

from blogapp1.models import Showdata

'''from .models import Showdata, Like, Post
from django.contrib.auth.models import User'''

def Loginpage(request):
    return render(request,"login.html")

def checkdata(request):
    uname=request.POST.get("t1")
    pas=request.POST.get("t2")
    if uname == "prashanth" and pas == "123456":
        return render(request,"welcome.html",{"message":"Welcome to Bloger"})
    else:
        return render(request,"Invalid.html",{"mess":"wrong username and password"})

def blog(request):
    return render(request,"blog/blog.html")

def saveblog(request):
    book = request.POST.get("b1")
    name = request.POST.get("b2")
    author = request.POST.get("b3")
    file = request.POST.get("b4")
    price = request.POST.get("b5")
    date = request.POST.get("b6")
    data = Showdata(bookno=book, name=name, author=author, file=file, price=price, date=date)
    rm = data.save()
    return render(request, "blog/show.html", {'messsa': "saved to blog"})



def savess(request):
    user=Showdata.objects.all()

    return render(request,"blog/show.html",{'messsa':user})


def saves(request):
    user=Showdata.objects.all()
    return render(request,'blog/saveblog.html',{"user":user})


def welcome(request):
    return render(request,'welcome.html')


def dash(request):
    return render(request,'dash.html')



'''def already_liked_post(user, post_id):

    post= Post.objects.get(id=post_id)
    return Like.objects.filter(user=user, post=post).exists()

def like_button_clicked(request, post_id):

    if request.user.is_authenticated():
        post = Post.objects.get(id=post_id)

        if not already_liked_post(request.user, post_id):
            Like.objects.create(user=request.user, post=post, timestamp=datetime.now())
        else:
            Like.objects.filter(user=request.user, post=post).delete()

        return redirect(reverse("index"))
    else:
        return redirect(reverse('login'))'''