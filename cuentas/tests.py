from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class PruebasPaginaRegistro(TestCase):
  def test_url_registro_existe_en_ubicacion_correcta(self):
    respuesta = self.client.get('/cuentas/registro/')
    self.assertEqual(respuesta.status_code, 200)
    
  def test_nombre_vista_registro(self):
    respuesta = self.client.get(reverse('signup'))
    self.assertEqual(respuesta.status_code, 200)
    self.assertTemplateUsed(respuesta, 'registration/signup.html')
    
  def test_formulario_registro(self):
    respuesta = self.client.post(
      reverse('signup'),
      {
        'username': 'usuarioprueba',
        'email': 'usuarioprueba@email.com',
        'password1': 'pruebasecreta123',
        'password2': 'pruebasecreta123',
      }
    )
    self.assertEqual(respuesta.status_code, 302)
    self.assertEqual(get_user_model().objects.all().count(), 1)
    self.assertEqual(get_user_model().objects.all()[0].username, 'usuarioprueba')
    self.assertEqual(get_user_model().objects.all()[0].email, 'usuarioprueba@email.com')
    