from django.views.generic import TemplateView

class HomeView(TemplateView):
	template_name = "homepage.html"

class AboutView(TemplateView):
	template_name = "about.html"
