"""defines X10View"""
import json
import os
import requests

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.decorators import renderer_classes, permission_classes
from rest_framework import permissions
from requests.auth import HTTPBasicAuth
from django.conf import settings


class HomeAssistantView(APIView):
    """defines views for each of the http verbs"""
     
    endpoint = "https://www.lofgrenguenther.com:8123"

    @api_view(['GET'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def status(self, pk=None):

        url = HomeAssistantView.endpoint + "/api/states/%s" % pk
        headers = {
            'accept': "application/json",
            'content-type': "text/json",
            'x-ha-access': "esp8266Fun",
            'Accept': "application/json"
        }
        static = "static/www.lofgrenguenther.com.pem"
        static = os.path.join(settings.BASE_DIR, static)
        response = requests.request("GET", url, headers=headers, verify=static)

        message = json.loads(response.text)
        return Response(message)

    @api_view(['PUT'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def turn_off(self, device_code=None):
        payload = {"entity_id": device_code}

        if "light." in device_code:
            url = HomeAssistantView.endpoint + "/api/services/light/turn_off"
        else:
            url = HomeAssistantView.endpoint + "/api/services/switch/turn_off"

        headers = {
            'accept': "application/json",
            'content-type': "text/json",
            'x-ha-access': "esp8266Fun",
            'Accept': "application/json"
        }

        response = requests.request(
            "POST", url, headers=headers, data=json.dumps(payload),
            verify=False)

        message = json.loads(response.text)
        return Response(message)

    @api_view(['PUT'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def turn_on(self, device_code, on_level=255):

        if "light." in device_code:
            url = HomeAssistantView.endpoint + "/api/services/light/turn_on"
            payload = {"entity_id": device_code, "brightness": on_level}
        else:
            url = "https://www.lofgrenguenther.com:8123"
            url += "/api/services/switch/turn_on"
            payload = {"entity_id": device_code}

        headers = {
            'accept': "application/json",
            'content-type': "text/json",
            'x-ha-access': "esp8266Fun",
            'Accept': "application/json"
        }

        response = requests.request(
            "POST", url, headers=headers, data=json.dumps(payload),
            verify=False)

        message = json.loads(response.text)
        return Response(message)
