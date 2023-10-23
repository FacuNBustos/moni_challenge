from django.test import TestCase
from ..application.commands.LoanSwiftCommands import CreateLoanSwiftCommand, DeleteLoanSwiftCommand, PatchLoanSwiftCommand
from uuid import uuid4

class LoanSwiftCommandTestCase(TestCase):

    sutCreate = CreateLoanSwiftCommand
    sutDelete = DeleteLoanSwiftCommand
    sutPatch = PatchLoanSwiftCommand 

    def test_HappyPatch_CreateCommand(self):
        payload = {
            'document_number': 30546758,
            'first_name': "Francisco",
            'last_name': "Saumerio",
            'gender': "Male",
            'email': "francisco@gmail.com",
            'amount': 15000,
        }
        sut = self.sutCreate(payload)

        self.assertEqual( sut.data, payload )

    def test_HappyPatch_DeleteLoanSwiftCommand(self):
        payload = {
            id: uuid4()
        }
        sut =  DeleteLoanSwiftCommand(payload)

        self.assertEqual( sut.data, payload )
        
    def test_HappyPatch_PatchLoanSwiftCommand(self):
        payload = {
            'id': uuid4(),
            'first_name': "Francisco",
            'last_name': "Saumerio",
            'amount': 2000
        }
        sut = PatchLoanSwiftCommand(payload)

        self.assertEqual( sut.data, payload )