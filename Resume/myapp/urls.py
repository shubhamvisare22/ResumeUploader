from django.urls import path
from myapp import views
from .views import Resume 


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('<int:pk>', views.CandidateView.as_view(), name='candidate')
]
