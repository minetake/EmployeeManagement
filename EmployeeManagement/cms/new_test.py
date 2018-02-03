from django.http import HttpResponse
from time import sleep

import json

def sample_1(request):
    
    sleep(10)
    print("sample1")
    
    response = json.dumps({'status' : 'sample1'})
    
    return HttpResponse(response,"text/javascript");

def sample_2(request):
    
    sleep(10)
    print("sample2")
    
    response = json.dumps({'status' : 'sample2'})
    
    return HttpResponse(response,"text/javascript");

def sample_3(request):
    
    sleep(10)
    print("sample3")
    
    response = json.dumps({'status' : 'sample3'})
    
    return HttpResponse(response,"text/javascript");