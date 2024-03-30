from django.db import models

from houses.models import House


class Agreement(models.Model):
    full_name_of_client = models.CharField("fullname of client", max_length=100)
    phone_number_of_client = models.CharField("phone number of client", max_length=20)
    date_of_create = models.DateTimeField(auto_now=True)
    id_of_agreement = models.IntegerField()
    status = models.CharField("status", max_length=100)

    house = models.ForeignKey(House, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Agreement"
        verbose_name_plural = "Agreements"

    def __str__(self):
        return self.full_name_of_client