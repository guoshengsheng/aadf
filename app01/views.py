from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.
def Users(request123):
    456789
    obj_list=models.User.objects.all().select_related()
    for i in obj_list:
        print(i.name,i.department.title,i.role.title)
    return HttpResponse("OK")



