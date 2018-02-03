from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import User

@login_required
def get_data(request):
    
    import json
    
    from django.http import HttpResponse,Http404
    
    user = User.objects.filter(auth_id=request.user.id).values(
        'last_name_kan',
        'first_name_kan'
    )
    
    list = []
    for data in user:
        #print(data)
        #response = json.dumps(data)
        list.append(data);
        
    print(list[0])    
        
    response = json.dumps( {'status' : 'OK', 'data' : list[0] } );   
    
    print(response)
    
    return HttpResponse(response, "text/json")

    