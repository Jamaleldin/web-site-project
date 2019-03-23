# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from .forms import UserLoginForm


def login_view(request):
    title = "Login"
    #next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        #if next:
            #return redirect(next)
        return redirect("/")
        
    context = {
        "form": form,
        "title": title,
    }
    return render(request, "posts/form.html", context)

    
def logout_view(request):
    logout(request)
    return redirect("/")
