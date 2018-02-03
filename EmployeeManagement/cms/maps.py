from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Supplier

import json

@login_required
def maps(request):    
    return render(request, 'maps.html')

def supplier(request):
    
    datas = Supplier.objects.all(
    
    ).select_related(
        'address'   
    ).values(
        'id',
        'name',
        'address__add'
    )
    
    list = []
    for data in datas:
        print(data)
        list.append(data)
    
    print(list);

    response = json.dumps({
        'status' : 'OK',
        'list' : list
    })
    
    return HttpResponse(response, "application/json")