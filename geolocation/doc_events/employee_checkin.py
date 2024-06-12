import frappe
import json
import requests

def validate(doc, methods=None):
    if doc.latitude and doc.longitude and not doc.custom_location:
        url = "https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json".format(
            lat = doc.latitude,
            lon = doc.longitude
        )
        response = requests.get(url)
        if response.status_code == 200:
            response = response.json()
            doc.custom_location = str(response.get("display_name"))
        else:
            doc.custom_location = ""
        