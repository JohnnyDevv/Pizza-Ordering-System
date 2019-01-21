from django.urls import path
from . import views

app_name = 'pizzas'

urlpatterns = [
	path('', views.PizzaListView.as_view(), name='list'),
]
