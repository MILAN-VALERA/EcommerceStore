from django.shortcuts import render
from aps.user.models import User
from aps.product.models import Product
from aps.order.models import Order
from aps.orderDetail.models import OrderDetail
from django.core.mail import send_mail

from django.http import JsonResponse,HttpResponse
# Create your views here.

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def orderValidate(request):
    
    if request.method == "POST":
        uid = request.POST["uid"]
        pid = request.POST["pid"]
        cnum= request.POST["cnum"]
        
        userData = User.objects.filter(userId=uid).values().first()
        
        productData = Product.objects.filter(productId =pid).values().first()
        
        if str(userData['totalOrderPlaced']) == '0':
            if cardChecker(userData,cnum):
                if CheckAmount(userData,productData):
                    if float(productData['productPrice']) > 500:
                        mess = "Your order has been placed of price " +  productData['productPrice']
                        mail_system(userData,"Order Placed", mess)
                    updateOrderModel(uid,pid,productData["productPrice"])
                    return JsonResponse({"error":"","productData":productData})
                else:
                    if float(productData['productPrice']) > 500:
                        mess = "System has detected over purchasing from your creditcard " + cnum
                        mail_system2(cnum,"Fraud detect",mess)
                    return JsonResponse({"error":"May be you are over purchasing "})
            else:
                mess = "May be your card "+  cnum +" is used by unauthorised person"
                mail_system2(cnum,"Some use card",mess)
                return JsonResponse({"error":"your Card is not matching with your profile"})
        else:
            
            orderData  = Order.objects.filter(userId = uid).values()
            newOrder = True
            orderAmountList = []
            if cardChecker(userData,cnum):
                
                for ordr in orderData:
                    ordrDetailsData = OrderDetail.objects.filter(orderDetailId=ordr['orderId']).values()
                    for ordrDet in ordrDetailsData:
                        
                        orderAmountList.append(float(ordrDet['orderAmount']))                        
                        if int(ordrDet['productId_id']) == int(pid):
                            if str(ordrDet['orderAmount']) == str(productData['productPrice']):
                                updateOrderModel(uid,pid,productData['productPrice'])
                                newOrder = False

                                if float(productData['productPrice']) > 500:
                                    mess = "Your order has been placed of price " +  productData['productPrice']
                                    mail_system(userData,"Order Placed", mess)
                                return JsonResponse({"error":"", "productData":productData})
                            elif CheckAmount(userData,productData):
                                if float(productData['productPrice']) > 500:
                                    mess = "Your order has been placed of price " +  productData['productPrice']
                                    mail_system(userData,"Order Placed", mess)
                                return JsonResponse({"error":"","productData":productData})
                if newOrder:
                    if CheckAmount(userData,productData):
                        if float(productData['productPrice']) > 500:
                                mess = "Your order has been placed of price " +  productData['productPrice']
                                mail_system(userData,"Order Placed", mess)
                        updateOrderModel(uid,pid,productData['productPrice'])
                        return JsonResponse({"error":"","productData":productData})
                    else:
                        if float(productData['productPrice']) > 500:
                            mess = "System has detected over purchasing from your creditcard " + cnum
                            mail_system2(cnum,"Fraud detect",mess)
                        return JsonResponse({"error":"You are over purchasing"})
                else:
                    return JsonResponse({"error":"i think add more detail"})

            else:
                mess = "May be your card "+  cnum +" is used by unauthorised person"
                mail_system2(cnum,"Someone use your card",mess)
                return JsonResponse({"error":"You not using valid card"})
                

    return JsonResponse({'error':"You have entered wrong site"})



def cardChecker(userCard,inputCard):
    if userCard['creditCard_1'] == inputCard or userCard['creditCard_2'] == inputCard or userCard['creditCard_3'] == inputCard or userCard['creditCard_4'] == inputCard:
        return True
    else:
        return False  


def CheckAmount(userData,productData):
    maxAmnt = float(userData['userMaxPurchase'])
    price  = float(productData['productPrice'])
    
    CmpAmount1 = maxAmnt + (maxAmnt * (25/100))
    
    if(CmpAmount1 >= price and 0 <= price ):
        return True
    else:
        return False

    
def updateOrderModel(uid,pid,orderAmount):
    
    productObject = Product.objects.get(pk=pid)
    userss = User.objects.get(pk=uid)
    userss.totalOrderPlaced = int(userss.totalOrderPlaced) + 1
    userss.save()
                   
    orderObect = Order(userId=userss)
    orderObect.save()
    OrderDetailObject = OrderDetail(orderId=orderObect,productId=productObject,orderAmount=orderAmount,orderShipAdd=userss.userAddress,quantity=1)
    OrderDetailObject.save()
   



def mail_system(userData,sub,mess):
    user_mail = userData['usermailId']
    recipt = []
    recipt.append(user_mail)
    send_mail(
        subject=sub,
        message=mess,
        from_email="ng458641@gmail.com",
        recipient_list=recipt,
        auth_user="ng458641@gmail.com",
        auth_password="naresh@#123"
    )


def mail_system2(cnum,sub,mess):
    
    x = User.objects.filter(creditCard_1=cnum).values()
    
    if len(x)==0:
        x = User.objects.filter(creditCard_2=cnum).values()
    
    if len(x) ==0:
        x = User.objects.filter(creditCard_3=cnum).values()
    if len(x) == 0:
        x = User.objects.filter(creditCard_4=cnum).values()
    
    user_mail = x[0]['usermailId']
    recipt = []
    recipt.append(user_mail)
    send_mail(
        subject=sub,
        message=mess,
        from_email="ng458641@gmail.com",
        recipient_list=recipt,
        auth_user="ng458641@gmail.com",
        auth_password="naresh@#123"
    )