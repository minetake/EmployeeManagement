from django.http.response import HttpResponse
from django.shortcuts import render

from cms.models import ProgrammingLanguage, UserProgrammingSkill
from cms.models import DevelopEnvironment, UserDevelopEnvironmentSkill
from cms.models import Project
from django.contrib.auth.decorators import login_required
from .common import get_user_id
import json

@login_required
def skill_edit(request, item):
    
    uid = get_user_id(request)
    
    programmings = ProgrammingLanguage.objects.all()
    
    userprogrammingno = {}
    userprogrammingskill = UserProgrammingSkill.objects.filter(
        user_id=uid,delflg=False
    )
    
    for line in userprogrammingskill:
        id = line.programming_language_id
        userprogrammingno.setdefault(id,"selected")
    
    environments = DevelopEnvironment.objects.all()
    
    userdevelopenvironmentno = {}
    userdevelopenvironmentskill = UserDevelopEnvironmentSkill.objects.filter(
        user_id=uid,delflg=False                                                                     
    )
    
    for line in userdevelopenvironmentskill:
        id = line.develop_environment_id
        userdevelopenvironmentno.setdefault(id,"selected")
    
    program_data = Project.objects.filter(
        agreement__user_id=uid, 
        agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__delflg=False
    ).select_related(
        'agreement__subprojectoverview__subprojectprogrammingskill__userprogrammingskill__programminglanguage'                                                                 
    ).values(
        'agreement__subprojectoverview__id',
        'agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__programming_language__name',
        'agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__version',
        'agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__id'     
    )

    userprogskill = UserProgrammingSkill.objects.filter(
        user_id=uid,delflg=False
    ).select_related(
        'userprogrammingskill__programminglanguage'
    ).values(
        'programming_language__name',
        'version',
        'id',
        'years'
    )

    programs = []
    for pd in userprogskill:
        skill_id = pd['id']
        version = pd['version']
        name = pd['programming_language__name']
        years = pd['years']
        if ( name is None ) :
            name = " "
        if ( version is None ) :
            version = " "
        program_data = {'skill_id':skill_id, 'name':name, 'version':version, 'years':years} 
        programs.append(program_data)  

    userprogskill = UserDevelopEnvironmentSkill.objects.filter(
        user_id=uid,delflg=False
    ).select_related(
        #'userprogrammingskill__programminglanguage'
        'userdevelopenvironmant__developenvironment'
    ).values(
        'develop_environment__name',
        'version',
        'id',
        'years'
    )

    envs = []
    for pd in userprogskill:
        skill_id = pd['id']
        version = pd['version']
        name = pd['develop_environment__name']
        years = pd['years']
        if ( name is None ) :
            name = " "
        if ( version is None ) :
            version = " "
        env_data = {'skill_id':skill_id, 'name':name, 'version':version, 'years':years} 
        envs.append(env_data) 


    template = "skill_edit_prg.html"
    if ( item == "program" ):
        template = "skill_edit_prg.html"
    else:
        template = "skill_edit_env.html"
       
    return render(request, template,
                {
                      'programmings' : programmings,
                      'userprogrammingno' : userprogrammingno,
                      'environments' : environments,
                      'userdevelopenvironmentno' : userdevelopenvironmentno,
                      'programs':programs,
                      'envs':envs,
                })
    
def regist(request,item):
    
    import json
    
    uid = get_user_id(request)
    
    from django.http import HttpResponse,Http404
     
    #print(request.POST.getlist('duallistbox_demo1[]'))
    
    if ( item == 'program' ):
    
        print(item)
    
        userprogrammingno = {}
        list = request.POST.getlist('duallistbox_demo1[]')
    
        if len(list) > 0:
            userprogrammingskill = UserProgrammingSkill.objects.filter(user_id=uid)
        
            for data in userprogrammingskill:
                id = data.programming_language_id
                userprogrammingno.setdefault(id,id)       
 
                #print(userprogrammingno)
     
                inputskillno = {} 
                for pid in list:
                    d = int(pid)
                    inputskillno.setdefault(d,d)
    
                    #print(inputskillno)
    
            for pid in userprogrammingno:
                k = pid
                print(k)
                #print(inputskillno.get(k))
                if ( inputskillno.get(k) == None ) :
                    print("delete")
                    s = UserProgrammingSkill.objects.filter(user_id=uid,programming_language_id=k).update(
                        delflg=True
                    )                   
                else :
                    print("update")
                    s = UserProgrammingSkill.objects.filter(user_id=uid,programming_language_id=k).update(
                        delflg=False
                    )
            
            for pid in list :
                k = pid
                print(k)
                if ( userprogrammingno.get(k) == None ) :

                    s = UserProgrammingSkill.objects.filter(user_id=uid,programming_language_id=k)
                    print(s)
                    if not ( s ):
                        print("create") 
                        UserProgrammingSkill.objects.get_or_create(
                            user_id = uid,
                            programming_language_id = k,
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
    
    return HttpResponse(response,"text/json");


def update(request, item):
    
    uid = get_user_id(request)
    
    print("item -----------------------")
    print(item)
    print("item -----------------------")
    
    from django.http import HttpResponse, Http404
    
    jsondata = json.loads(request.body.decode('utf-8'))
    
    if (item == 'version'):
        
        print(jsondata['id'])
        print(jsondata['dat'])
        id = jsondata['id']
        dat = jsondata['dat']
        
        if ( id ):
            p = UserProgrammingSkill.objects.get(id=id)
            p.version = dat
            p.save()
        
    if (item == 'years'):
        
        print(jsondata['dat'])
        id = jsondata['id']
        dat = jsondata['dat']
        
        if ( id ):
            p = UserProgrammingSkill.objects.get(id=id)
            p.years = dat
            p.save()
        
           
    response = json.dumps({'status' : 'OK'})
        
    return HttpResponse(response, "text/javascript")
        
def add(request, item):
    
    uid = get_user_id(request)
    
    print(request.POST.getlist('program')[0])
    
    pid = request.POST.getlist('program')[0]
    
    if ( item == "program"):
    
        UserProgrammingSkill.objects.create(
            user_id = uid,
            programming_language_id = pid,
            years = '1',
            delflg = False,
        )        
    
        response = json.dumps({'status' : 'OK'})
    
        return HttpResponse(response,"text/javascript")




    