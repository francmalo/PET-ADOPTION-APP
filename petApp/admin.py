from django.contrib import admin
from .models import Vaccines,Pet

# Register your models here.
admin.site.register(Vaccines)
#admin.site.register(Pet)

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display=(
        'name','gender','submitted_on','species','owner','age'
    )
    