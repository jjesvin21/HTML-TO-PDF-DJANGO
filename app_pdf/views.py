from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from pdf.settings import TEMPLATE_DIR
from app_pdf.utls import render_to_pdf
from django.http import HttpResponse

# Create your views here.

class PDF(APIView):

    def get(self,request):
        print(TEMPLATE_DIR)
        
        # data is consist of the key value pairs of the data to be passed to the template

        data = {"name":"Jesvin Jose"}

        #template is stored in app_pdf/templates/pdf.html
        #render_to_pdf writen in utls.py

        pdf=render_to_pdf('pdf.html',data)

        return HttpResponse(pdf, content_type='application/pdf')
