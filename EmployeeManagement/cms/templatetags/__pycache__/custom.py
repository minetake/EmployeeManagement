from django import template
from time import time
from datetime import timedelta
from dateutil.relativedelta import relativedelta

register = template.Library()

def lookup(value, arg, default=""):
    if arg in value:
        return value[arg]
    else:
        return default
register.filter('lookup',lookup)


def bitween(value, arg, default=""):

    after = time()
    before = value
    if arg :
        after = arg + timedelta(days=31)   
    delta = relativedelta(after, before)
    if ( delta.year ) :
        return str(delta.year) + "年" + str(delta.months) + "ヶ月"
    else :
        return str(delta.months) + "ヶ月"    
register.filter('bitween',bitween)


def cut(value,arg):
    return value.replace(arg,'')
register.filter('cat',cut)

