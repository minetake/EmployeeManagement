from django.db import models
from django.contrib.auth import settings

# Create your models here.
class User(models.Model):
    
    user_id = models.IntegerField('社員番号')
    last_name_kan = models.CharField('姓', max_length=20)
    first_name_kan = models.CharField('名', max_length=20)
    last_name_kana = models.CharField('セイ', max_length=30)
    first_name_kana = models.CharField('メイ', max_length=30)
    password = models.CharField('パスワード', max_length=20)
    address = models.ForeignKey('Address', blank=True, null=True)
    duties = models.ForeignKey('Duties', blank=True, null=True)
    age = models.IntegerField('年齢')
    gender = models.ForeignKey('Gender', blank=True, null=True)
    nationality = models.CharField('国籍', max_length=100)
    final_education = models.CharField("最終学歴", max_length=200)
    appeal = models.CharField('アピール', max_length=1000)
    last_update = models.DateTimeField('last update', auto_now=True)
    auth_id = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def __str__(self):
        return self.last_name_kan + ' ' + self.first_name_kan
    
class Project(models.Model):
     
    name = models.CharField('案件名', max_length=20)
    supplier = models.ForeignKey('Supplier')
    last_update = models.DateTimeField('last update', auto_now=True)
     
    def __str__(self):
        return self.name

    def supplier_name(self):
        return self.supplier.name
    
    #supplier_name.allow_tags = True
    #supplier_name.admin_order_field = 'supplier.name'
    
