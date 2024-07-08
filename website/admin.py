from django.contrib import admin
from website.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date',)
    list_filter = ('email',)

admin.site.register(Contact, ContactAdmin)
