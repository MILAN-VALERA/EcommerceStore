from django.shortcuts import render
from ..user.models import User

# Create your views here.
def dashboard(request,Id):
    user_dash = User.objects.filter(userId=Id).values()[0]
    
    win  = {'win':user_dash}
    return render(request,'dashboard.html',win)