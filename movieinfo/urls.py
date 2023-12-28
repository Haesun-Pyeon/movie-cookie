from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

movie_info_router = DefaultRouter()
movie_info_router.register("detail", views.MovieInfoViewSet)
one_line_critic_router = DefaultRouter()
one_line_critic_router.register("onelinecritic", views.OneLineCriticViewSet)
user_llw_router = DefaultRouter()
user_llw_router.register("userlike", views.UserLWWViewSet)

urlpatterns = [
    path("search/", views.SearchMovieAPIView.as_view(), name="search"),
    path("", include(movie_info_router.urls)),
    path("detail/<int:movie_id>/", include(one_line_critic_router.urls)),
    path("detail/<int:movie_id>/<str:mode>/", include(user_llw_router.urls)),
]
