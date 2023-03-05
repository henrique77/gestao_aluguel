from django.db import models

# Create your models here.
class Edificio(models.Model):
    edificio_name = models.CharField(max_length=100)

    class Meta:
        db_table = "tbledificio"

class Apartamento(models.Model):
    ap_name = models.CharField(max_length=100)
    ap_status = models.IntegerField()
    edificio_id = models.IntegerField()
    valor_aluguel = models.FloatField()
    locatario_nome = models.CharField(max_length=100)
    locatario_contato = models.CharField(max_length=15)

    class Meta:
        db_table = "tblapartamento"