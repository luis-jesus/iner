#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

def home_page(request):
    context = {
        "title":"Acerca de",
        "content": "Welcome to about page"
    }
    return render(request, "home_page.html", context)
