from django.db import models



class ModelBase(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Cliente(ModelBase):
    cliente_id = models.AutoField(primary_key=True)
    CPF = models.CharField(max_length=11, unique=True)
    Nome = models.CharField(max_length=100)

    def __str__(self):
        return self.Nome

class Filme(ModelBase):
    filme_id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=200)
    Duracao = models.PositiveIntegerField()
    sessao_id = models.IntegerField()

    def __str__(self):
        return self.Titulo

class Checkout(ModelBase):
    checkout_id = models.AutoField(primary_key=True)
    Valor = models.DecimalField(max_digits=6, decimal_places=2)
    filme_id = models.ForeignKey(Filme, on_delete=models.CASCADE)
    sessao_id = models.IntegerField()

    def __str__(self):
        return f"Checkout {self.checkout_id}"

class Checkout_Filme(ModelBase):
    checkout_filme_id = models.AutoField(primary_key=True)
    Data = models.DateField()
    Horario = models.TimeField()
    filme_id = models.ForeignKey(Filme, on_delete=models.CASCADE)
    checkout_id = models.ForeignKey(Checkout, on_delete=models.CASCADE)

    def __str__(self):
        return f"Filme {self.filme_id} em {self.Data} às {self.Horario}"

class Ingresso(ModelBase):
    ingresso_id = models.AutoField(primary_key=True)
    cliente_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    filme_id = models.ForeignKey(Filme, on_delete=models.CASCADE)
    sessao_id = models.IntegerField()
    checkout_id = models.ForeignKey(Checkout, on_delete=models.CASCADE)

    def __str__(self):
        return f"Ingresso {self.ingresso_id} - Cliente {self.cliente_id}"


class Cliente(ModelBase):
    cliente_id = models.AutoField(primary_key=True)
    CPF = models.CharField(max_length=11, unique=True)
    Nome = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.Nome} ({self.CPF})"
class Filme(ModelBase):
    filme_id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=200)
    Duracao = models.PositiveIntegerField()
    sessao_id = models.IntegerField()  # ou models.ForeignKey(Sessao, ...)

    def __str__(self):
        return self.Titulo
class Filme(ModelBase):
    filme_id = models.AutoField(primary_key=True)
    Titulo = models.CharField(max_length=200)
    Duracao = models.PositiveIntegerField()
    sessao_id = models.IntegerField()  # ou models.ForeignKey(Sessao, ...)

    def __str__(self):
        return self.Titulo
