from django.shortcuts import render
from django.http import HttpResponse
from collections import defaultdict
from .models import User
from .models import Address
from .models import UserDevelopEnvironmentSkill
from .models import UserProgrammingSkill
from .models import UserLicense
from .models import Agreement
from .models import Project
from .models import SubProjectOverview
from .models import ProgrammingLanguage
from .models import SubProjectProgrammingSkill
from .models import DevelopEnvironment
from .models import SubProjectEnvironmentSkill
from .models import WorkScope
from .models import Position
from .models import WorkScopeBottom
from .models import WorkScopeTop

import json
from pydoc import pager
from django.contrib.auth.decorators import login_required
from .common import get_user_id
from operator import concat
from itertools import count
from django.db.models.functions import Concat

@login_required
# Create your views here.
def skill_s(request):
    
    uid = get_user_id(request)
    
    data = User.objects.filter(user_id=uid).select_related(
        'gender',
        'address'
    ).values(
        'user_id',
        'last_name_kana',
        'first_name_kana',
        'last_name_kan',
        'first_name_kan',
        'age',
        'nationality',
        'final_education',
        'gender__gender',
        'address__railway_routes',
        'address__station',
        'address__working',
        'appeal'
    )
    
    userlicense = UserLicense.objects.filter(user_id=uid).select_related(
        'license'
    ).values(
        'license__license'    
    )


    projects = Project.objects.filter(agreement__user_id=uid, agreement__subprojectoverview__id__isnull=False).select_related(
        'agreement__subprojectoverview',
        'agreement__subprojectoverview__workscopebottom__workscope',
        'agreement__subprojectoverview__workscopetop__workscope'
    ).values(
        'agreement__id',
        'agreement__subprojectoverview__id',
        'agreement__subprojectoverview__name',
        'agreement__subprojectoverview__scale',
        'agreement__subprojectoverview__comment',
        'agreement__subprojectoverview__position__id',
        'agreement__subprojectoverview__position__name',
        'agreement__subprojectoverview__start_date',
        'agreement__subprojectoverview__end_date',
        'agreement__subprojectoverview__work_scope_bottom__workscope__name',
        'agreement__subprojectoverview__work_scope_bottom__workscope__initial',
        'agreement__subprojectoverview__work_scope_top__workscope__name',
        'agreement__subprojectoverview__work_scope_top__workscope__initial'
    ).order_by(
        # 'agreement__subprojectoverview__id',
        'agreement__subprojectoverview__end_date'
    ).distinct(
        # 'agreement__subprojectoverview__id'
        'agreement__subprojectoverview__end_date'      
    )
    
    projects = delete_if_none(projects.reverse());
    
    cnt = 0
    for index in range(len(projects)):
        cnt = cnt + 1
        projects[index]['num'] = cnt
        
    new_projects = list(projects)
    page = new_projects[:3]  
    del new_projects[:3]
    
    projects_page = []
    projects_page.append([page])
    
    while ( len(new_projects) > 0 ):
        #print(len(new_projects))
        page = new_projects[:5]
        del new_projects[:5]
        projects_page.append([page])      
    
    program_data = Project.objects.filter(agreement__user_id=uid, agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__delflg=False).select_related(
        'agreement__subprojectoverview__subprojectprogrammingskill__userprogrammingskill__programminglanguage'                                                                 
    ).values(
        'agreement__subprojectoverview__id',
        'agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__programming_language__name',
        'agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__version',
        'agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__id'     
    )

    environment_data = Project.objects.filter(agreement__user_id=uid).select_related(
        'agreement__subprojectoverview__subprojectenvironmentskill__userdevelopenvironmentskill__developenvironment'
    ).values(
        'agreement__subprojectoverview__id',
        'agreement__subprojectoverview__subprojectenvironmentskill__user_develop_environment_skill__develop_environment__name',
        'agreement__subprojectoverview__subprojectenvironmentskill__user_develop_environment_skill__version',
        'agreement__subprojectoverview__subprojectenvironmentskill__user_develop_environment_skill__id'
    )         
                              
    programs = {}
    for pd in program_data:
        id = pd['agreement__subprojectoverview__id']
        skill_id = pd['agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__id']
        version = pd['agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__version']
        name = pd['agreement__subprojectoverview__subprojectprogrammingskill__user_program_skill__programming_language__name']
        if ( name is None ) :
            name = " "
        if ( version is None ) :
            version = " "
        program_data = {'skill_id':skill_id, 'name':name + version} 
        programs.setdefault(id, []).append(program_data)
 
    environment = {}
    for ed in environment_data:
        id = ed['agreement__subprojectoverview__id']
        skill_id = ed['agreement__subprojectoverview__subprojectenvironmentskill__user_develop_environment_skill__id']
        version = ed['agreement__subprojectoverview__subprojectenvironmentskill__user_develop_environment_skill__version']
        name = ed['agreement__subprojectoverview__subprojectenvironmentskill__user_develop_environment_skill__develop_environment__name']
        #print(version)
        if ( name is None ) :
            name = " "
        if ( version is None) :
            version = " "
        environment_data = {'skill_id':skill_id, 'name':name + version}
        environment.setdefault(id, []).append(environment_data)
         
    return render(request, 'skill_s.html', {
        'data':data,
        'licenses':userlicense,
        'projects':projects,
        'programs':programs,
        'environment':environment,
        'projects_page':projects_page
    })
    
