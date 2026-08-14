from django.db import models
from usuarios.models import Usuario

class Caixa(models.Model):
    STATUS_CHOICES=[
        ('ABERTO', 'aberto'),
        ('FECHADO', 'fechado')
    ]

    usuarioAbertura = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='caixa_abertos'
    )
    usuarioFechamento = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name='caixa_fechados',
        blank=True,
        null=True
    )

    dataAbertura = models.DateTimeField(
        auto_now_add=True
    )
    dataFechamento = models.DateTimeField(
        blank=True,
        null=True
    )

    valorInicial = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    valorFinal = models.DecimalField(
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

    formaPagamento = models.CharField(
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