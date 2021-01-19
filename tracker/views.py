from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Club



class ClubChartView(TemplateView):
	templates_name='clubs/chart.js'
	def get_context_data(self,**kwargs):
		context=super().get_context_data(**kwargs)
		context['qs']=Club.objects.all()
		return context