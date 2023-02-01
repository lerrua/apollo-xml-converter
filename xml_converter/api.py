from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from xml_converter.services import XmlConverterService


class ConverterViewSet(ViewSet):
    # Note this is not a restful API
    # We still use DRF to assess how well you know the framework
    parser_classes = [MultiPartParser]

    @action(methods=["POST"], detail=False, url_path="convert")
    def convert(self, request, **kwargs):
        xml_file = request.data.get("file")
        if xml_file is None:
            return Response(
                {"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not xml_file.name.endswith(".xml"):
            return Response(
                {
                    "error": 'File extension "json" is not allowed. Allowed extensions are: xml.'
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        xml_dict = XmlConverterService(request.data["file"]).convert_to_dict(
            custom_format=True
        )
        return Response(xml_dict)
