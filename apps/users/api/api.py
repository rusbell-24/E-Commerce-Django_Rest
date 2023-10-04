from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import  api_view #Libreria para el uso de decoradores
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer

@api_view(['GET','POST'])       #Decorador
def user_api_view(request):
    
    #List
    if request.method == 'GET':
        
        #queryset
        users = User.objects.all().values('id','username','email', 'password')
        users_serializer = UserListSerializer(users, many=True)
        
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    #Create
    elif request.method == 'POST':
        
        #En este caso el serializador funciona como un validador
        user_serializer = UserSerializer(data=request.data)
        
        #validation
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail_api_view(request, pk=None):
    
    # queryset
    user = User.objects.filter(id = pk).first()

    #Validation
    if user:
        
        #retrieve
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status=status.HTTP_200_OK)
        
        #update
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user, data=request.data)
            
            #validation
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status=status.HTTP_200_OK)
            return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        #delete
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario eliminado correctamente!'}, status=status.HTTP_200_OK)
        
    return Response({'message':'No se ha encontrado un usuario con estos datos'}, status=status.HTTP_400_BAD_REQUEST)