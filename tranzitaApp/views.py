from django.shortcuts import redirect, render
from django.contrib import messages

from .models import URL
import random

# Create your views here.

def index(request):
    urls = URL.objects.all().order_by("-id")
    context = {
        'urls':urls,
    }
    return render(request, "index.html", context)

def urlGenerator():
    li = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']
    new_url_endpoint = random.choice(li) + random.choice(li) + random.choice(li) + random.choice(li) + random.choice(li) + random.choice(li)
    new_url = f"http://127.0.0.1:8000/{new_url_endpoint}/"
    if URL.objects.filter(generated_url=new_url).exists():
        urlGenerator()
    else:
        return new_url


def urlConvert(request):
    if request.method=="POST":
        url = request.POST.get("url")
        if URL.objects.filter(original_url=url).exists():
            messages.error(request, "URL already converted")
            return redirect("home")
        else:
            gen_url = urlGenerator()
            form = URL(original_url=url, generated_url=gen_url)
            form.save()
            messages.success(request,'URL converted successfully!')
            return redirect("home")
    else:
        return redirect("home")

def deleteURL(request, id):
    url = URL.objects.get(id=id)
    url.delete()
    return redirect("home")

