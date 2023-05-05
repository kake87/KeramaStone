from django.contrib import admin
from .models import Travertin, Granit, Mramor, Request


class AdminProduct(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)
    ordering = ('name', )


admin.site.register(Travertin)
admin.site.register(Granit)
admin.site.register(Mramor)
admin.site.register(Request)
# Register your models here.
