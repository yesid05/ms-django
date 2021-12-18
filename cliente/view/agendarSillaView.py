from datetime import date

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User



from cliente.model.agendarSilla import AgendarSilla
from cliente.model.ruta import Ruta
from cliente.model.silla import Silla
from cliente.serializer.agendarSillaSerializer import AgendarSillaSerializer

class AgendarSillaView(APIView):

    def post(self, request, format=None):
        
        unIdUsuario = request.data['usuario']
        unIdSilla = request.data['silla']
        unIdRuta = request.data['ruta']
        unaFecha = request.data['fecha']

        objUsuario = User.objects.get(username=unIdUsuario)
        objSilla = Silla.objects.get(pk=unIdSilla)
        objRuta = Ruta.objects.get(pk=unIdRuta)
        objFecha = date.fromtimestamp(unaFecha)

        #existe = AgendarSilla.objects.get(silla=objSilla)
        
        if AgendarSilla.objects.filter(fecha=objFecha,silla=objSilla,ruta=objRuta):
            print("existe")
            return Response({"msg":"error"})
        else:
            print("No existe")
            agendar = AgendarSilla(usuario=objUsuario,silla=objSilla,ruta=objRuta,fecha=objFecha)
            #return Response({"usuario":objUsuario.username,"silla":objSilla.nombre,"ruta":objRuta.descripcion,"fecha":objFecha})
            #agendar.save()
            return Response({"msg":"ok"})

        #agendar = AgendarSilla(usuario=objUsuario,silla=objSilla,ruta=objRuta,fecha=objFecha)
        #agendar.save()
        #print(agendar.silla.nombre)
        #return Response({"usuario":objUsuario.username,"silla":objSilla.nombre,"ruta":objRuta.descripcion,"fecha":objFecha})
        #return Response({"msg":"ok"})

    def get(self, request, format=None):
        unIdUsuario = request.GET.get('usuario') #despliegue
        #unIdUsuario = request.data['usuario'] #postman
        
        objUsuario = User.objects.get(username=unIdUsuario)

        queryset = AgendarSilla.objects.filter(usuario=objUsuario)
        serializer = AgendarSillaSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def delete(self, request, format=None):

        unId = request.data['id']

        objAgendarSilla = AgendarSilla.objects.get(pk=unId)

        if objAgendarSilla.delete():
            return Response({"msg":"ok"})
        else:
            return Response({"msg":"error"})
