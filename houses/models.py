from django.db import models


class Company(models.Model):
    name = models.CharField("name", max_length=255)

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class House(models.Model):

    house_number = models.CharField("house number", max_length=255)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    floor = models.IntegerField("floor", default=1)
    area = models.DecimalField("area", max_digits=6, decimal_places=3)
    datetime_of_public = models.DateTimeField("datetime of public", auto_now=True)
    date_of_public = models.DateField("date of public", auto_now=True)
    status = models.CharField("status", max_length=255)
    price = models.BigIntegerField("price")

    class Meta:
        verbose_name = "House"
        verbose_name_plural = "Houses"

    def __str__(self):
        return self.house_number

