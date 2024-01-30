from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from .models import Mark, Modelo
# Create your tests here.

class ModeloTest(TestCase):
    @classmethod
    def setUpTestData(clase):
        clase.modelo = Modelo.objects.create(
            mark = Mark.objects.create(descript = "Toyota"),
            descript = "Rush"

        )
        clase.user = get_user_model().objects.create_user(
            username = "test",
            email = "test@mail.com",
            first_name="test",
            password="ozymandias2795"
        )

        clase.ver_modelo=Permission.objects.get(
            codename = "view_modelo"

        )

    def test_lista(self):
        self.assertEqual(self.modelo.descript,"Rush")
        self.assertEqual(self.modelo.mark.descript,"Toyota")

    def test_vista_modelo_logout(self):
        self.client.logout()
        response = self.client.get(reverse("control:modelo_list"))
        self.assertEqual(response.status_code,302)


    def test_vista_modelo_usuario_autenticado(self):
        self.client.login(email="test@mail.com",password="ozymandias2795")
        self.user.user_permissions.add(self.ver_modelo)
        response = self.client.get(reverse("control:modelo_list"))
        #print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code,200)
        #self.assertContains(response,"Rush")
        self.assertTemplateUsed(response,"ctrl_comb/modelo.html")

    def test_vista_marca_logout(self):
        self.client.logout()
        response = self.client.get(reverse("control:mark_list"))
        self.assertEqual(response.status_code,302)

    def test_vista_marca_usuario_autenticado(self):
        self.client.login(email="test@mail.com",password="ozymandias2795")
        response = self.client.get(reverse("control:mark_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Toyota")
        self.assertTemplateUsed(response,"ctrl_comb/mark.html")



    def test_vista_modal(self):
        response = self.client.get(reverse("control:modelo_edit_modal",kwargs={'pk':self.modelo.id}))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Toyota")
        self.assertTemplateUsed(response,"ctrl_comb/modelo_modal.html")

    def test_vista_modal(self):
        response = self.client.get(reverse("control:modelo_new_modal",kwargs={'mark':'Toyota','modelo':'Rush'}))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Rush")
        self.assertTemplateUsed(response,"ctrl_comb/modelo_modal.html")     
