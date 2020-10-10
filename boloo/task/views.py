from django.shortcuts import render
from rest_framework import status
from task.models import Shipments
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
import requests
import json
from random import randint


url = "https://login.bol.com/token"
# querystring = {"grant_type":"client_credentials"}
headers = {'authorization': "Basic ZDRhM2JjZmYtNjI2Mi00ZjAzLWJhYTAtOWU3MzNkMmNlZWM3OkFNeUhiQm81VFJpU1NDd3Jfb0ZWVzVERDJ5anlvOWwySDNrSGdlRVRyVExUd3VoMFptSTZXS0kwWkJVbXQ1aG5OOTNvTVFIc2RCVV9mS2I5OE10c0s2UQ==",}

# Method for Generate Access Token (code to auto-refresh the access token)
def access_token():
    response = requests.request("POST", url, headers=headers).json()
    token = (response['access_token'])   
    return token
   
# Method for fetching All List of Shipments from Local DB and Company API's 
@api_view(['GET',])
def list_all_shipment(request):
    if request.method == 'GET':
        token = access_token()
        url = "https://api.bol.com/retailer/shipments"
        headers = {
            'authorization': "Bearer "+token,
            'accept': "application/vnd.retailer.v3+json",
            }
        response = requests.request("GET", url, headers=headers).json()
        shipmentResponseAPI = response["shipments"]
       
        shipmentResQs = Shipments.objects.all().values()
        shipment_list = getAllShipmentList(shipmentResQs)
        for valuesItems in shipmentResponseAPI:
            shipment_list.append(valuesItems)
            responseData = {}
            responseData["shipments"]=shipment_list
       
        return Response(responseData)

# Method for fetching Detail of Particular Shipment_Id from Company provided URL
@api_view(['GET',])
def shipment_details(request):
    if request.method == 'GET':
        token = access_token()
        url = "https://api.bol.com/retailer/shipments/714782685"
        headers = {
            'authorization': "Bearer "+token,
            'accept': "application/vnd.retailer.v3+json",
            }

        response = requests.request("GET", url, headers=headers).json()
        shipment_list = (response)
        return Response(shipment_list)


# Method for fetching Shipment List from my local DB and we sync all Shipments for his shop 
@api_view(['GET',])
def GetList(request):
    if request.method == 'GET':
        ship_list = Shipments.objects.all().values()
        mesg=list(ship_list)
        return Response(mesg)


# Method for seller can add his Shop and store each data item from shipment detail
@api_view(['POST',])
def AddShipmentAPIView(request):
    shipmentItems = {}
    shipmentItemList = []

    title = request.data.get('title', None)
    shipmentId = request.data.get('shipmentId', randint(112, 9991213113))
    orderItemId = request.data.get('orderItemId', "2841788590")
    orderId = request.data.get('orderId', "2841788590")
    quantity = request.data.get('quantity',1)
    offerPrice = request.data.get('offerPrice',None)
    offerCondition = request.data.get('offerCondition',"NEW")
    fulfilmentMethod = request.data.get('fulfilmentMethod',"FBR")
    ean = request.data.get('ean', "8958226364")

    saveQuerySet = Shipments.objects.create(shipmentId=shipmentId,orderItemId =orderItemId,
                        orderId = orderId,ean = ean,title = title,quantity =quantity,
                        offerPrice =offerPrice,offerCondition =offerCondition,
                        fulfilmentMethod = fulfilmentMethod)
    saveQuerySet.save()
   
    shipmentItemList.append({
            "shipmentId":saveQuerySet.shipmentId,
            "orderItemId": saveQuerySet.orderItemId,
            "orderId": saveQuerySet.orderId,
            "orderDate": saveQuerySet.orderDate,
            "latestDeliveryDate": saveQuerySet.latestDeliveryDate,
            "ean": saveQuerySet.ean,
            "title": saveQuerySet.title,
            "quantity": saveQuerySet.quantity,
            "offerPrice": saveQuerySet.offerPrice,
            "offerCondition": saveQuerySet.offerCondition,
            "fulfilmentMethod": saveQuerySet.fulfilmentMethod,
            "shipmentDate":saveQuerySet.shipmentDate
        })
    shipmentItems["shipmentItems"] = shipmentItemList
    return SuccessResponse(shipmentItems, status=200)
   

def SuccessResponse(objects, status):
    return JsonResponse({
        "results":objects,
        "status":status
        },safe=False)


# To Return data as boloo API's and merge data as user added to new ship
def getAllShipmentList(shipmentRes):
    shipments = []
       
    for items in shipmentRes:
        shipmentId = items["shipmentId"]
        shipmentDate = items["shipmentDate"]
        orderItemId = items["orderItemId"]
        orderId = items["orderId"]
       
        shipments.append({
            "shipmentDate":shipmentDate,
            "shipmentId":shipmentId,
            "shipmentItems":[{
                "orderItemId":orderItemId,
                "orderId":orderId
                }]

            })

    return shipments
