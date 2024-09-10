from django.urls import path
from .views import AdmissionListCreateView

urlpatterns = [
    path('admissions/', AdmissionListCreateView.as_view(),
         name='admission-list-create'),
]
