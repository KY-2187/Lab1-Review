from django.shortcuts import render
from django.views.generic.base import TemplateView


class HeroesView(TemplateView):
	template_name = 'heroes.html'

class JesterView(TemplateView):
	template_name = 'detail_jester.html'

