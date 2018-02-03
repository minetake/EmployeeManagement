from django.contrib import admin

from .models import Address
from .models import Agreement
from .models import AgreementStatus
from .models import City
from .models import Duties
from .models import Position
from .models import Project
from .models import SubProjectOverview
from .models import Supplier
from .models import User
from .models import UnitPrice
from .models import WorkScope
from .models import WorkScopeTop
from .models import WorkScopeBottom
from .models import ProgrammingLanguage
from .models import UserProgrammingSkill
from .models import SubProjectProgrammingSkill
from .models import DevelopEnvironment
from .models import UserDevelopEnvironmentSkill
from .models import SubProjectEnvironmentSkill
from .models import Gender
from .models import License
from .models import UserLicense
from .models import LicenseLevel


# # Register your models here.
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'zip_code', 'add', 'station', 'working', 'city_id')
    list_display_links = ('id',)
admin.site.register(Address, AddressAdmin)

class AgreementAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'project', 'period', 'agreement_status')
    list_display_links = ('id',)
admin.site.register(Agreement, AgreementAdmin) 

class AgreementStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'status')
    list_display_links = ('id',)
admin.site.register(AgreementStatus, AgreementStatusAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
admin.site.register(City, CityAdmin)

class DutiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'content')
    list_display_links = ('id',)
admin.site.register(Duties, DutiesAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
admin.site.register(Position, PositionAdmin)

class ProjectAdmin(admin.ModelAdmin):
    list_display = (
                    'id', 
                    'name', 
                    #'supplier')
                    'supplier_name')
    list_display_links = ('id',)
admin.site.register(Project, ProjectAdmin)

class SubProjectOverviewAdmin(admin.ModelAdmin):
    list_display = (
                    'id', 
                    #'agreement',
                    'agreement_user',
                    'agreement_project',
                    'name',
                    'scale', 
                    'comment',
                    'position',
                    'start_date',
                    'end_date',
                    'work_scope_top',
                    'work_scope_bottom')
    list_display_links = ('id',)
admin.site.register(SubProjectOverview, SubProjectOverviewAdmin)

class SupplierAdmin(admin.ModelAdmin):
    list_display = (
                    'id', 
                    'name',
                    'address')
    list_display_links = ('id',)
admin.site.register(Supplier, SupplierAdmin)

class UnitPriceAdmin(admin.ModelAdmin): 
    list_display = ('id', 'user', 'start_date', 'price')
    list_display_links = ('id',)
admin.site.register(UnitPrice, UnitPriceAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = (
                    'id', 
                    'user_id', 
                    'last_name_kan', 
                    'first_name_kan', 
                    'password',
                    'address',
                    'duties',
                    'age',
                    'gender',
                    'auth_id')
    list_display_links = ('id',)
admin.site.register(User, UserAdmin)

class WorkScopeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'initial', 'content')
    list_display_links = ('id',)
admin.site.register(WorkScope, WorkScopeAdmin)

class WorkScopeBottomAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
admin.site.register(WorkScopeBottom, WorkScopeBottomAdmin)

class WorkScopeTopAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)
admin.site.register(WorkScopeTop, WorkScopeTopAdmin)

class ProgrammingLanguageAdmin(admin.ModelAdmin):
    list_displey = ('id', 'name')
    list_displey_links = ('id',)
admin.site.register(ProgrammingLanguage, ProgrammingLanguageAdmin)

class UserProgrammingSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'programming_language', 'years')
    list_display_links = ('id',)
admin.site.register(UserProgrammingSkill, UserProgrammingSkillAdmin)

class SubProjectProgrammingSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'subproject_overview', 'user_program_skill')
    list_display_links = ('id',)
admin.site.register(SubProjectProgrammingSkill, SubProjectProgrammingSkillAdmin)
    
class DevelopEnvironmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id',)
admin.site.register(DevelopEnvironment, DevelopEnvironmentAdmin)
    
class UserDevelopEnvironmanetSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'develop_environment', 'version', 'years')
    list_display_links = ('id',)
admin.site.register(UserDevelopEnvironmentSkill, UserDevelopEnvironmanetSkillAdmin)

class SubProjectEnvironmanetSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'subproject_overview', 'user_develop_environment_skill')
    list_display_links = ('id',)
admin.site.register(SubProjectEnvironmentSkill, SubProjectEnvironmanetSkillAdmin)

class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender')
    list_display_links = ('id',)
admin.site.register(Gender, GenderAdmin)

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'license')
    list_display_links = ('id',)
admin.site.register(License, LicenseAdmin)

class UserLicenseAdmin(admin.ModelAdmin):
    list_display = ('id', 'license')
    list_display_links = ('id',)
admin.site.register(UserLicense, UserLicenseAdmin)

class LicenseLevelAdmin(admin.ModelAdmin):
    list_display = ('id', 'level', 'comment')
    list_display_links = ('id',)
admin.site.register(LicenseLevel, LicenseLevelAdmin)
