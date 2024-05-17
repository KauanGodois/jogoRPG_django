from django.contrib import admin
from .models import ClassePersonagem, Jogador, Inimigo, Item

@admin.register(ClassePersonagem)
class ClassePersonagemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao', 'vida', 'dano', 'armadura', 'experiencia', 'nivel', 'habilidade_especial')

@admin.register(Jogador)
class JogadorAdmin(admin.ModelAdmin):
    list_display = ('user', 'classe')

@admin.register(Inimigo)
class InimigoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vida', 'dano', 'armadura', 'recompensas_ouro', 'recompensas_exp')
    search_fields = ('nome',)
    list_per_page = 5

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'efeito', 'descricao')
    search_fields = ('nome', 'efeito')
    list_per_page = 5