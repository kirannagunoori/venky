from django.shortcuts import render
from django.views.generic import View,CreateView
from .models import User,Donor


class SaveUser(View):
    def post(self,request):
        uname=request.POST.get("uname")
        uemail = request.POST.get("uemail")
        upassword = request.POST.get("upassword")
        User(uname=uname,uemail=uemail,password=upassword).save()
        return render(request,"userlogin.html",{"msg1":"user details are saved"})
class SaveDonor(View):
    def post(self,request):
        dname=request.POST.get("dname")
        demail=request.POST.get("demail")
        dpass=request.POST.get("dpassword")
        dage=request.POST.get("dage")
        dwieght=request.POST.get("dweight")
        dblood=request.POST.get("dgroup")
        dcontact=request.POST.get("dcontact")
        dcity=request.POST.get("dcity")
        dstate=request.POST.get("dstate")
        Donor(name=dname,email=demail,password=dpass,age=dage,
              weigth=dwieght,blood_group=dblood,
              contact=dcontact,city=dcity,state=dstate).save()
        return render(request,"donorlogin.html",{"msg":"donor succesfully register"})
class DonorLoginchek(View):
    def post(self,request):
        username=request.POST.get("uname")
        userpass = request.POST.get("upass")
        try:
            c=Donor.objects.get(name=username,password=userpass)
            if c:
                return render(request,"donorviewreq.html")
            else:
                return render(request, "donorlogin.html", {"ms": "invalid details"})
        except:
            return render(request, "donorlogin.html",{"ms":"invalid details"})


class UserLoginchek(View):
    def post(self,request):
        username=request.POST.get("uname")
        userpass = request.POST.get("upass")
        try:
            c=User.objects.get(uname=username,password=userpass)
            if c:
                return render(request,"usersendreq.html")
            else:
                return render(request, "userlogin.html", {"ms": "invalid details"})
        except:
            return render(request, "userlogin.html",{"ms":"invalid details"})