from django.contrib import admin
from restaurants.models import Restaurant,Food,Comment
# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
	list_display = ('name' , 'phone_number' , 'address')
	list_filter = ('open_date',)
	search_fields = ('name',)

class FoodAdmin(admin.ModelAdmin):
	list_display = ('name' , 'restaurant' , 'price')
	list_filter = ('is_spicy',)
	ordering = ('-price',)
	fields =('price','restaurant')





admin.site.register(Restaurant,RestaurantAdmin)
admin.site.register(Food,FoodAdmin)
admin.site.register(Comment)
