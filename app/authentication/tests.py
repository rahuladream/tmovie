# python core impprt

from django.test import TestCase
# django core import
from model_mommy import mommy

# Local imports
from .models import CustomUser
from .serializers import UserCreateSerializer, UserListSearialzer


# DRF import


class UserAPITest(TestCase):

    def test_list_user(self):
        """
        Ensure that the model creating list
        """
        
        user                        = mommy.make(CustomUser)
        self.assertTrue(isinstance(user, CustomUser))

        user_serializer             = UserListSearialzer(user)

        assert user.id              == user_serializer.data.get('id')
        assert user.first_name      == user_serializer.data.get('first_name')
        assert user.last_name       == user_serializer.data.get('last_name')
        assert user.username        == user_serializer.data.get('username')
        assert user.email           == user_serializer.data.get('email')
    

    def test_register(self):
        """
        Ensure that user able to register
        """

        request_data = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email@gmail.com',
            'password': '1qwerty1234',
        }
        user_serializer             = UserCreateSerializer(data=request_data)
        if user_serializer.is_valid():
            pass
        else:
            message = ''
            for error in user_serializer.errors.values():
                message += " "
                message += error[0]
            print(message)
        
        user = CustomUser(username=request_data.get('username'), first_name=request_data.get('first_name'), last_name=request_data.get('last_name'), email=request_data.get('email'), password=request_data.get('password'))

        assert request_data.get('username') == user_serializer.data.get('username') 
        assert request_data.get('first_name') == user_serializer.data.get('first_name')
        assert request_data.get('last_name') == user_serializer.data.get('last_name')
        assert request_data.get('email') == user_serializer.data.get('email')
