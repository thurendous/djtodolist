from django.contrib import admin
from .models import MyToDoList

# Register your models here.
# admin.site.register(MyToDoList) #追加
@admin.register(MyToDoList)
class MyToDoListAdmin(admin.ModelAdmin):

    list_display = ['title', "entryDate","deadline","done"]