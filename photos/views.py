from django.shortcuts import render
from django.http import HttpResponse
from photos.models import Photo

def home(request):
    '''
    Renderiza el home con un listado de fotos
    ;param request: objeto HttpRequest con los datos de la petición
    ;return: objeto HttpResponse con los datos de la respuesta
    '''
    photos = Photo.objects.all()  # recupera todas las fotos de la base de datos
    context = {'photos_list': photos}
    return render(request, 'photos/home.html', context)
