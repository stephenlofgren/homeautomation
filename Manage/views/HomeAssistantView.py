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
from django.conf import settings
from django.http import HttpResponse


class HomeAssistantView(APIView):
    """defines views for each of the http verbs"""

    endpoint = os.environ.get("HOMEASSISTANT_ENDPOINT", '')

    @staticmethod
    @api_view(['GET'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def status(request, device_id=None):
        """returns the status from the homeassistant service"""

        url = HomeAssistantView.endpoint + "/api/states/%s" % device_id

        ha_password = os.environ.get("HOMEASSISTANT_PASSWORD", '')

        if ha_password == '':
            return HttpResponse(
                'Unauthorized - HOMEASSISTANT_PASSWORD var not set',
                status=401)

        headers = {
            'accept': "application/json",
            'content-type': "text/json",
            'x-ha-access': ha_password,
            'Accept': "application/json"
        }
        static = "static/cert.pem"
        static = os.path.join(settings.BASE_DIR, static)
        response = requests.request("GET", url, headers=headers, verify=static)

        message = json.loads(response.text)
        return Response(message)

    @staticmethod
    @api_view(['PUT'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def turn_off(request, device_code=None):
        """turns_off a light or a switch using the appropriate ha service"""

        payload = {"entity_id": device_code}

        if "light." in device_code:
            url = HomeAssistantView.endpoint + "/api/services/light/turn_off"
        else:
            url = HomeAssistantView.endpoint + "/api/services/switch/turn_off"

        ha_password = os.environ.get("HOMEASSISTANT_PASSWORD", '')

        if ha_password == '':
            return HttpResponse(
                'Unauthorized - HOMEASSISTANT_PASSWORD var not set',
                status=401)

        headers = {
            'accept': "application/json",
            'content-type': "text/json",
            'x-ha-access': ha_password,
            'Accept': "application/json"
        }

        response = requests.request(
            "POST", url, headers=headers, data=json.dumps(payload),
            verify=False)

        message = json.loads(response.text)
        return Response(message)

    @staticmethod
    @api_view(['PUT'])
    @renderer_classes((JSONRenderer,))
    @permission_classes((permissions.AllowAny,))
    def turn_on(request, device_code, on_level=255):
        """turns on a light or switch using the appropriate ha service"""

        if "light." in device_code:
            url = HomeAssistantView.endpoint + "/api/services/light/turn_on"
            payload = {"entity_id": device_code, "brightness": on_level}
        else:
            url = HomeAssistantView.endpoint
            url += "/api/services/switch/turn_on"
            payload = {"entity_id": device_code}

        ha_password = os.environ.get("HOMEASSISTANT_PASSWORD", '')

        if ha_password == '':
            return HttpResponse(
                'Unauthorized - HOMEASSISTANT_PASSWORD var not set',
                status=401)

        headers = {
            'accept': "application/json",
            'content-type': "text/json",
            'x-ha-access': ha_password,
            'Accept': "application/json"
        }

        response = requests.request(
            "POST", url, headers=headers, data=json.dumps(payload),
            verify=False)

        message = json.loads(response.text)
        return Response(message)
