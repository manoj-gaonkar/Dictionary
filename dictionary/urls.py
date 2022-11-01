
from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('word',views.meaning,name="meaning"),
]
