from django.db import models
from django.contrib.auth.models import User

class Accident(models.Model):
    TYPES = [
        ('fatal', 'Смертельное'),
        ('serious', 'Серьёзное'),
        ('minor', 'Незначительное'),
        ('multiple', 'Более двух машин'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    accident_type = models.CharField(max_length=20, choices=TYPES, verbose_name="Тип ДТП")
    latitude = models.FloatField(verbose_name="Широта")
    longitude = models.FloatField(verbose_name="Долгота")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.get_accident_type_display()})"
