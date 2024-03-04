from django.urls import path
from . import views

urlpatterns=[
    path('<str:type>', views.check_api, name='check-api'),
    path('<str:type>/<str:id>', views.check_api, name='check-api-id'),
]