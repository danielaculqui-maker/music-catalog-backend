from rest_framework import serializers
from .models import Artista, Album


class AlbumSerializer(serializers.ModelSerializer):
    artista_nombre = serializers.CharField(source='artista.nombre', read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'titulo', 'fecha_lanzamiento', 'numero_canciones', 'artista', 'artista_nombre']


class ArtistaSerializer(serializers.ModelSerializer):
    albumes = AlbumSerializer(many=True, read_only=True)

    class Meta:
        model = Artista
        fields = ['id', 'nombre', 'biografia', 'genero_musical', 'fecha_formacion', 'foto', 'albumes']
        