def update(request, item):
    
    uid = get_user_id(request)
    
    print("item ------------------ ")
    print(item);
    print("item ------------------ ")
    
    from django.http import HttpResponse, Http404
    
    jsondata = json.loads(request.body.decode('utf-8'))
        
    if (item == 'comment'):
        
        print(jsondata['dat']);
        id = jsondata['id']
        dat = jsondata['dat']
            
        if (id):
            p = SubProjectOverview.objects.get(id=id)
            p.comment = dat
            p.save()
     
    if (item == 'appeal') :
        
        print(jsondata['dat']);
        id = jsondata['id']
        dat = jsondata['dat']
        
        if (id):
            p = User.objects.get(user_id=id)
            p.appeal = dat
            p.save()
     
            
    if (item == 'program'):
        
        skill_id = jsondata['skill_id']
        proj_id = jsondata['proj_id']
        
        if ('del_' in skill_id):
            skill_id = skill_id.replace("del_", "")
            if (skill_id):
                p = SubProjectProgrammingSkill.objects.filter(user_program_skill_id=skill_id, subproject_overview_id=proj_id)
                p.delete()
        else:
            p = SubProjectProgrammingSkill.objects.update_or_create(user_program_skill_id=skill_id, subproject_overview_id=proj_id) 
            
            
    if (item == 'environment'):

        skill_id = jsondata['skill_id']
        proj_id = jsondata['proj_id']
        
        if ('del_' in skill_id):
            skill_id = skill_id.replace("del_", "")
            if (skill_id):
                p = SubProjectEnvironmentSkill.objects.filter(user_develop_environment_skill_id=skill_id, subproject_overview_id=proj_id)
                p.delete()
        else:
            p = SubProjectEnvironmentSkill.objects.update_or_create(user_develop_environment_skill_id=skill_id, subproject_overview_id=proj_id) 
                              
    if (item == 'work-scope-bottom'):
        
        uid = get_user_id(request)
        
        skill_id = jsondata['skill_id']
        proj_id = jsondata['proj_id'] 
            
        if (proj_id):
            id = Project.objects.filter(
                agreement__user_id=uid,
                agreement__subprojectoverview__id=proj_id
            ).select_related(
                'agreement__subprojectoverview',
                'agreement__subprojectoverview__workscopebottom__workscope'
            ).values(
                'agreement__subprojectoverview__work_scope_bottom__id',
            ).order_by(
                'agreement__subprojectoverview__end_date'
            ).distinct(
                'agreement__subprojectoverview__end_date'      
            )
            
            print(id)
            
            p = WorkScopeBottom.objects.get(id=id)
            p.workscope_id = skill_id
            p.save()
        
    
    if (item == 'work-scope-top'):
        
        uid = get_user_id(request)
        
        skill_id = jsondata['skill_id']
        proj_id = jsondata['proj_id'] 
            
        if (proj_id):
            id = Project.objects.filter(
                agreement__user_id=uid,
                agreement__subprojectoverview__id=proj_id
            ).select_related(
                'agreement__subprojectoverview',
                'agreement__subprojectoverview__workscopetop__workscope'
            ).values(
                'agreement__subprojectoverview__work_scope_top__id',
            ).order_by(
                'agreement__subprojectoverview__end_date'
            ).distinct(
                'agreement__subprojectoverview__end_date'      
            )
            
            print(id);
            
            p = WorkScopeTop.objects.get(id=id)
            p.workscope_id = skill_id
            p.save()
    
    if (item == 'position'):
        
        uid = get_user_id(request)
        
        skill_id = jsondata['skill_id']
        proj_id  = jsondata['proj_id'] 

        if ( 'del_' in skill_id ):
            skill_id = "";
            
        if (proj_id):
            id = Project.objects.filter(
                agreement__user_id=uid,
                agreement__subprojectoverview__id=proj_id
            ).select_related(
                'agreement__subprojectoverview',
            ).values(
                'agreement__subprojectoverview__id',
            ).order_by(
                'agreement__subprojectoverview__end_date'
            ).distinct(
                'agreement__subprojectoverview__end_date'      
            )
            
            p = SubProjectOverview.objects.get(id=id)
            p.position_id = skill_id
            p.save() 
    
    if (item == 'scale'):

        uid = get_user_id(request)
        
        proj_id = jsondata['id']
        dat = jsondata['dat']
            
        if (proj_id):
            id = Project.objects.filter(
                agreement__user_id=uid,
                agreement__subprojectoverview__id=proj_id
            ).select_related(
                'agreement__subprojectoverview',
            ).values(
                'agreement__subprojectoverview__id',
            ).order_by(
                'agreement__subprojectoverview__end_date'
            ).distinct(
                'agreement__subprojectoverview__end_date'      
            )
    
            if (id):
                p = SubProjectOverview.objects.get(id=id)
                p.scale = dat
                p.save()
    
                
    if (item == 'name'):

        uid = get_user_id(request)
        
        proj_id = jsondata['id']
        dat = jsondata['dat']
            
        if (proj_id):
            id = Project.objects.filter(
                agreement__user_id=uid,
                agreement__subprojectoverview__id=proj_id
            ).select_related(
                'agreement__subprojectoverview',
            ).values(
                'agreement__subprojectoverview__id',
            ).order_by(
                'agreement__subprojectoverview__end_date'
            ).distinct(
                'agreement__subprojectoverview__end_date'      
            )
    
            if (id):
                p = SubProjectOverview.objects.get(id=id)
                p.name = dat
                p.save()            
                
        
    response = json.dumps({'status' : 'OK'})
    
    return HttpResponse(response, "text/javascript")
        

