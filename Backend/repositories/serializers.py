# repositories/serializers.py
from rest_framework import serializers

class RepositorySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    language = serializers.CharField()

    
    stars = serializers.IntegerField(source='stargazers_count')
    created_at = serializers.DateTimeField() 
    avatar_url = serializers.CharField(source='owner.avatar_url')  # URL de l'avatar du propriétaire du dépôt
class LanguageSerializer(serializers.Serializer):
    language = serializers.CharField()
