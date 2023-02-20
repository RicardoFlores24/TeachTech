from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static 
from accounts import views

urlpatterns = [
    path('', views.store_view, name='all_topics'),
    path('<slug:category_language>/', views.store_view, name='accounts_by_category'),
    path('<slug:category_language>/<str:first_name>/', views.account_detail, name='account_detail'),
    path('search/', views.search, name='search')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)