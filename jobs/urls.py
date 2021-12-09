from django.urls import path

from jobs import views
from django.conf import settings
from django.conf.urls.static import static


app_name = "jobs"

urlpatterns = [
    path('', views.home, name= "home"),
    path('jobs/<int:job_id>', views.detail, name="detail")
]

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)