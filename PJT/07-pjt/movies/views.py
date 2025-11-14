from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Actor, Movie, Review
from .serializers import (
    ActorListSerializer, ActorDetailSerializer,
    MovieListSerializer, MovieDetailSerializer,
    ReviewListSerializer, ReviewDetailSerializer,
    ReviewSerializer
)


@api_view(['GET'])
def actor_list(request):
    """전체 배우 목록 조회"""
    actors = Actor.objects.all()
    serializer = ActorListSerializer(actors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def actor_detail(request, actor_pk):
    """단일 배우 정보 조회"""
    actor = get_object_or_404(Actor, pk=actor_pk)
    serializer = ActorDetailSerializer(actor)
    return Response(serializer.data)


@api_view(['GET'])
def movie_list(request):
    """전체 영화 목록 조회"""
    movies = Movie.objects.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def movie_detail(request, movie_pk):
    """단일 영화 정보 조회"""
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


@api_view(['GET'])
def review_list(request):
    """전체 리뷰 목록 조회"""
    reviews = Review.objects.all()
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, review_pk):
    """단일 리뷰 조회, 수정, 삭제"""
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        review.delete()
        return Response({'message': 'review is deleted.'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def create_review(request, movie_pk):
    """영화에 대한 리뷰 생성"""
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save(movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
