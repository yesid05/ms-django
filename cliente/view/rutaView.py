from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.response import Response
import json

from cliente.model.ruta import Ruta
from cliente.serializer.rutaSerializer import RutaSerializer

class RutaView(viewsets.ModelViewSet):
    serializer_class = RutaSerializer
    queryset = Ruta.objects.all()
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=['POST'])
    def buscar(self, request):
        data = request.data
        print("data", request.data['q'])
        queryset = Ruta.objects.filter(descripcion__icontains=data['q'])
        #queryset = Ruta.objects.all()
        serializer = RutaSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        #if serializer.is_valid():
            #return Response(serializer.data)
        #else:
            #return Response(serializer.errors,
                            #status=status.HTTP_400_BAD_REQUEST)
        