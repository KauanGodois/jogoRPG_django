from django.db import models
from django.conf import settings

class ClassePersonagem(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    habilidade_especial = models.CharField(max_length=255)
    vida = models.IntegerField(default=100)
    dano = models.IntegerField(default=10)
    armadura = models.IntegerField(default=5)
    experiencia = models.IntegerField(default=0)
    nivel = models.IntegerField(default=1)
    imagem_url = models.ImageField(upload_to='imagens/classe/', blank=True)

    def __str__(self):
        return self.nome

class Jogador(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)  
    classe = models.ForeignKey(ClassePersonagem, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome


class Inimigo(models.Model):
    nome = models.CharField(max_length=255)
    vida = models.IntegerField()
    dano = models.IntegerField()
    armadura = models.IntegerField()
    descricao = models.TextField()
    recompensas_ouro = models.IntegerField(default=0)
    recompensas_exp = models.IntegerField(default=0)
    nivel = models.IntegerField(default=1)
    imagem_url = models.URLField(blank=True)

    def __str__(self):
        return self.nome


class Combate(models.Model):
    jogador = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='combates')
    inimigo = models.ForeignKey(Inimigo, on_delete=models.CASCADE, related_name='combates')
    data = models.DateTimeField(auto_now_add=True)
    resultado = models.CharField(max_length=10, choices=(('venceu', 'Venceu'), ('perdeu', 'Perdeu')))

    def __str__(self):
        return f"{self.jogador.username} {self.resultado} contra {self.inimigo.nome} em {self.data.strftime('%d/%m/%Y')}"


class Item(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    efeito = models.CharField(max_length=255)
    imagem_url = models.URLField(blank=True)

    def __str__(self):
        return f"{self.nome} ({self.efeito})"