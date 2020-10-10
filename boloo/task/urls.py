# from .import views
from django.urls import path
from .views import(
    list_all_shipment,
    shipment_details,
    GetList,
    AddShipmentAPIView,
    )

urlpatterns = [
	 # List of All Shipments From LocalDB and Company API's
    path('ListAllShipment/', list_all_shipment, name='list_all_shipment'), 
     # Detail of Particular Shipments via shipment_id   
    path('ShipmentDetails/', shipment_details, name='shipment_details'),
     # This is return user added Shop(shipments)
    path('GetList/', GetList, name='GetList'),
     # Via this we can Add more Shop in DB
    path('addShipments/', AddShipmentAPIView, name='AddShipmentAPIView'), 
]



