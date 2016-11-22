from django.db import models
from django.utils import timezone
# Create your models here.
class Conceptos(models.Model):
    concepto=models.CharField(max_length=100)

    def __str__(self):
        return self.concepto

class Post(models.Model):
        observacion = models.TextField()
        published_date = models.DateTimeField(blank=True, null=True)
        entrada = models.IntegerField(null=True, blank=True)
        salida= models.IntegerField(null=True, blank=True)
        saldo_general=models.IntegerField(null=True, blank=True)
        idconcepto = models.ForeignKey(Conceptos)

        def publish(self):
            self.published_date = timezone.now()
            self.save()

        def __str__(self):
            return self.idconcepto