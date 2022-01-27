from django.urls import path
from . import views

urlpatterns =[
    path('', views.index_dept1),
    path('dept2/<str:head_num>/', views.index_dept2),
    path('<int:team_num_id>/', views.index_dept3)
]