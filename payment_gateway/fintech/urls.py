
from django.urls import path
from fintech import views
from fintech.views import payment





urlpatterns = [
 
    path("payment/", views.payment),
    path("testing/", views.testing)


]
