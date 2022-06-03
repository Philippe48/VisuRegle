from .import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.listeAbonne),
    path('regle/<str:pk>', views.listeRegleAbonne, name="regle"),

]
