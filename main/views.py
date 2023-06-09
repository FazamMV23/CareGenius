from django.shortcuts import render,redirect
from django.views import View
# import time
# Create your views here.
class Home(View):
    def get(self,request):

        context = {}
        return render(request, 'main/index.html')

    def post(self,request):
        return render(request, 'main/index.html')

class Dashboard(View):
    def get(self,request):

        context = {}

        return render(request, 'main/dashboard.html')

    def post(self,request):
        return render(request, 'main/dashboard.html')

class Record(View):
    def get(self,request):

        context = {}

        return render(request, 'main/record.html')

    def post(self,request):
        return render(request, 'main/record.html')

class RecordView(View):
    def get(self,request):

        context = {}

        return render(request, 'main/record-view.html')

    def post(self,request):
        return render(request, 'main/record-view.html')

class About(View):
    def get(self,request):

        context = {}

        return render(request, 'main/about.html')

    def post(self,request):
        return render(request, 'main/about.html')

