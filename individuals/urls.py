from django.urls import path
from . import views

urlpatterns = [
    # path("january/", views.january),
    # path("february/", views.february),
    # path("march/", views.march),
    path("", views.index),
    path("<int:month>/", views.montly_challenge_by_numbers),
    path("<str:month>/", views.monthly_challenge, name="month-challenge")

]
