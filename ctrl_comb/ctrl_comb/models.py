from django.db import models
from django.urls import reverse
from bases.models import ClassModelo

# Create your models here.

class Mark(ClassModelo):
    descript = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.descript
    
    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

class Modelo(ClassModelo):
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
        permissions = [
            ("permiso_especial","Puede Leer y Editar Modelos"),
        ]

class Vehiculo(ClassModelo):
    modelo = models.ForeignKey(Modelo, on_delete=models.RESTRICT)
    register = models.CharField(
        max_length=50,
        db_column="Matrícula Vehículo",
        help_text="Matrícula Vehículo")
    
    year = models.PositiveSmallIntegerField(help_text="Año del Vehículo")

    def __str__(self):
        return self.register
    
    def get_absolute_url(self):
        return reverse("vehiculo_edit",kwargs={'pk':self.pk}
                       )
    class Meta:
        verbose_name_plural="Vehículos"
        db_table_comment="Vehículos"


    