def programs(request):
    
    jsondata = json.loads(request.body.decode('utf-8'))
    
    # プロジェクトID
    proj_id = jsondata['proj_id']
    
    # UserID
    uid = get_user_id(request)
    
    # サブプロジェクトのスキル一覧
    id_list = SubProjectProgrammingSkill.objects.filter(
        subproject_overview_id=proj_id
    ).values(
        'user_program_skill_id'
    )
    
    # ユーザが持っているスキル一覧
    userprogrammingskill = UserProgrammingSkill.objects.filter(
        user_id=uid, delflg=False
    ).select_related(
        'programming_language'
    # where column not in list
    ).exclude(
        id__in=id_list
    ).values(
        'id',
        'programming_language__name'
    ).annotate(
        prog_name=Concat('programming_language__name', 'version')
    )
    
    print(userprogrammingskill.query)
    print(userprogrammingskill);
    
    list = []
    for data in userprogrammingskill:
        #print(data['programming_language__name']);
        # print(data.id)
        list.append(data);
    
    new_list = json.dumps(list);
    
    response = json.dumps({
        'status' : 'OK',
        'list' : list
    })
    
    return HttpResponse(response, "text/json")

    
def environments(request):
    
    jsondata = json.loads(request.body.decode('utf-8'))
    
    proj_id = jsondata['proj_id']
    
    uid = get_user_id(request)
    
    # ユーザがそのプロジェクトの開発環境スキルとして登録している一覧
    id_list = SubProjectEnvironmentSkill.objects.filter(subproject_overview_id=proj_id).values('user_develop_environment_skill_id')
    
    print(id_list.query)
    
    # ユーザが持っている環境スキル 開発環境マスタと結合してIDと環境名を返却
    userenvironmentskill = UserDevelopEnvironmentSkill.objects.filter(user_id=uid, delflg=False).select_related(
        'develop_environment'
    # where column not in list
    # ユーザがそのプロジェクトに登録しているスキル以外を抽出するための条件
    ).exclude(
        id__in=id_list
    ).values(
        'id',
        'develop_environment__name'
    ).annotate(
        env_name=Concat('develop_environment__name', 'version')
    )
     
    # print(userenvironmentskill.query)
    # print(userenvironmentskill);
     
    list = []
    for data in userenvironmentskill:
        print(data['develop_environment__name']);
        # print(data.id)
        list.append(data);
     
    new_list = json.dumps(list);
    
    response = json.dumps({
        'status' : 'OK',
        'list' : list
    })
    
    return HttpResponse(response, "text/json")    
        
