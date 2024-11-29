from django.contrib import admin
from .models import Articulo, Comentario

class ComentarioEnLinea(admin.TabularInline):
  model = Comentario
  extra = 0
  
class ArticuloEnLinea(admin.ModelAdmin):
  inlines = [
    ComentarioEnLinea,
  ]

# Register your models here.
admin.site.register(Articulo, ArticuloEnLinea)
admin.site.register(Comentario)