from rest_framework.test import APITestCase
from rest_framework import status

class AuthTestCase(APITestCase):


    def setUp(self):
        from django.contrib.auth.models import User
        self.user = User.objects.create_superuser(
            last_name="test",
            username="test",
            password="test",
            email="test@test.com"
        )

        return super().setUp()

    def test_HappyPatch_Login(self):

        login_url = '/api/v1/auth/login/'

        response = self.client.post(
            login_url,
            {
                'username': self.user.username,
                'password': 'test'
            },
            format='json'
        )
        
        self.assertEqual( response.status_code, status.HTTP_200_OK )
        self.assertIsNotNone( response.data['access'] )
        self.assertIsNotNone( response.data['refresh'] )

    
    def test_HappyPatch_RefreshToken(self):
        refresh_url = '/api/v1/auth/token/refresh/'
        login_url = '/api/v1/auth/login/'

        token = self.client.post(
            login_url,
            {
                'username': self.user.username,
                'password': 'test'
            },
            format='json'
        ).data['refresh']

        response = self.client.post(
            refresh_url,
            {
                'refresh': token,
            },
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        