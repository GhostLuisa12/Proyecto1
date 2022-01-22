from django.contrib import admin

# Register your models here.
from apps.users.models import persona, staffCheck

class personaAdmin(admin.ModelAdmin):
    pass
admin.site.register(persona, personaAdmin)

class staffAdmin(admin.ModelAdmin):
    pass
admin.site.register(staffCheck, staffAdmin)