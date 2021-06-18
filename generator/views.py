from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def about(request):
    return render(request, 'generator/about.html')

def password(request):

    # Defino las cadenas que voy a ir agregando a la lista de la cual elijo los caracteres
    alphabet_list = 'abcdefghijklmnñopqrstuvwxyz'
    special_list = '!#@$%&/<>*+~'
    numbers_list = '1234567890'

    characters = list(alphabet_list)

    if request.GET.get('uppercase'):
        characters.extend(list(alphabet_list.upper()))

    if request.GET.get('special'):
        characters.extend(list(special_list))

    if request.GET.get('numbers'):
        characters.extend(list(numbers_list))

#   Traigo la longitud que se seleccionó en el dropdown length del home
    length = int(request.GET.get('length',12))

#   Fuerzo a que la primera letra del pass siempre es una letra minúscula
    thepassword = random.choice(alphabet_list)

    for x in range(length-1):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})
