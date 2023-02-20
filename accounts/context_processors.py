from .models import Account

def menu_links(request):
    links = Account.LANGUAGE_CHOICE
    return dict(links=links)