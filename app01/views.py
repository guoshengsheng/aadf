from django.shortcuts import render,HttpResponse
from app01 import models
# Create your views here.
def Users(request123):
    obj_list=models.User.objects.all().select_related()
    for i in obj_list:
        print(i.name,i.department.title,i.role.title)
        master开发完毕
    return HttpResponse("OK")
3333333333333333
4444444444444444
开发小视频完毕
0000000000000000
1111111111111111
2222222222222222
