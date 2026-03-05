
from django.urls import path
from . import views

urlpatterns = [
    path('',views.all_biryani,name='all_biryani'),
    path('<int:biryani_id>/', views.biryani_detail, name='biryani_detail'),
    path('biryani_stores/', views.biryani_stores_view, name='biryani_stores')
]
