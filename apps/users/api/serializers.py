from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Muestra todos los campos
        #fields = ['name', 'last_name', 'email']  -> para darle campos especificos

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password']) # Metodo para encriptar password
        user.save()
        return user
    
    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data) # Actualiza la informacion de la forma por defecto que tiene django rest
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user
    
class UserListSerializer(serializers.ModelSerializer): 
    
    class Meta:
        model: User 
        
    def to_representation(self, instance):
        return {
            "id": instance["id"],
            "username":instance["username"],
            "email": instance["email"],
            "password": instance["password"],
            
        }