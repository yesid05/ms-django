from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password

class AccesoView(APIView):
    
    def post(self, request, format=None):

        print("Iniciando sesión...")
        
        usuario = request.data['usuario']
        contrasena = request.data['contrasena']

        print("Datos de usuario")
        print(usuario, contrasena)

        try:
            user = User.objects.get(username=usuario)
        except User.DoesNotExist:
            return Response({"msg": "Error en el usuario o contraseña"}, status=status.HTTP_404_NOT_FOUND)

        contrasenaValida = check_password(contrasena, user.password)

        if not contrasenaValida:
            return Response({"msg": "Error en el usuario o contraseña"}, status=status.HTTP_404_NOT_FOUND)

        token, _ = Token.objects.get_or_create(user=user)

        print("Token de usuario")
        print(token.key)

        return Response({"usuario": usuario, "token": token.key, "msg": "Bienvenido"}, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):

        print("Cerrando sesión")

        token = request.data['unToken'] #Postman
        #token = request.GET.get('token') #Despliegue
        
        print("Token de usuario")
        print(token)

        if Token.objects.filter(key=token).delete() :
            print("Sesión cerrada")
            return Response({"token":token}, status=status.HTTP_200_OK)
        else:
            print("Error, cerrando sesión")
            return Response({"token":token}, status=status.HTTP_404_NOT_FOUND)
