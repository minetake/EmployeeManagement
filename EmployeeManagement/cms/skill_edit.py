from django.http.response import HttpResponse
from django.shortcuts import render

from cms.models import ProgrammingLanguage, UserProgrammingSkill
from cms.models import DevelopEnvironment, UserDevelopEnvironmentSkill
from django.contrib.auth.decorators import login_required
from .common import get_user_id

@login_required
def skill_edit(request):
    
    uid = get_user_id(request)
    
    programmings = ProgrammingLanguage.objects.all()
    
    userprogrammingno = {}
    userprogrammingskill = UserProgrammingSkill.objects.filter(user_id=uid,delflg=False)
    
    for line in userprogrammingskill:
        id = line.programming_language_id
        userprogrammingno.setdefault(id,"selected")
    
    print(userprogrammingno)
    
    environments = DevelopEnvironment.objects.all()
    
    userdevelopenvironmentno = {}
    userdevelopenvironmentskill = UserDevelopEnvironmentSkill.objects.filter(user_id=uid,delflg=False)
    
    for line in userdevelopenvironmentskill:
        id = line.develop_environment_id
        userdevelopenvironmentno.setdefault(id,"selected")
    
    print(userdevelopenvironmentno)
        
    return render(request, 'skill_edit.html',
                {
                      'programmings' : programmings,
                      'userprogrammingno' : userprogrammingno,
                      'environments' : environments,
                      'userdevelopenvironmentno' : userdevelopenvironmentno
                })
    
def regist(request,item):
    
    import json
    
    uid = get_user_id(request)
    
    from django.http import HttpResponse,Http404
    
    #print(request.POST.getlist('duallistbox_demo1[]'))
    
    if ( item == 'program' ):
     
        userprogrammingno = {}
        list = request.POST.getlist('duallistbox_demo1[]')
     
        if len(list) > 0:
            userprogrammingskill = UserProgrammingSkill.objects.filter(user_id=uid)
         
            for data in userprogrammingskill:
                id = data.programming_language_id
                userprogrammingno.setdefault(id,id)       
  
                print(userprogrammingno)
      
                inputskillno = {} 
                for pid in list:
                    d = int(pid)
                    inputskillno.setdefault(d,d)
     
                    print(inputskillno)
     
            for pid in userprogrammingno:
                k = pid
                print(inputskillno.get(k))
                if ( inputskillno.get(k) == None ) :
                    s = UserProgrammingSkill.objects.filter(user_id=uid,programming_language_id=k).first()
                    s.delflg = True
                    s.save()
                else :
                    s = UserProgrammingSkill.objects.filter(user_id=uid,programming_language_id=k).first()
                    s.delflg = False
                    s.save()
             
            for pid in list :
                k = pid
                if ( userprogrammingno.get(k) == None ) :
                    UserProgrammingSkill.objects.get_or_create(
                        user_id = uid,
                        programming_language_id = pid,
                        years = '1',
                        delflg = False,
                    )
    
    if ( item == 'environment' ):
    
        userdevelopenvironmentno = {}
        list = request.POST.getlist('duallistbox_demo2[]')
    
        if len(list) > 0:
            userdevelopenviromentskill = UserDevelopEnvironmentSkill.objects.filter(user_id=uid)
        
            for data in userdevelopenviromentskill:
                id = data.develop_environment_id
                userdevelopenvironmentno.setdefault(id,id)       
 
                print(userdevelopenvironmentno)
     
                inputskillno = {} 
                for pid in list:
                    d = int(pid)
                    inputskillno.setdefault(d,d)
    
                    print(inputskillno)
    
            for pid in userdevelopenvironmentno:
                k = pid
                print(inputskillno.get(k))
                if ( inputskillno.get(k) == None ) :
                    s = UserDevelopEnvironmentSkill.objects.filter(user_id=uid,develop_environment_id=k).first()
                    s.delflg = True
                    s.save()
                else :
                    s = UserDevelopEnvironmentSkill.objects.filter(user_id=uid,develop_environment_id=k).first()
                    s.delflg = False
                    s.save()
            
            for pid in list :
                k = pid
                if ( userdevelopenvironmentno.get(k) == None ) :
                    UserDevelopEnvironmentSkill.objects.get_or_create(
                        user_id = uid,
                        develop_environment_id = pid,
                        years = '1',
                        delflg = False,
                    )
    
    
    
    
    
    
    response = json.dumps({'status' : 'OK'})
    
    return HttpResponse(response,"text/javascript");
    