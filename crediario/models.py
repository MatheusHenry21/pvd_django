from django.db import models

class Cliente(models.Model):
    nome = models.CharField(
        max_length=150
    )

    cpf = models.CharField(
        max_length=14,
        unique=True
    )

    telefone = models.CharField(
        max_length=20,
        blank=True
    )

    limite_crediario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    ativo = models.BooleanField(
        default=True
    )

    def __str__(self):
        return f'{self.nome}'

class Credito(models.Model):
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name='creditos'
    )

    valor_total = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    data = models.DateTimeField(
        auto_now_add=True
    )

    observacao = models.CharField(
        max_length=50,
        blank=True
    )

    def __str__(self):
        return f'{self.cliente} - R% {self.valorTotal}'

class Parcela(models.Model):
    credito = models.ForeignKey(
        Credito,
        on_delete=models.PROTECT,
        related_name='parcelas'
    )

    numero = models.PositiveBigIntegerField()

    valor = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    data_vencimento = models.DateField()

    data_pagamento = models.DateField(
        blank=True,
        null=True
    )

    paga = models.BooleanField(
        default=False
    )

    def __str__(self):
        return f'Parcela {self.numero} - {self.credito.cliente.nome}'