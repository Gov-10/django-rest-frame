from django.urls import path
from . import views
urlpatterns = [
    path('advocate_detail/<str:username>/', views.advocate_detail, name='advocate_detail'),
    path('advocate_list/', views.advocate_list, name='advocate_list'),
]
