from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

class RegistroView(APIView):
    
    def post(self, request, format=None):

        print("Creando usuario...")
        nombre = request.data['nombre']
        apellido = request.data['apellido']
        nombreDeUsuario = request.data['nombreDeUsuario']
        correo = request.data['correo']
        contrasena = make_password(request.data['contrasena'], None, 'md5')

        usuario = User(first_name=nombre, last_name=apellido, username=nombreDeUsuario, email=correo,
                       password=contrasena, is_superuser=False)
        print("Datos de usuario")
        print(usuario)
        
        usuario.save()

        usuario = User.objects.get(username=nombreDeUsuario)
        token, _ = Token.objects.get_or_create(user=usuario)

        print("Token de usuario")
        print(token.key)

        return Response({"usuario": usuario.username, "token": token.key, "msg": "Bienvenido"}, status=status.HTTP_200_OK)