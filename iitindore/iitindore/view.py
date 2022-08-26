from django.http import HttpResponse
from django.shortcuts import render
data={
    
    'id' :[1,2,3,4,5,6,7,8,9,10],
    'name':['Rupantar','Rittik','Sayak','Sikta','Sagnick','Satyajit','Aniket','Samik','Arindol','Bihan'],
    'password':['001','002','003','004','005','006','007','008','009','010']
}
data1={

    'comp_id' : ['01','02','03'],
    'company_name' : ['zomato','swiggy','cred'],
    'comp_ceo' : ['abc','xyz','def'],
    'comp_email' : ['abc@gmail.com','xyz@gmail.com','def@gmail.com']


}

def func(request):
    return HttpResponse("hackathon")

def reg(request):
    return render(request,"index.html",data)
def entdata(request):
    return render(request,"ent.html",data1)