from django.db import models
from usuarios.models import Usuario

class Caixa(models.Model):
    STATUS_CHOICES=[
        ('ABERTO', 'aberto'),
        ('FECHADO', 'fechado')
    ]

    usuario_abertura = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='caixa_abertos'
    )
    usuario_fechamento = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='caixa_fechados',
        blank=True,
        null=True
    )

    data_abertura = models.DateTimeField(
        auto_now_add=True
    )
    data_fechamento = models.DateTimeField(
        blank=True,
        null=True
    )

    valor_inicial = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    valor_final = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='ABERTO'
    )

    def __str__(self):
        return f'Caixa #{self.id} - {self.status}'

class MovimentoCaixa(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'entrada'),
        ('SAIDA', 'saida')
    ]

    FORMA_PAGAMENTO_CHOICES = [
        ('DINHEIRO', 'dinheiro'),
        ('PIX', 'pix'),
        ('CARTAO', 'cartao'),
        ('OUTRO', 'outro')
    ]

    caixa = models.ForeignKey(
        Caixa,
        on_delete=models.CASCADE,
        related_name='caixas'
    )

    tipo = models.CharField(
        max_length=10,
        choices=TIPO_CHOICES
    )

    forma_pagamento = models.CharField(
        max_length=10,
        choices=FORMA_PAGAMENTO_CHOICES
    )

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    descricao = models.CharField(
        max_length=255,
        blank=True
    )

    data = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f'{self.tipo} - R$ {self.valor}'