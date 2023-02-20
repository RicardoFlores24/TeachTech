#projecest view

from django.shortcuts import render
from accounts.models import Account

def home(request):
    accounts = Account.objects.filter(is_staff=True,is_active=True).exclude(is_superadmin=True)
    context = {
        "accounts":accounts
    }
    return render(request, 'home.html',context=context)

