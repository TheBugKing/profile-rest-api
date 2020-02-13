from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views


router = DefaultRouter()
router.register('hello-viewsets',views.HelloViewSets, base_name ='hello-viewset')
router.register('UserProfile',views.UserProfileViewSet)
router.register('feed',views.UserProfileFeedViewSet)

urlpatterns = [
    path('hello-view',views.HelloApiView.as_view()),
    path('login',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
]
