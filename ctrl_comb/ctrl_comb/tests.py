from django.test import TestCase
from django.urls import reverse

from .models import Mark, Modelo
# Create your tests here.

class ModeloTest(TestCase):
    @classmethod
    def setUpTestData(clase):
        clase.modelo = Modelo.objects.create(
            mark = Mark.objects.create(descript = "Toyota"),
            descript = "Rush"

        )

    def test_lista(self):
        self.assertEqual(self.modelo.descript,"Rush")
        self.assertEqual(self.modelo.mark.descript,"Toyota")

    def test_vista_modelo(self):
        response = self.client.get(reverse("control:modelo_list"))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Rush")
        self.assertTemplateUsed(response,"ctrl_comb/modelo.html")

    def test_vista_modelo(self):
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
        response = self.client.get(reverse("control:modelo_new_modal",kwargs={'mark':'Suzuki','modelo':'Baleno'}))
        self.assertEqual(response.status_code,200)
        self.assertContains(response,"Baleno")
        self.assertTemplateUsed(response,"ctrl_comb/modelo_modal.html")     
