from django.contrib import admin

# Register your models here.
from .models import Users , Location

class UsersAdmin(admin.ModelAdmin):
	list_display = ("name","location" , "price" , "updated")
	list_filter = ("status","updated" )
	#search_fields = ("name")

admin.site.register(Location);


admin.site.register(Users , UsersAdmin);

