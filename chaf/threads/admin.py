from django.contrib import admin
from chaf.threads.models import BirthRegistration, MarriageRegistration

# Register your models here.

class BirthAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'index_child_surname', 'index_child_firstname', 'index_registration_place', 'index_year')
	list_filter = ('index_year', 'index_registration_place',)
	search_fields = ('index_child_surname', 'index_child_firstname')

class MarriageAdmin(admin.ModelAdmin):
	list_display = ('__unicode__', 'index_spouse1_surname', 'index_spouse1_firstname', 'index_spouse2_surname', 'index_spouse2_firstname', 'index_registration_place', 'index_year')
	list_filter = ('index_year', 'index_registration_place',)
	search_fields = ('index_spouse1_surname', 'index_spouse1_firstname', 'index_spouse2_surname', 'index_spouse2_firstname')

admin.site.register(BirthRegistration, BirthAdmin)
admin.site.register(MarriageRegistration, MarriageAdmin)