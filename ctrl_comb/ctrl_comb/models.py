from django.db import models

# Create your models here.

class Mark(models.Model):
    descript = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.descript
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Modelo(models.Model):
    descript = models.CharField(
        max_length = 50,
        db_comment = "Descripción del modelo de Vehículo"
    )

    mark = models.ForeignKey(Mark, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.mark} - {self.descript}"
    
    class Meta:
        verbose_name_plural = "Modelos"
        db_table_comment = "Modelos de Vehículos"

    
