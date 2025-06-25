from django.contrib import admin
from .models import Module, Section, SectionImage

# Register your models here.

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ("name",)

class SectionImageInline(admin.TabularInline):
    model = SectionImage
    extra = 1

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "module")
    list_filter = ("module",)
    inlines = [SectionImageInline]
