from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return super().__str__()

class Produto(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True
        )
    descricao = models.TextField(blank=True)

    categoria = models.ForeignKey(
        Categoria,
        on_delete=PROTECT,
        related_name="produtos"
    )

    precoCusto = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    precoVenda = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estoque = models.PositiveIntegerField(default=0)
    estoqueMinimo = models.PositiveIntegerField(default=0)
    
    ativo = models.BooleanField(default=True)

    def __str__(self):  
        return super().__str__()