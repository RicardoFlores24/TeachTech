
from django.contrib import admin
from django.urls import path, include
from .import views
from django.conf.urls.static import static 
from django.conf import settings 
from accounts.views import account_detail,store_view

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.home, name='home'),
#     path('store/', include('accounts.urls')),
#     path('cart/', include('carts.urls')),
#     path('category/<slug:category_language>/', store_view, name='accounts_by_category'),
#     path('category/<slug:category_language>/<str:first_name>/', account_detail, name='account_detail'),
#     path('accounts/', include('accounts.urls')),
# ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('store/', include('accounts.urls')),
    path('cart/', include('carts.urls')),
    path('category/', include('category.urls')),
    path('accounts/', include('accounts.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)