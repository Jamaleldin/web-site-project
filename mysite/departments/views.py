# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def computer(request):
    return render(request, 'departments/computer.html')

def electric(request):
    return render(request, 'departments/electric.html')

def mecha(request):
    return render(request, 'departments/mecha.html')
