from django.db import models

# Create your models here.
class item(models.Model):
    index = models.AutoField(primary_key=True, verbose_name="Primary Key")
    name = models.CharField(max_length=200, verbose_name="Product Name")
    qty = models.CharField(max_length=10, verbose_name="Quantity")
    price = models.DecimalField(max_digits=10, decimal_places=1, verbose_name="Price")

    def save(self, force_insert=False, force_update=False):
        self.name = self.name.title()
        self.qty = self.qty.lower()
        self.price = self.price
        super(item, self).save(force_insert, force_update)