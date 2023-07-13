
from django.urls import path
from api.views import AllDogList, AllBreedList, SpecificDogDetail, SpecificBreedDetail

urlpatterns = [
    path('dogs/', AllDogList.as_view(), name='dogs-list-view'),
    path('breeds/', AllBreedList.as_view(), name='breeds-list-view'),
    path('dogs/<int:pk>/', SpecificDogDetail.as_view(), name='specific-dog-details-view'),
    path('breeds/<int:pk>/', SpecificBreedDetail.as_view(), name='specific-breed-details-view'),

]