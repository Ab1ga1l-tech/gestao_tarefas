from django.db import models
from django.contrib.auth.models import User

class Tarefa(models.Model):
    PRIORIDADES = [
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)  # Relacionamento com usuário
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True, null=True)
    concluida = models.BooleanField(default=False)
    prioridade = models.CharField(max_length=1, choices=PRIORIDADES, default='M')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_vencimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo

