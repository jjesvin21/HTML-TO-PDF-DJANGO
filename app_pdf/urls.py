from django.urls import path
from app_pdf.views import PDF

urlpatterns = [
    path("",PDF.as_view())
]
