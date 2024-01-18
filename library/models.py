from django.db import models

# Create your models here.
# estructura de la tabla libros

class Libro(models.Model):
    id= models.AutoField(primary_key = True)
    titulo = models.CharField(max_length = 100, verbose_name= 'Título')
    imagen = models.ImageField(upload_to='imagenes/',verbose_name= 'Imagen', null=True)
    descripcion = models.TextField(verbose_name ='Descripción', null = True)

    def __str__(self):
        fila = "Título: " + self.titulo +" - " + "Descripción: " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents= False):
        self.imagen.storage.delete(self.imagen.name)
        super.delete()




# class Prestamos(models.Model):
#     identificacion = models.CharField(primary_key=True, max_length=15)
#     nombres = models.CharField(max_length=30)
#     apellidos = models.CharField(max_length=30)

#     def __str__(self): 
#         return f"{self.identificacion} - {self.nombres} {self.apellidos}"