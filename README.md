# TrendingPost
Guide pour excécuter le projet TrendingPost.

## Instructions pour le Backend
Ce guide vous aidera à démarrer le projet Django dans le dossier Backend depuis le début, en configurant un environnement virtuel, en installant Django, et egalement , demarrer le font-end réalisé avec vueJS
1. Cloner le projet

Cloner le projet et ouvrez-le avec votre éditeur de code.
2. Installer python

Assurer vous d'avoir python installé sur votre machine ; Si ce n'est pas le cas, rendez-vous sur le site de python pour installer une version selon votre système.https://www.python.org/

3. Créer un environnement virtuel

Ouvrez le terminal et exécutez la commande suivante pour créer un environnement virtuel:

```bash
python -m venv nom_de_l_environnement  # Préférez 'venv' ou 'env' ou '.env' ou '.venv'
```
4. Activer l'environnement virtuel

Naviguez vers le dossier Scripts (Windows) ou bin (Unix) et activez l'environnement:

- Pour unix
```bash
source venv/bin/activate
```
- Pour windows
```bash
.\venv\Scripts\activate
```
5. Installer Django

Assurez-vous que l'environnement est activé, puis installez Django:
```bash
pip install django  # Ou spécifiez la version: pip install django==version
```
6. Installer les dependances depuis le fichier requirements.txt

Enregistrez les dépendances de votre projet:
```bash
pip install -r requirements.txt
```
7. Lancer le serveur

Démarrez le serveur de développement:
```bash
python manage.py runserver
```
8. Accédez à l’API :

Les dépôts GitHub : http://127.0.0.1:8000/api/repositories/

Les langages de programmation : http://127.0.0.1:8000/api/languages/

## Instructions pour le Frontend

Déplacer vous dans le dossier fontend
```bash
cd frontend
```
Installez les dépendances :
```bash
npm install
```
Lancez le serveur de développement 
```bash
npm run serve
```

Accédez à l’application :
le Frontend sera disponible sur un lien qui vous sera fourni dans le terminal

## Fonctionnalités Bonus Implémentées
•Implémentez la pagination pour récupérer et afficher les dépôts par lots de
10 ou 20.
•Mettez en cache les résultats pour minimiser les appels à l'API GitHub.

•Ajoutez une gestion des erreurs pour des cas comme les limites de taux de
l'API GitHub ou des problèmes de réseau.

Ajoutez une barre de recherche pour filtrer les dépôts par nom ou
description.

•Ajoutez un style de base pour améliorer l'expérience utilisateur.
