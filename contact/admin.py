from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','phone','email')
    list_filter = ('created_date',)
    search_fields = ('first_name','last_name','phone','email')
    list_per_page = 1
    list_max_show_all = 100
    list_display_links = ('id',)



