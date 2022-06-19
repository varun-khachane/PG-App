from django.contrib import admin

# Register your models here.
from pgapp.models import Tenants

class TenantsAdmin (admin.ModelAdmin):
    list_display = ("name","rent","from_date")
    

admin.site.register(Tenants,TenantsAdmin)