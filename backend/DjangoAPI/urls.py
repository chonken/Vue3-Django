from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('CRUD/', include('CRUD.urls')),
    path('CheckKPI/', include('CheckKPI.urls')),
]
