from rest_framework import serializers
from .models import Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'name']


class MovieTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title']


class ActorDetailSerializer(serializers.ModelSerializer):
    movies = MovieTitleSerializer(many=True, read_only=True)

    class Meta:
        model = Actor
        fields = ['id', 'name', 'movies']


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'overview']


class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'content']


class ReviewDetailSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'movie', 'title', 'content']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['title', 'content']


class MovieDetailSerializer(serializers.ModelSerializer):
    actors = serializers.SerializerMethodField()
    reviews = ReviewListSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'overview', 'release_date', 'poster_path', 'actors', 'reviews']

    def get_actors(self, obj):
        return [actor.name for actor in obj.actors.all()]
