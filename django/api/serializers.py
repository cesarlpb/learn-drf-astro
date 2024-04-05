from rest_framework import serializers
from .models import Album, Song

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['title', 'artist']

class AlbumSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['title', 'release_date', 'songs']
