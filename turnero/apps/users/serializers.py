
from rest_framework import routers, serializers
from apps.users.models import persona

class userSerializer(serializers.ModelSerializer):   
    def validate_username(self, username):
         is_already_exists = persona.objects.filter(username=username).exists()
         if is_already_exists:
             raise serializers.ValidationError('already exists')
         return username
    class Meta:
        model = persona
        fields =  ('__all__')
