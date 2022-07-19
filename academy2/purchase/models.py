from django.db import models
from django.contrib.auth.models import User
from package.models import Package
from finance.models import Payment
# Create your models here.


class Purchase(models.Model):
    PAID = 10
    NOT_PAID = -10

    STATUS_CHOICES = (
        (PAID, 'Paid'),
        (NOT_PAID, 'Not paid'),
    )
    user = models.ForeignKey(User, related_name='purchase', on_delete=models.SET_NULL, null=True)
    package = models.ForeignKey(Package, related_name='purchase', on_delete=models.SET_NULL, null=True)
    price = models.PositiveBigIntegerField()
    status = models.SmallIntegerField(choices=STATUS_CHOICES, default=NOT_PAID)
    payment = models.ForeignKey(Payment, related_name='purchase', on_delete=models.PROTECT)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} >> {self.package}"
    
    @classmethod
    def create(cls, package, user):
        if package.is_enable:
            return cls.objects.create(
                user=user, package=package, price=package.price
            )
        return None
