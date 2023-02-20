from django.shortcuts import render, get_object_or_404
from .models import Account

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse

from .forms import RegistrationForm
# Create your views here.
def store_view(request, category_language=None):
    categories = None
    accounts = None
    if category_language is not None:
        accounts = Account.objects.filter(languages_choice=category_language)
        paginator = Paginator(accounts, 4)
        page = request.GET.get('page')
        paged_accounts = paginator.get_page(page)
    else:
        accounts = Account.objects.filter(is_staff=True, is_active=True).exclude(is_superadmin=True)
        paginator = Paginator(accounts, 4)
        page = request.GET.get('page')
        paged_accounts = paginator.get_page(page)

    if request.GET.get("name"):
        accounts = accounts.filter(first_name__icontains=request.GET.get("name"))

    account_count = accounts.count()

    context = {
        "accounts": paged_accounts,
        "account_count": account_count,
        "search_kw": request.GET.get("name", "")

    }
    return render(request, 'store/store.html', context)


def account_detail(request,category_language, first_name):
    try:
        single_account = Account.objects.get(languages_choice=category_language, first_name = first_name)
    except Exception as e:
        raise e 
    
    context = {
        'single_account':single_account,
    }

    return render(request, 'store/account_detail.html', context)


def search(request):
    return HttpResponse('Search page')



def register(request):
    form = RegistrationForm()
    context = { 
        'form': form,

    }
    return render(request, 'accounts/register.html', context)


def login(request):
    return render(request, 'accounts/login.html')

def logout(request): 
    return



"""

from django.shortcuts import render, get_object_or_404
from .models import Account

# Create your views here.
def store_view(request, category_language=None):
    categories = None
    accounts = None
    if category_language != None:
        categories = get_object_or_404(Account, languages_choice=category_language)
        accounts = Account.objects.filter(category=categories)
        account_count = accounts.count()
    else:
        accounts = Account.objects.filter(is_staff=True,is_active=True).exclude(is_superadmin=True)
        account_count = accounts.count()
    
    context = {
        "accounts":accounts,
        "account_count":account_count,

    }
    return render(request, 'store/store.html', context)


"""


"""
def store_view(request, languages_choice=None):
    categories = None
    accounts = None
    if languages_choice != None:
        categories = get_object_or_404(Account, languages_choice=languages_choice)
        accounts = Account.objects.filter(languages_choice=languages_choice)
        account_count = accounts.count()
    else:
        accounts = Account.objects.filter(is_staff=True,is_active=True).exclude(is_superadmin=True)
        account_count = accounts.count()
    context = {
        "accounts":accounts,
        "account_count":account_count,

    }
    return render(request, 'store/store.html', context)  
    
    """