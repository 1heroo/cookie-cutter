from django.urls import path
from .views import (ListProjectView, ProjectDetailView)


urlpatterns = [
    path("", ListProjectView.as_view(), name="project_index"),
    path("<int:pk>/", ProjectDetailView.as_view(), name="project_detail"),
]