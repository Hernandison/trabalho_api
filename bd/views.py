from rest_framework import generics
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer
import boto3
from django.http import JsonResponse

# View para listar todos os usuários e criar um novo usuário
class UsuarioListCreate(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# View para obter, atualizar ou deletar um usuário específico
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

# Função para listar instâncias EC2
def list_ec2_instances(request):
    ec2 = boto3.client('ec2')
    instances = ec2.describe_instances()
    instance_data = []
    for reservation in instances['Reservations']:
        for instance in reservation['Instances']:
            instance_data.append({
                'InstanceId': instance['InstanceId'],
                'InstanceType': instance['InstanceType'],
                'State': instance['State']['Name']
            })
    return JsonResponse({'instances': instance_data})
