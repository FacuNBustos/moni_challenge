from django.urls import path, include
from .http.routes import LoanSwiftRouter

urlpatterns = [
    path( "loanswift/", include(LoanSwiftRouter) )
]