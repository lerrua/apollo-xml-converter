from django.http import JsonResponse
from django.shortcuts import render

from xml_converter.forms import XMLConverterFileForm
from xml_converter.services import XmlConverterService


def upload_page(request):
    if request.method == "POST":
        form = XMLConverterFileForm(request.POST, request.FILES)
        if form.is_valid():
            xml_dict = XmlConverterService(request.FILES["file"]).convert_to_dict(
                custom_format=True
            )
            return JsonResponse(xml_dict)
    else:
        form = XMLConverterFileForm()
    return render(request, "upload_page.html", {"form": form})
