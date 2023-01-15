from django.contrib import admin


class ProjectAdmin(admin.ModelAdmin):
    pass

from django.contrib import admin

from .models import Category, Subcategory, GeneralmenuItem, Generalmenu
admin.site.register(Category)
admin.site.register(Subcategory)


class GeneralmenuItemInline(admin.TabularInline):
    model = GeneralmenuItem
    extra = 0

class GeneralmenuAdmin(admin.ModelAdmin):
    inlines = [GeneralmenuItemInline]

admin.site.register(Generalmenu, GeneralmenuAdmin)
#
class GeneralmenuItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(GeneralmenuItem, GeneralmenuItemAdmin)