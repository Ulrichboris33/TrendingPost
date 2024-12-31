# repositories/serializers.py
from rest_framework import serializers

class RepositorySerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()
    language = serializers.CharField()

    # Vous pouvez aussi ajouter un champ personnalisé "stars" pour la réponse, si nécessaire
    stars = serializers.IntegerField(source='stargazers_count')
    created_at = serializers.DateTimeField()  # Ajout du champ created_at pour la date de soumission
    avatar_url = serializers.CharField(source='owner.avatar_url')  # URL de l'avatar du propriétaire du dépôt
class LanguageSerializer(serializers.Serializer):
    language = serializers.CharField()
