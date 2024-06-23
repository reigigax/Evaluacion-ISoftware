from django.db import models

# Create your models here.

# Tabla Empresa
class Empresa(models.Model):
    #Id (autoincrementable), Nombre Empresa
    id_empresa = models.AutoField(db_column='id_empresa', primary_key=True)
    nombre_empresa = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return str(self.nombre_empresa)
    

# Tabla Usuario 
class Usuario(models.Model):
    #Rut, Nombre, Empresa asociada, Correo, Fecha de Nacimiento, Telefono y Direccion
    rut = models.CharField(primary_key=True,max_length=10)
    nombre = models.CharField(max_length=30)
    apellido_paterno = models.CharField(max_length=30)
    apellido_materno = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_empresa_asociada = models.ForeignKey('Empresa',on_delete=models.CASCADE, db_column='id_empresa')
    correo = models.EmailField(unique=True, max_length=150, blank=True, null=True)
    telefono = models.CharField(max_length=9)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField(default=1)

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)+" "+str(self.apellido_materno)