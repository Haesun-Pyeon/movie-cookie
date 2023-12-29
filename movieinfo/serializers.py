from rest_framework import serializers
from rest_framework.validators import ValidationError
from django.db.models import Q

from .models import MovieInfo, OneLineCritic
from accounts.models import User
from accounts.models import LikeMovie, WatchedMovie, WatchlistMovie


class MovieInfoSerializers(serializers.ModelSerializer):
    class Meta:
        model = MovieInfo
        fields = "__all__"
        depth = 1


class ExceptSensitiveInfoUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "nickname", "profile_picture"]


class OneLineCriticSerializers(serializers.ModelSerializer):
    author = ExceptSensitiveInfoUserSerializers()

    class Meta:
        model = OneLineCritic
        fields = [
            "id",
            "content",
            "starpoint",
            "created_at",
            "updated_at",
            "author",
            "movie",
        ]

    def validate_content(self, value):
        if len(value) <= 3:
            raise ValidationError("내용이 너무 짧습니다.")
        return value

    def validate_starpoint(self, value):
        if not value:
            raise ValidationError("별점을 입력하지 않았습니다.")

        if value < 0 or value > 5:
            raise ValidationError("잘못된 별점 입력입니다.")
        return value

    def validate(self, value):
        try:
            a = OneLineCritic.objects.get(
                Q(author=User.objects.get(id=self._kwargs["data"]["author"]))
                & Q(movie=MovieInfo.objects.get(id=self._kwargs["data"]["movie"]))
            )

            print(a)
        except:
            return value
        raise ValidationError("잘못된 접근입니다.")


class OneLineCriticSaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = OneLineCritic
        fields = [
            "id",
            "content",
            "starpoint",
            "created_at",
            "updated_at",
            "author",
            "movie",
        ]

    def validate_content(self, value):
        if len(value) <= 3:
            raise ValidationError("내용이 너무 짧습니다.")
        return value

    def validate_starpoint(self, value):
        if not value:
            raise ValidationError("별점을 입력하지 않았습니다.")

        if value < 0 or value > 5:
            raise ValidationError("잘못된 별점 입력입니다.")
        return value

    def validate(self, value):
        try:
            a = OneLineCritic.objects.get(
                Q(author=User.objects.get(id=self._kwargs["data"]["author"]))
                & Q(movie=MovieInfo.objects.get(id=self._kwargs["data"]["movie"]))
            )

            print(a)
        except:
            return value
        raise ValidationError("잘못된 접근입니다.")


class OneLineCriticCreateUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = OneLineCritic
        fields = ["content", "starpoint"]

    def validate_content(self, value):
        if len(value) <= 3:
            raise ValidationError("내용이 너무 짧습니다.")
        return value

    def validate_starpoint(self, value):
        if not value:
            raise ValidationError("별점을 입력하지 않았습니다.")

        if value < 0 or value > 5:
            raise ValidationError("잘못된 별점 입력입니다.")
        return value


class LikeMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = LikeMovie
        fields = ["id"]

    def validate(self, value):
        try:
            LikeMovie.objects.get(
                Q(user=User.objects.get(username=self._kwargs["data"]["user"]))
                & Q(movie=MovieInfo.objects.get(id=self._kwargs["data"]["movie_id"]))
            )
        except:
            return value
        raise ValidationError("이미 좋아요를 눌렀습니다.")


class WatchedMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = WatchedMovie
        fields = ["id"]

    def validate(self, value):
        try:
            WatchedMovie.objects.get(
                user=self._kwargs["data"]["user"],
                movie=MovieInfo.objects.get(id=self._kwargs["data"]["movie_id"]),
            )
        except:
            return value
        raise ValidationError("이미 등록되어 있습니다.")


class WatchlistMovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = WatchlistMovie
        fields = ["id"]

    def validate(self, value):
        try:
            WatchlistMovie.objects.get(
                user=self._kwargs["data"]["user"],
                movie=MovieInfo.objects.get(id=self._kwargs["data"]["movie_id"]),
            )
        except:
            return value
        raise ValidationError("이미 등록되어 있습니다.")
