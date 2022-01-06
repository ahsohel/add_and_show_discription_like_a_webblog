
from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('Entry_on_table', views.Entry_on_table, name='Entry_on_table'),
    path('save', views.save, name='save'),
    path('details_page/<int:pk>', views.details_page, name='details_page'),
    path('see_details_monna', views.see_details_monna, name='see_details_monna'),
]
