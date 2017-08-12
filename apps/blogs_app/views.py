# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response = "Placeholder to later display all the lists of blogs"
    return HttpResponse(response)

def new(request):
    response = "Placeholder to display a form to create a new blog"
    return HttpResponse(response)

def create():
    return redirect('/blogs')

def show(request):
    response = "Placeholder to display blog {{number}}"
    return HttpResponse(response)

def edit(request):
    response = "Placeholder to edit blog {{number}}"
    return HttpResponse(response)

def destroy():
    return redirect ('/blogs')