class Supplier(models.Model):
     
    name = models.CharField('会社名', max_length=128)
    address = models.ForeignKey('Address', blank=True, null=True)
    last_update = models.DateTimeField('last update', auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
    
class Agreement(models.Model):
     
    user = models.ForeignKey('User')
    project = models.ForeignKey('Project')
    start_date = models.DateField('開始日')
    period = models.IntegerField('期間')
    work_add = models.ForeignKey('Address', blank=True, null=True)
    agreement_status = models.ForeignKey('AgreementStatus')
    redeem = models.IntegerField('請け')
    last_update = models.DateTimeField('last update', auto_now=True)

#     def __unicode__(self):
#         return self.user

    def __str__(self):
        return self.project.name
     
class SubProjectOverview(models.Model):
     
    agreement = models.ForeignKey('Agreement')
    #project = models.ForeignKey('Project')
    name = models.CharField('プロジェクト名', max_length=100)
    scale = models.IntegerField('規模', blank=True, null=True)
    comment = models.CharField('プロジェクト概要', max_length=200)
    position = models.ForeignKey('Position', blank=True, null=True)
    start_date = models.DateField('開始日', blank=True, null=True)
    end_date = models.DateField('終了日', blank=True, null=True)
    work_scope_top = models.ForeignKey('WorkScopeTop')
    work_scope_bottom = models.ForeignKey('WorkScopeBottom')
    last_update = models.DateTimeField('last update', auto_now=True)
 
    def __str__(self):
        return self.name
 
    # 管理ツールにobjectではなく名称を載せるためのメソッド
    # admin.pyのSubProjectOverviewAdminクラス参照
    def agreement_user(self):
        return self.agreement.user
    
    def agreement_project(self):
        return self.agreement.project
 
class Position(models.Model):
     
    name = models.CharField('', max_length=20)
    last_update = models.DateTimeField('last update', auto_now=True)
    
    def __str__(self):
        return self.name
     
class AgreementStatus(models.Model):
    
    status = models.CharField('契約状況', max_length=10)
    last_update = models.DateTimeField('last update', auto_now=True)
    
    def __str__(self):
        return self.status

    
class Address(models.Model):
    
    zip_code = models.IntegerField('郵便番号')
    city = models.ForeignKey('City')
    add = models.CharField('住所', max_length=50)
    railway_routes = models.CharField('路線', max_length=50)
    station = models.CharField('駅', max_length=10)
    working = models.IntegerField('徒歩')
    
    def __str__(self):
        return self.add
    
class City(models.Model):
    
    name = models.CharField('都道府県', max_length=10)
    
    def __str__(self):
        return self.name

    
class UnitPrice(models.Model):
    
    user = models.ForeignKey('User', blank=True, null=True)
    start_date = models.DateField('開始日')
    price = models.IntegerField('単価')
    
    def __unicode__(self):
        return unicode(self.start_date) + " " + unicode(self.price)

"-----------------------------------"
" 作業範囲 "
" 要件定義　設計 実装 テスト " 
" 開発工程 "
"-----------------------------------"
class WorkScope(models.Model):
    
    name = models.CharField('作業範囲', max_length=100)
    initial = models.CharField('略称', max_length=10)
    content = models.CharField('内容', max_length=100)
    
    def __str__(self):
        return self.name

"-----------------------------------"
" 役割 "
" PM PL SE PG "
"-----------------------------------"    
class Duties(models.Model):
    
    name = models.CharField('役割', max_length=10)
    content = models.CharField('内容', max_length=200) 
     
    def __str__(self):
        return self.name
    
class WorkScopeTop(models.Model):
    
    workscope = models.ForeignKey('WorkScope')

    def __str__(self):
        return self.workscope.name
    
class WorkScopeBottom(models.Model):
    
    workscope = models.ForeignKey('WorkScope')
    
    def __str__(self):
        return self.workscope.name
    
class ProgrammingLanguage(models.Model):
    
    name = models.CharField('名前', max_length=100)
    
    def __str__(self):
        return self.name
    
class UserProgrammingSkill(models.Model):

    user = models.ForeignKey('User', blank=True, null=True)
    programming_language = models.ForeignKey('ProgrammingLanguage', blank=True, null=True)
    version = models.CharField('バーション', max_length=50)
    years = models.IntegerField('経験年数')
    delflg = models.BooleanField('削除フラグ', default=False)

    def __str__(self):
        return self.programming_language.name
    
class SubProjectProgrammingSkill(models.Model):

    subproject_overview = models.ForeignKey('SubProjectOverview', blank=True, null=True)
    user_program_skill = models.ForeignKey('UserProgrammingSkill', blank=True, null=True)

    def __unicode__(self):
        return self.user_program_skill
    
class DevelopEnvironment(models.Model):
    
    name = models.CharField('名前', max_length=100)
    
    def __str__(self):
        return self.name
    
class UserDevelopEnvironmentSkill(models.Model):
    
    user = models.ForeignKey('User', blank=True, null=True)
    develop_environment = models.ForeignKey('DevelopEnvironment', blank=True, null=True)
    version = models.CharField('バージョン', max_length=50)
    years = models.IntegerField('経験年数')
    delflg = models.BooleanField('削除フラグ')
    
    def __str__(self):
        return self.develop_environment.name
    
class SubProjectEnvironmentSkill(models.Model):
    
    subproject_overview = models.ForeignKey('SubProjectOverview', blank=True, null=True)
    user_develop_environment_skill = models.ForeignKey('UserDevelopEnvironmentSkill', blank=True, null=True)
    
class Gender(models.Model):
    
    gender = models.CharField('性別', max_length=50)

    def __str__(self):
        return self.gender
    
class UserLicense(models.Model):
    
    user = models.ForeignKey('User', blank=True, null=True)
    license = models.ForeignKey('License', blank=True, null=True)
    
    def __int__(self):
        return self.license
    
class License(models.Model):
    
    license = models.CharField('資格名', max_length=100)
    license_level = models.ForeignKey('LicenseLevel', blank=True, null=True)
       
    def __str__(self):
        return self.license
    
class LicenseLevel(models.Model):
    
    level = models.IntegerField('レベル')
    comment = models.CharField('内容', max_length=300)
    
    def __str__(self):
        return self.comment
    
    