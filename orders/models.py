from django.db import models


class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Заявка создана'),
        ('in_delivery', 'Товар передан в доставку'),
        ('delivered', 'Товар доставлен'),
    ]
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.id} - {self.status}'