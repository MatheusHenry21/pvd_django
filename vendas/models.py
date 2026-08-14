from django.db import models
from usuarios.models import Usuario
from produtos.models import Produto

class Venda(models.Model):
    STATUS_CHOICES=[
        ('ABERTA', 'aberta'),
        ('FINALIZADA', 'finalizada'),
        ('CANCELADA', 'cancelada')
    ]

    usuario = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT
    )

    data = models.DateField(auto_now_add=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ABERTA"
    )

    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return super().__str__()

class ItemVenda(models.Model):
    venda = models.ForeignKey(
        Venda,
        on_delete=models.CASCADE,
        related_name='itens'
    )

    produto = models.ForeignKey(
        Produto,
        on_delete=models.PROTECT,

    )

    quantidade = models.PositiveIntegerField()

    preco_unitario = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )

    sub_preco = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.produto.nome} - Venda #{self.venda.id}'