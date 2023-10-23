from django.urls import path
from ..controllers.LoanSwiftControllers import listLoanSwift, createLoanSwift, deleteLoanSwift, patchLoanSwift

urlpatterns = [
    path( "list/", listLoanSwift ),
    path( "create/", createLoanSwift ),
    path( "path/<str:id>/", patchLoanSwift ),
    path( "delete/<str:id>/", deleteLoanSwift ),
]