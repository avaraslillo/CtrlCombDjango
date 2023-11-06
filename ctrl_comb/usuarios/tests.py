from django.test import TestCase
from django.contrib.auth import get_user_model



# Create your tests here.

class CustomUserTests(TestCase):
    def test_crear_usuario(self):
        User = get_user_model()
        usr = User.objects.create_user(
            username = "debsconsultores",
            email = "debsconsultores@gmail.com",
            password = "ozymandias2795"
        )

    #Qué esperamos

        self.assertEqual(usr.username,"debsconsultores")
        self.assertEqual(usr.email,"debsconsultores@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertFalse(usr.is_staff)
        self.assertFalse(usr.is_superuser)

    def test_crear_superusuario(self):
        User = get_user_model()
        usr = User.objects.create_superuser(
            username = "debsconsultores",
            email = "debsconsultores@gmail.com",
            password = "ozymandias2795"
        )

    #Qué esperamos

        self.assertEqual(usr.username,"debsconsultores")
        self.assertEqual(usr.email,"debsconsultores@gmail.com")
        self.assertTrue(usr.is_active)
        self.assertTrue(usr.is_staff)
        self.assertTrue(usr.is_superuser)      
