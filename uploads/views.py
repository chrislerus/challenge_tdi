from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import HttpResponse


def upload_file(request):
    return render(request,
                  "uploads/upload.html",
        {})


@require_POST
def display_file(request):
    pic = request.FILES['pic']
    img_data = pic.file.read()

    return HttpResponse(img_data, content_type=pic.content_type)