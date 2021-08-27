from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('', index, name='index'),
    path(
        'delete/<int:document_id>/',
        views.document_delete,
        name='document_delete'
    ),
]
