from django.contrib import admin
from .models import *


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    search_fields=('ism', 'id')
    list_display=("ism", "jins", "kitob_soni")
    list_display_links=('ism', 'jins')
    list_editable=('kitob_soni',)
    list_filter=('jins',)
    list_per_page=4
@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    search_fields = ('ism', 'id')
    list_display = ("ism", "tirik", "kitob_soni", "tugilgan_yil")
    list_display_links = ('ism',)
    list_editable = ('kitob_soni','tirik')
    list_filter = ('tirik',)
    list_per_page = 4


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    search_fields=('nom', 'muallif__ism', 'janr')
    list_filter=('janr',)

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    search_fields=('student__ism', 'kitob_nom')
    autocomplete_fields=('student',)
    list_filter=('qaytardi',)