def work_scope_top(request):
    
    jsondata = json.loads(request.body.decode('utf-8'))
    
    proj_id = jsondata['proj_id']
    
    uid = get_user_id(request)
    
    # ユーザが持っている
    id_list = Project.objects.filter(
        agreement__user_id=uid,
        agreement__subprojectoverview__id=proj_id
    ).select_related(
        'agreement__subprojectoverview',
        'agreement__subprojectoverview__workscopebottom__workscope',
        'agreement__subprojectoverview__workscopetop__workscope'
    ).values(
        'agreement__subprojectoverview__work_scope_top__workscope__id',
    ).order_by(
        'agreement__subprojectoverview__end_date'
    ).distinct(
        'agreement__subprojectoverview__end_date'      
    )
     
    # 作業範囲の一覧
    workscope = WorkScope.objects.exclude(
        id__in=id_list
    ).values(
        'id',
        'name',
        'initial'
    ) 
         
    print(workscope.query)
    print(workscope);
     
    list = []
    for data in workscope:
        # print(data['agreement__subprojectoverview__work_scope_top__workscope__name']);
        # print(data)
        list.append(data);
     
    new_list = json.dumps(list);
    
    response = json.dumps({
        'status' : 'OK',
        'list' : list
    })
    
    return HttpResponse(response, "text/json")      
    
def work_scope_bottom(request):
    
    jsondata = json.loads(request.body.decode('utf-8'))
    
    proj_id = jsondata['proj_id']
    
    uid = get_user_id(request)
    
    # ユーザが持っている
    id_list = Project.objects.filter(
        agreement__user_id=uid,
        agreement__subprojectoverview__id=proj_id
    ).select_related(
        'agreement__subprojectoverview',
        'agreement__subprojectoverview__workscopebottom__workscope',
        'agreement__subprojectoverview__workscopetop__workscope'
    ).values(
        'agreement__subprojectoverview__work_scope_bottom__workscope__id',
    ).order_by(
        'agreement__subprojectoverview__end_date'
    ).distinct(
        'agreement__subprojectoverview__end_date'      
    )
     
    # 作業範囲の一覧
    workscope = WorkScope.objects.exclude(
        id__in=id_list
    ).values(
        'id',
        'name',
        'initial'
    ) 
         
    print(workscope.query)
    print(workscope);
     
    list = []
    for data in workscope:
        # print(data['agreement__subprojectoverview__work_scope_top__workscope__name']);
        # print(data)
        list.append(data);
     
    new_list = json.dumps(list);
    
    response = json.dumps({
        'status' : 'OK',
        'list' : list
    })
    
    return HttpResponse(response, "application/json")

def position(request):
    
    jsondata = json.loads(request.body.decode('utf-8'))
    
    proj_id = jsondata['proj_id']
    
    uid = get_user_id(request)
    
    # ユーザが持っている
#     id_list = Project.objects.filter(
#         agreement__user_id=uid,
#         # agreement__subprojectoverview__id__isnull=False
#         agreement__subprojectoverview__id=proj_id
#     ).select_related(
#         'agreement__subprojectoverview'
#     ).values(
#         'agreement__subprojectoverview__position__id',
#     ).order_by(
#         'agreement__subprojectoverview__end_date'
#     ).distinct(
#         'agreement__subprojectoverview__end_date'      
#     )
     
    #print(id_list);
     
    # 作業範囲の一覧
    position = Position.objects.filter(

    ).values(
        'id',
        'name'
    ) 
#    position = Position.objects.values('id','name')
         
    #print(position.query)
    #print(position);
     
    list = []
    for data in position:
        #print(data['agreement__subprojectoverview__work_scope_top__workscope__name']);
        #print(data)
        list.append(data);
     
    new_list = json.dumps(list);
    
    response = json.dumps({
        'status' : 'OK',
        'list' : list
    })
    
    return HttpResponse(response, "text/json")       
    
def delete(request):
    
    jsondata = json.loads(request.body.decode('utf-8'))
    
    proj_id = jsondata['proj_id']
    
    uid = get_user_id(request)
    
    id_list = Project.objects.filter(
        agreement__user_id=uid,
        agreement__subprojectoverview__id=proj_id
    ).select_related(
        'agreement__subprojectoverview',
    ).values(
        'agreement__subprojectoverview__id',
    )
    
    SubProjectOverview.objects.filter(
        id = proj_id
    ).delete()
        
    response = json.dumps({
        'status' : 'OK'
    })
    
    return HttpResponse(response, 'text/JSON')

# --------------------------- #
# 返却データのNoneを空にする
# --------------------------- # 
def delete_if_none(list):
    c = 0
    for dic in list:

        for k, v in dic.items():
             if v is None:
                 dic[k] = ""
                 
             print("--------------")
             print(c)
             print(dic['agreement__id'])
             print("--------------")  
             
                    
             c = dic['agreement__id']    
                 
    return list    
        
