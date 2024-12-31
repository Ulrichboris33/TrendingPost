# repositories/views.py
from requests import get
from datetime import datetime, timedelta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RepositorySerializer, LanguageSerializer
from django.core.cache import cache

GITHUB_API_URL = "https://api.github.com/search/repositories"

@api_view(['GET'])
def get_repositories(request):
    # Vérification du cache
    cache_key = 'repositories'
    cached_data = cache.get(cache_key)
    if cached_data:
        return Response(cached_data)

    # Calcul des dates des 30 derniers jours
    thirty_days_ago = datetime.now() - timedelta(days=30)
    date_str = thirty_days_ago.strftime('%Y-%m-%d')

    # Effectuer la requête vers l'API GitHub
    url = f'https://api.github.com/search/repositories?q=created:>{date_str}+&sort=stars&order=desc'
    response = get(url)

    if response.status_code != 200:
        return Response({"error": "GitHub API error"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    repositories = response.json().get('items', [])

    
    serializer = RepositorySerializer(repositories, many=True)

    # Mise en cache des résultats pendant 1 heure
    cache.set(cache_key, serializer.data, timeout=3600)

    return Response(serializer.data)

@api_view(['GET'])
def get_languages(request):
    
    repositories = cache.get('repositories')  
    if not repositories:
        return Response({"error": "No repositories found"}, status=status.HTTP_404_NOT_FOUND)

   
    languages = set(repo['language'] for repo in repositories)

    
    serializer = LanguageSerializer([{'language': lang} for lang in languages], many=True)

    return Response(serializer.data)
