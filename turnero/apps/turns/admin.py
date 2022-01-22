from django.contrib import admin

# Register your models here.
from apps.turns.models import estados,turnos

class estadosAdmin(admin.ModelAdmin):
    pass
admin.site.register(estados, estadosAdmin)

class turnosAdmin(admin.ModelAdmin):
    pass
admin.site.register(turnos, turnosAdmin)