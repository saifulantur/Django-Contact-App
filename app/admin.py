from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'info', 'email', 'phone')
    list_editable = ('info',)
    list_per_page = 10
    search_fields = ('name', 'gender', 'email', 'phone')
    list_filter = ('gender', 'date_added')    

admin.site.register(Contact, ContactAdmin)
admin.site.unregister(Group)