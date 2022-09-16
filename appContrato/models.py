from django.db import models

# Create your models here.

class tipo_persona(models.Model):
    tipo_persona_id=models.BigAutoField(primary_key=True)
    descripcion=models.CharField(max_length=30)
    estado=models.BooleanField()


class persona(models.Model):
    persona_id=models.BigAutoField(primary_key=True)
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    alias=models.CharField(max_length=20)
    sexo=models.CharField(max_length=1)
    fecha_nacimiento=models.DateField()
    pais_id=models.ForeignKey("appCompeticion.pais",on_delete=models.CASCADE)
    estatura=models.FloatField()
    peso=models.FloatField()
    estado=models.BooleanField()
    tipo_persona_id=models.ForeignKey(tipo_persona,on_delete=models.CASCADE)
    