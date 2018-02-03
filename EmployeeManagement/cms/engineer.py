from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User
from .models import UserProgrammingSkill
from django.core import serializers

@login_required
def view(request):    
    return render(request, 'engineer.html')

def list(request):
    
    import json
    
    from django.http import HttpResponse,Http404
    
    data = User.objects.select_related(
        'address',
        'userprogrammingskill_programminglanguage',
        'agreement'
    ).values(
        'user_id',
        'last_name_kan',
        'first_name_kan',
        'userprogrammingskill__programming_language__name',
        'userprogrammingskill__years',
        'address__station',
        'agreement__period'
    ).order_by(
        'user_id',
        'userprogrammingskill__years'
    ).reverse(
    ).distinct(
        'user_id',
        #'userprogrammingskill__years'     
    )
    
    newdata = {}
    newdata['data'] = []
    for line in data:
        #print(line)
        newdata['data'].append(line)
    
    response = json.dumps(newdata)
    
    print(response)
    
    return HttpResponse(response, "text/json")

    