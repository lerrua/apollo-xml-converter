import xmltodict
from django.core.files.uploadhandler import InMemoryUploadedFile


class XmlConverterService:
    def __init__(self, xml_file: InMemoryUploadedFile) -> None:
        self.xml_file = xml_file

    def convert_to_dict(self) -> dict:
        data_dict = xmltodict.parse(self.xml_file.read())
        return data_dict
