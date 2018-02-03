"""EmployeeManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from cms import index, list, views, skill_s, skill, skill_edit, project_edit, maps, engineer, user, skill_edit_prg
from django.contrib import admin
from distutils.sysconfig import project_base
from cms import new_test
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^login/', login, {'template_name': 'login.html'}, name='login'),
    url(r'^index/', index.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^engineer/$', engineer.view, name='engineer-view'),
    url(r'^engineer/list/$', engineer.list, name='engineer-list'),
    url(r'^maps/$', maps.maps, name='maps'),
    url(r'^maps/supplier/$', maps.supplier, name='supplier'),
    url(r'^skill-edit/$', skill_edit.skill_edit, name='skill-edit'),
    url(r'^skill-edit/list/(?P<item>[a-z]+)', skill_edit_prg.skill_edit, name='skill-edit'),
    url(r'^skill-edit/program/update/(?P<item>[a-z]+)', skill_edit_prg.update, name='update'),
    url(r'^skill-edit/regist/(?P<item>[a-z]+)',skill_edit_prg.regist, name='regist'),
    url(r'^skill-edit/add/(?P<item>[a-z]+)',skill_edit_prg.add, name='add'),
    url(r'^skill-s/$', skill_s.skill_s, name='skill-s'),
    url(r'^skill-s/update/(?P<item>[a-z-]+)', skill_s.update, name='skill-update'),
    url(r'^skill-s/programs/$', skill_s.programs, name='skill-programs'),
    url(r'^skill-s/environments/$', skill_s.environments, name='skill-environments'),
    url(r'^skill-s/work-scope-top/$', skill_s.work_scope_top, name='skill-work_scope_top'),
    url(r'^skill-s/work-scope-bottom/$', skill_s.work_scope_bottom, name='skill-work_scope_bottom'),
    url(r'^skill-s/position/$', skill_s.position, name='skill-position'),
    url(r'^skill-s/delete/$', skill_s.delete, name='skill-delete'),
    url(r'^skill/', skill.skill, name='skill'),
    url(r'^project-edit/$', project_edit.project_edit, name='project-edit'),
    url(r'^project-edit/regist$', project_edit.regist, name='project-edit-regist'),
    url(r'^project-list$', project_edit.project_list, name='project-list'),
    url(r'^user/$', user.get_data, name='user'),
    url(r'^list/', list.list, name='list'),
    url(r'^template/$', views.hello_template,name='hello_template'),
    url(r'^sample1/$', new_test.sample_1,name='sample1'),
    url(r'^sample2/$', new_test.sample_2,name='sample2'),
    url(r'^sample3/$', new_test.sample_3,name='sample3'),
]
