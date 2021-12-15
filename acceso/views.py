from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password

# Create your views here.
class AccesoView(APIView):

    def post(self, request, format=None):

        usuario = request.data['usuario']
        contrasena = request.data['contrasena']

        print(usuario, contrasena)

        try:
            user = User.objects.get(username=usuario)
        except User.DoesNotExist:
            return Response({"msg": "Error en el usuario o contraseña"}, status=status.HTTP_404_NOT_FOUND)

        contrasenaValida = check_password(contrasena, user.password)

        if not contrasenaValida:
            return Response({"msg": "Error en el usuario o contraseña"}, status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)

        print(token.key)

        return Response({"usuario": usuario, "token": token.key, "msg": "Bienvenido"}, status=status.HTTP_200_OK)

    def put(self, request, format=None):

        nombre = request.data['nombre']
        apellido = request.data['apellido']
        nombreDeUsuario = request.data['nombreDeUsuario']
        correo = request.data['correo']
        contrasena = make_password(request.data['contrasena'], None, 'md5')

        #esContrasena = check_password(request.data['contrasena'],contrasena)

        usuario = User(first_name=nombre, last_name=apellido, username=nombreDeUsuario, email=correo,
                       password=contrasena, is_superuser=False)
        usuario.save()

        usuario = User.objects.get(username=nombreDeUsuario)
        token, _ = Token.objects.get_or_create(user=usuario)

        return Response({"usuario": usuario.username, "token": token.key, "msg": "Bienvenido"}, status=status.HTTP_200_OK)
        #return Response({"contraseña":contrasena,"comprobar":esContrasena})

    def delete(self, request, format=None):

        print("Cerrando sesión")
        #print(request.data['unToken'])
        print(request.GET.get('token'))

        token = request.GET.get('token')
        eliminado = Token.objects.filter(key=token).delete()

        print("Sesión cerrada")
        print(eliminado)

        return Response({"token":token}, status=status.HTTP_200_OK)