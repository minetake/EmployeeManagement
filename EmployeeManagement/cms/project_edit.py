from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Project, UserProgrammingSkill, ProgrammingLanguage, SubProjectOverview, Agreement, User
from django.contrib.auth.decorators import login_required
from .common import get_user_id

@login_required
def project_edit(request):

    uid = get_user_id(request)
        
    projects = Project.objects.filter(
        agreement__user_id=uid
    ).distinct('agreement__project__id')
    
    programmings = UserProgrammingSkill.objects.filter(user_id=uid,delflg=False)   
            
    return render(request, 'project_edit.html', {
        'projects':projects,
        'programmings' : programmings
    })

def project_list(request):
    
    import json
    
    uid = get_user_id(request)
    
    from django.http import HttpResponse,Http404

    projects = Project.objects.filter(
        agreement__user_id=uid,
        name__contains=request.POST.get('param1')
    ).distinct('agreement__project__id')

    if ( not projects ):
        projects = Project.objects.filter(
        agreement__user_id=uid
        ).distinct('agreement__project__id')
        
    data = []
 
    for line in projects:
        #print(vars(line));
        data.append({'label' :line.name, 'data' : line.id});
        #data.append(line);
    
    print(data);
    
    response = json.dumps(data)
    
    return HttpResponse(response, "text/json");

    
def regist(request):
    
    uid = get_user_id(request)
    
    import json
    
    from django.http import HttpResponse,Http404
    
    print("project edit regist -------------------")
    print(request.POST.get('project'))
    print(request.POST.get('projectid'))
    print(request.POST.get('start_date'))
    print(request.POST.get('end_date'))
    print(request.POST.get('comment'))
    
    project_id = request.POST.get('projectid')
    name = request.POST.get('subproject')
    work_scope_bottom_id = "1"
    work_scope_top_id = "5"
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    comment = request.POST.get('comment')
    
    agreement_id = Agreement.objects.filter(user_id=uid,project_id=project_id).first()
    
    print(agreement_id.id)
    
    if ( agreement_id ):
        SubProjectOverview.objects.get_or_create(
            agreement_id = agreement_id.id,
            name = name,
            work_scope_bottom_id = work_scope_bottom_id,
            work_scope_top_id = work_scope_top_id,
            start_date = start_date.replace('/','-'),
            end_date = end_date.replace('/','-'),
            comment = comment
        )
        
    response = json.dumps({'status' : 'OK'})
    
    return HttpResponse(response, "text/javascript")
        
    