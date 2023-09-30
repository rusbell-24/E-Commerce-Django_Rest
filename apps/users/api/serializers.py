from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # Muestra todos los campos
        #fields = ['name', 'last_name', 'email']  -> para darle campos especificos