"""Kutubxona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginView),
    path('husan/',husan ),

    path('student/',student ),


    path('bitiruvchi/',bitiruvchi ),
    path('kitob/',kitob ),
    path('talaba/<int:son>/', talaba ),
    path('talaba_ochir/<int:son>/', talaba_ochir ),
    path('books/', books),
    path('kitob1/<int:son>/', kitob1),
    path('talaba_edit/<int:son>/', student_tahrirlash),
    path('talaba_tas/<int:son>/', talaba_tasdiqlash),

    path('mualliflar/', mualliflar),
    path('Muallif/<int:son>/', muallif_delete),
    path('delete_m/<int:son>/', delete_m),

    path('muallif/<int:son>/', muallif),
    path('muallif_t/<int:son>/', muallif_t),

    path('recordlar/', recordlar),
    path('rdelete/<int:son>/', rdelete),
    path('delete_r/<int:son>/', delete_r),
    path('tirik/', tirik),
    path('katta/', katta_kitob),
    path('kop/', kitobi_kop),
    path('last/', last_record),
    path('mk/',mk ),
    path('badiiy/',badiiy ),
    path('isma/',isma ),
    path('tyil/',tyil ),
    path('km/',km),
    path('erkak/',erkak),
    path('rid/<int:son>/',rid),
    path('bitir/',bitir),
    path('record_t/<int:son>/',record_t),
    path('book/<int:son>/',book_delete),
    path('delete_k/<int:son>/',delete_k),
    path('bosh/', bosh),
    path('logout/', logoutView),
    path('register/', register)

]
