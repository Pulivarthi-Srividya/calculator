from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.loginpage,name='login'),
    path('register/',views.registerpage,name='register'),
    path('home/',views.home,name='home'),
    path('calculator/',views.calculator,name='calculator'),
    path('result/<str:result>/',views.result,name='result'),
    path('logout/',views.logoutpage,name='logout')
    
]
