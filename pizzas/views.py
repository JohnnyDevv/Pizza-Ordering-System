from django.shortcuts import render
from django.views.generic import ListView
from .models import Pizza

class PizzaListView(ListView):
	template_name = 'pizza_list.html'
	context_object_name = 'pizzas'

	def get_queryset(self):
		return Pizza.objects.all().order_by('-date')