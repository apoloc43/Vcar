from django.db import models

# Create your models here.

class Cliente(models.Model):

    nome = models.CharField("Nome", max_length=250)
    email = models.EmailField("Email")
    cpf = models.CharField("CPF", max_length=15)
    data_nascimento = models.DateField("Data de nascimento")

    def __str__(self):
        return "{}".format(self.nome)
    
    class Meta:
        verbose_name_plural = "Clientes"

class Carro(models.Model):

    placa = models.CharField("Placa", max_length=100)
    marca = models.CharField("Marca", max_length=100)
    modelo = models.CharField("Modelo", max_length=100)
    comprar = models.DateField("Data de compra")
    ano = models.CharField('Ano', max_length=10)

    def __str__(self):
        return "{} - {}".format(self.marca, self.modelo)

    class Meta:
        verbose_name = "carro"
        verbose_name_plural = "carros"

class Aluguel(models.Model):

    codigo = models.CharField("Codigo", max_length=100)
    data_aluguel = models.DateField("Data de aluguel")
    data_devolucao = models.DateField("Data de devolução")
    valor = models.DecimalField("Valor", max_digits=15, decimal_places=2)
    devolucao = models.BooleanField("Devolvido")
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING, related_name='cliente_alugueis', verbose_name="Cliente")
    carro = models.ForeignKey(Carro, on_delete=models.DO_NOTHING, related_name='carro_alugueis', verbose_name="carros") 

    def __str__(self):
        return "{} - {} - {}".format(self.codigo, self.cliente.nome, self.carro.modelo)

    class Meta:
        verbose_name = "Aluguel"
        verbose_name_plural = "Alugueis"
