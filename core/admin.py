from django.contrib import admin
from .models import Module, Section

# Register your models here.

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "module")
    list_filter = ("module",)
