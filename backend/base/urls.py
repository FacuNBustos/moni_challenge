from django.urls import path, include
from .http.routes import LoanSwiftRouter, AuthRouter

urlpatterns = [
    path( "loanswift/", include(LoanSwiftRouter) ),
    path( "auth/", include(AuthRouter) )
]