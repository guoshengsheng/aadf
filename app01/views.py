from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.
def Users(request123):
    obj_list=models.User.objects.all().select_related()
    for i in obj_list:
        print(i.name,i.department.title,i.role.title)
        6666666666


    return HttpResponse("OK")
77777777777777

