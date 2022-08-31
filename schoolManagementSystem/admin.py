from django.contrib import admin
from .models import Student,Trainer




class StudentAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","surname",)
    search_fields = ("first_name","last_name")

admin.site.register(Student)
admin.site.register(Trainer)


    



