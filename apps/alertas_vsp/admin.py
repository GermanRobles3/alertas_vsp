from django.contrib import admin
from .models import Brote, Evento, Medio, Alerta

# Register your models here.


admin.site.register(Brote)
admin.site.register(Evento)
admin.site.register(Medio)
admin.site.register(Alerta)