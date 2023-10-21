from django.urls import path
from ..controllers.LoanSwiftControllers import listLoanSwift, createLoanSwift

urlpatterns = [
    path( "list/", listLoanSwift ),
    path( "create/", createLoanSwift ),
]