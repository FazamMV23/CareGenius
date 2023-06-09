from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home.as_view(), name="Home"),
    path('dashboard/', views.Dashboard.as_view(), name="Dashboard"),
    path('record/', views.Record.as_view(), name="Record"),
    path('record/1/', views.RecordView.as_view(), name="RecordView"),
    path('about/', views.About.as_view(), name="About"),

]
