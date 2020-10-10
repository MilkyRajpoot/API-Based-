from django.db import models

# Shipment Model 
class Shipments(models.Model):
    shipmentId = models.IntegerField(null=True)
    shipmentDate = models.DateTimeField(auto_now_add=True)
    orderItemId = models.CharField(max_length=255,null=True)
    orderId = models.CharField(max_length=255,null=True)
    orderDate = models.DateTimeField(auto_now_add=True)
    latestDeliveryDate = models.DateTimeField(auto_now_add=True)
    ean = models.CharField(max_length=255,null=True)
    title = models.CharField(max_length=255,blank=True)
    quantity = models.PositiveIntegerField(null=True)
    offerPrice = models.PositiveIntegerField(null=True)
    offerCondition = models.CharField(max_length=255,blank=True)
    fulfilmentMethod = models.CharField(max_length=255,blank=True)

def __str__(self):
    return self.shipmentId




    
