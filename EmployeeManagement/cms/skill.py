from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def skill(request):    
    return render(request, 'skill.html')