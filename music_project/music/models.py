from django.db import models

class Musico(models.Model):
	nome = models.CharField(max_length=100)
	
	def __str__(self):
		return self.nome

class EstiloMusical(models.Model):
	nome = models.CharField(max_length=100)

	def __str__(self):
		return self.nome

class Banda(models.Model):
	estilo = models.ForeignKey(EstiloMusical, on_delete=models.CASCADE)
	nome = models.CharField(max_length=100)
	data_criacao = models.DateField()
	ativa = models.BooleanField(default=True)
	numero_ouvintes_mensais_spotify = models.IntegerField()
	musicos = models.ManyToManyField(Musico)

	def __str__(self):
		return self.nome + " fundada em: " + str(self.data_criacao) + "\n Numero de ouvintes mensais no spotify: " + str(self.numero_ouvintes_mensais_spotify)
