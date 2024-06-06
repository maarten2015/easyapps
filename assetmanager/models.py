from django.db import models

from easyapps.utils import BaseModel
from internal.crm.models import Customer


# Create your models here.
class AssetList(BaseModel):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(Customer, on_delete=models.PROTECT)


class AssetItem(BaseModel):
    list = models.ForeignKey(AssetList, on_delete=models.CASCADE, related_name="assets")
    item = models.CharField(max_length=255)
    purchase_date = models.DateField(null=True)
    invoice = models.ImageField(null=True)
    value = models.DecimalField(decimal_places=2, max_digits=10)
    comments = models.TextField()


class AssetImage(BaseModel):
    asset_item = models.ForeignKey(
        AssetItem, on_delete=models.CASCADE, related_name="images"
    )
    file = models.ImageField()
