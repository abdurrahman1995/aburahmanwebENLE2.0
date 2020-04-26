from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from mysite.polls.aform import uadminform
from mysite.polls.models import User_Admin

def usradmin(request):
    if request.method == "POST":
        aform = uadminform(request.POST)
        if aform.is_valid():
            try:
                aform.save()
                return redirect()
            except:
                pass
    else:
        aform =uadminform()
    return render(request, "register.html", {'form': aform})


