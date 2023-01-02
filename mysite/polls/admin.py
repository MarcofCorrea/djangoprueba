from django.contrib import admin
from .models import Question

#agrega opciones a la pagina de admin
admin.site.register(Question)

# Register your models here.
