from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


@api_view(['POST'])
def ingresar(request):

    usuario = request.POST.get('usuario')
    contasena = request.POST.get('contrasena')

    try:
        user = User.objects.get(username=usuario)
    except User.DoesNotExist:
        return Response("Usuario no existe")

    contrasenaValida = check_password(contasena,user.password)

    if not contrasenaValida:
        return Response("Contraseña invalida")
    
    token, _ = Token.objects.get_or_create(user=user)

    

    print(token.key)

    return Response(token.key)

@api_view(['POST'])
def registrarse(request):
    
    nombre = request.POST.get('nombre')
    apellido = request.POST.get('apellido')
    nombreDeUsuario = request.POST.get('nombreDeUsuario')
    correo = request.POST.get('correo')
    contrasena = request.POST.get('contrasena')

    usuario = User(first_name=nombre,last_name=apellido,username=nombreDeUsuario,email=correo,password=contrasena,is_superuser=False)
    usuario.save()

    usuario = User.objects.get(username=nombreDeUsuario)
    token, _ = Token.objects.get_or_create(user=usuario)

    return Response(token.key)

@api_view(['POST'])
def cerrar(request):
    key = request.POST.get('key')
    eliminado = Token.objects.filter(key=key).delete()

    print(eliminado)

    Response({"msg":"Cerrar"})

