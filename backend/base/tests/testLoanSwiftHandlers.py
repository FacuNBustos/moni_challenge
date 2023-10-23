from django.test import TestCase

class LoanSwiftHandlerTestCase(TestCase):

    def setUp(self):
        from ..domain.entities.LoanSwift import LoanSwift
        from ..application.handlers.LoanSwiftHandlers import ListLoanSwiftHandler, DeleteLoanSwiftHandler, PatchLoanSwiftHandler

        self.sutListHandler = ListLoanSwiftHandler
        self.sutDeleteHandler = DeleteLoanSwiftHandler
        self.sutPatchHandler = PatchLoanSwiftHandler

        self.LoanSwiftMock = {
        'document_number': 305747584,
        'first_name': "Esteban",
        'last_name': "Quito",
        'gender': "Male",
        'email': "QuitoelEsteban@gmail.com",
        'amount': 25000
        }
        LoanSwift.objects.create(**self.LoanSwiftMock)

        return super().setUp()
    

    def test_HappyPath_ListHandler(self):

        response = self.sutListHandler()[0]
        self.LoanSwiftMock['id'] = response['id']
        self.assertDictEqual( {**response}, self.LoanSwiftMock )


    def test_HappyPath_DeleteHandler(self):
        from ..application.commands.LoanSwiftCommands import DeleteLoanSwiftCommand

        listLoanSwiftBefereDelete = self.sutListHandler()[0]

        toDelete_id = listLoanSwiftBefereDelete['id']
        command = DeleteLoanSwiftCommand({ "id":toDelete_id })
        self.sutDeleteHandler(command)

        listLoanSwiftAfterDelete = self.sutListHandler()
        self.assertEqual(listLoanSwiftAfterDelete, [])


    
    def test_HappyPath_PatchHandler(self):
        from ..application.commands.LoanSwiftCommands import PatchLoanSwiftCommand

        loanSwiftBeforeToChange = self.sutListHandler()[0]
        toPatch_id = loanSwiftBeforeToChange['id']

        command = PatchLoanSwiftCommand({
            "id": toPatch_id,
            "first_name": "Pedro",
            "email": "pedro@gmail.com"
        })
        print(command.data)
        self.sutPatchHandler(command)
        loanSwiftAfterToChange = self.sutListHandler()[0]

        self.LoanSwiftMock['id'] = toPatch_id
        self.LoanSwiftMock['first_name'] = "Pedro"
        self.LoanSwiftMock['email'] = "pedro@gmail.com"

        self.assertDictEqual( {**loanSwiftAfterToChange} , self.LoanSwiftMock )



        



    
    