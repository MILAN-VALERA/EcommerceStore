from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

from django.views.decorators.csrf import csrf_exempt
from .models import User
import datetime

def signup(request):

    return render(request,'signup.html')

@csrf_exempt
def signin(request):
    if  request.method == "POST":
            formEmail = request.POST['email']
            formPass  = request.POST['password'] 
      
            userData = User.objects.filter(usermailId=formEmail).values()
            if(len(userData) != 0):
                if(userData[0]['userPassword'] == formPass):

                    userData[0].pop('userPassword')
                    newUserData = userData[0]
                    return JsonResponse({"error":"","data":newUserData})
                else:
                    return JsonResponse({"error":"something went wrong"})
            else:
                return JsonResponse({"error":"may be email id is wrong"})

            
            
            
        
    
    return render(request,'signin.html')



def userDetail(request):
    if request.method == "POST":       
        if request.POST['hiddenValue']  == "new":
            uname = request.POST.get('username')
            useremail = request.POST['useremail']
            password = request.POST['password']
            phoneNo= request.POST['phoneNo']
            age= request.POST['age']
            maxAmount = request.POST['maxpurchase']
            address= request.POST['address']
            pincode= request.POST['pincode']
            credicrad_1 = request.POST['CreditCard1']
            credicrad_2 = request.POST['CreditCard2']
            credicrad_3 = request.POST['CreditCard3']
            credicrad_4 = request.POST['CreditCard4']
                        

            if creditCardAvailabe1(credicrad_1) or creditCardAvailabe2(credicrad_2) or creditCardAvailabe3(credicrad_3) or creditCardAvailabe4(credicrad_4) :
                
                dataModel = User(userName= uname,userAge=age,userMaxPurchase= maxAmount,createDate=datetime.time(),userPhone=phoneNo,userAddress=address,pincode=pincode,usermailId=useremail,userPassword=password,creditCard_1=credicrad_1,creditCard_2=credicrad_2,creditCard_3=credicrad_3,creditCard_4=credicrad_4)
                dataModel.save()
                return redirect('/')
            else:
                return HttpResponse("MAY BE YOUR CREDIT CARD IS NOT VALID")


        elif request.POST['hiddenValue'] == "old":
            userId = request.POST['userId']
            userObj = User.objects.get(pk=userId)
            
            
            userObj.userName = request.POST['userName']
            userObj.usermailId = request.POST['useremail']
            userObj.userPassword = request.POST['password']
            userObj.userPhone = request.POST['phoneNo']
            userObj.userAge= request.POST['age']
            userObj.userMaxPurchase = request.POST['maxpurchase']
            userObj.userAddress = request.POST['address']
            userObj.userpincode= request.POST['pincode']
            userObj.crediCrad_1 = request.POST['CreditCard1']
            userObj.crediCrad_2 = request.POST['CreditCard2']
            userObj.crediCrad_3 = request.POST['CreditCard3']
            userObj.crediCrad_4 = request.POST['CreditCard4']
            
            userObj.save()
            return redirect('/')
            

    return HttpResponse("<h1>Please send Post Request")


def creditCardAvailabe1(cardnum):
    userss = User.objects.filter(creditCard_1= cardnum).values()
    
    if len(userss) == 0 :
        return True
    else:
        return False
def creditCardAvailabe2(cardnum):
    userss = User.objects.filter(creditCard_2= cardnum).values()
    
    if len(userss) == 0 :
        return True
    else:
        return False
def creditCardAvailabe3(cardnum):
    userss = User.objects.filter(creditCard_3= cardnum).values()
    
    if len(userss) == 0 :
        return True
    else:
        return False

def creditCardAvailabe4(cardnum):
    userss = User.objects.filter(creditCard_4= cardnum).values()
    
    if len(userss) == 0 :
        return True
    else:
        return False
