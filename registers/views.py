from pipes import Template
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import TemplateView
# Create your views here.

class HomeView(LoginRequiredMixin,TemplateView):
    template_name = 'registers/home.html'
    login_url = '/login'