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
        on_delete=models.PROTECT,
        related_name="produtos"
    )

    preco_custo = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    preco_venda = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    estoque = models.PositiveIntegerField(default=0)
    estoque_minimo = models.PositiveIntegerField(default=0)
    
    ativo = models.BooleanField(default=True)

    def __str__(self):  
        return super().__str__()