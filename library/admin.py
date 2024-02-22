from django.contrib import admin
from .models import Libro
# Register your models here.

# Este espacio es para que el administrador manipule información
admin.site.register(Libro)
#admin.site.register(Prestamos)