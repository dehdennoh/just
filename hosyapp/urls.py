
from django.contrib import admin
from django.urls import path
from hosyapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inner/', views.inner, name='inner'),
    path('', views.index, name='index'),
]
