from django.shortcuts import render
from projects.models import Project
from django.views.generic import DetailView, ListView


class ListProjectView(ListView):
    model = Project
    template_name: str = 'project_index.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = "project_detail.html"
    pk_url_kwarg: str = 'pk'
