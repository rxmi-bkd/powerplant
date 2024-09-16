from django.urls import path
from powerplant import views

urlpatterns = [
    path('productionplan/', views.get_production_plan),
]