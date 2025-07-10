from django.contrib import admin

# Register your models here.
from .models import Menu, Servicos, Reserva, Sub

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['prato','valor', 'ativo']

@admin.register(Servicos)
class ServicosAdmin(admin.ModelAdmin):
    list_display = ['servico', 'ativo']

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefone', 'date', 'time']

@admin.register(Sub)
class SubAdmin(admin.ModelAdmin):
    list_display = ['email', 'ativo']
