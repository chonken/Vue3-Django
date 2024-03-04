from django.urls import path
from . import views

urlpatterns=[
    path('<str:model_name>', views.model_api, name='model-api'),
    path('<str:model_name>/<str:id>', views.model_api, name='model-api-id'),
]