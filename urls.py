from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="homes"),
    path('list/',views.list,name="list"),
    path('otp/',views.verify,name="verifyotp"),
]