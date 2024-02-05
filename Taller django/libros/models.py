from django.db import models


# Create your models here.
class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    resume = models.TextField()
    #editorial = models.CharField(max_length=200)
    #isbn = models.CharField(max_length=200)
    #paginas = models.IntegerField()
    #fecha_publicacion = models.DateField()
    #precio = models.DecimalField(max_digits=10, decimal_places=2)
    #imagen = models.ImageField(upload_to='libros/')
    #disponible = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
