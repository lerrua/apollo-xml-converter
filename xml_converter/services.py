import xmltodict
from django.core.files.uploadhandler import InMemoryUploadedFile


class XmlConverterService:
    def __init__(self, xml_file: InMemoryUploadedFile) -> None:
        self.xml_file = xml_file

    def convert_to_dict(self, custom_format: bool=False) -> dict:
        """
        Convert xml file to a dict
        :param custom_format: if True, the dict will be formatted in a custom way
        :return: dict
        """
        data_dict = xmltodict.parse(self.xml_file.read())
        if custom_format is False:
            return data_dict

        root = data_dict.get("Root")
        if not root:
            data_dict["Root"] = ""
            return data_dict

        custom_format_list = []
        for i, value in root.items():
            for item in value:
                custom_format_list.append(
                    {i: [{j: k} for j, k in item.items()]})
        data_dict["Root"] = custom_format_list

        return data_dict
