from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('home.urls')),
	path('products/', include('products.urls')),
    path('admin/', admin.site.urls),
    path('accounts/register/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
