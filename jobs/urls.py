from django.urls import path

from jobs import views


app_name = "jobs"

urlpatterns = [
    path('', views.HomeView.as_view(), name= "home")
]