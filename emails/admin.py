from django.contrib import admin
from .models import EmailSource
from django.contrib import admin
from django import forms



class EmailSourceAdmin(admin.ModelAdmin):
	# fieldsets = [
	# 	('predmet', {'fields': [ 'subject']}),
	# 	(None,      {'fields': [ 'template']}),
	# ]
	list_display = ( 'subject', 'user',)

admin.site.register(EmailSource, EmailSourceAdmin)
