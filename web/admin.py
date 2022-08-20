from django.contrib import admin
from .models import Roman
# Register your models here.
class RomanAdmin(admin.ModelAdmin):
	list_display = ('user', 'title')
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title', 'body')
admin.site.register(Roman, RomanAdmin)