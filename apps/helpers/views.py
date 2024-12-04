from django.shortcuts import render
from django.apps import apps
from rest_framework.response import Response
from rest_framework.views import APIView
# from apps.helpers import serializers
from apps.helpers import models as HelperModels
from rest_framework.request import Request

# Create your views here.
class FileUpload(APIView):
    permission_classes = ()
    def post(self: 'FileUpload', request: Request, version: str) -> Response:
        pass
        # data = request.data
        # createdobj = HelperModels.FileUpload.objects.create(file=data.get("file"))
        # return Response(
        #     {
        #         "success": True,
        #         "file": request.build_absolute_uri(createdobj.file.url),
        #         "id": createdobj.id,
        #     }
        # )