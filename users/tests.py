from django.contrib.auth.middleware import get_user
from users.models import CustomUser
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        self.client.post(reverse('users:register'), data={
            'username': 'testuser',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'akmalusmonov446@gmail.com',
            'password': '1234',
        })
        user = CustomUser.objects.get(username='testuser')

        self.assertEqual(user.first_name, 'test')
        self.assertEqual(user.last_name, 'test')
        self.assertEqual(user.email, 'akmalusmonov446@gmail.com')
        self.assertTrue(user.password, ('1234'))

    def test_required_fields(self):
        response = self.client.post(reverse('users:register'), data={
            'first_name': 'test',
            'email': 'akmalusmonov446@gmail.com',
        })

        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)

        form = response.context['form']
        self.assertFormError(form, 'username', 'This field is required.')
        self.assertFormError(form, 'password', 'This field is required.')

    def test_invalid_email(self):
        response = self.client.post(reverse('users:register'), data={
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'invalid-email',
            'password': '1234',
        })

        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 0)
        form = response.context['form']
        self.assertFormError(form, 'email', 'Enter a valid email address.')

    def test_unique_username(self):
        # 1. Birinchi foydalanuvchini yaratamiz
        self.client.post(reverse('users:register'), data={
            'username': 'test',
            'first_name': 'Test',
            'last_name': 'User',
            'email': 'test1@example.com',
            'password': '1234',
        })

        # 2. Endi xuddi shu username bilan ikkinchi foydalanuvchini yaratamiz
        response = self.client.post(reverse('users:register'), data={
            'username': 'test',  # Takroriy username
            'first_name': 'Test2',
            'last_name': 'User2',
            'email': 'test2@example.com',
            'password': '1234',
        })

        # 3. Username allaqachon mavjudligi xatosini tekshiramiz
        form = response.context['form']
        self.assertFormError(form, 'username', 'A user with that username already exists.')

        # 4. Foydalanuvchilar soni 1 ta bo'lishi kerak
        user_count = CustomUser.objects.count()
        self.assertEqual(user_count, 1)

class LoginTestCase(TestCase):
    def setUp(self):
        self.db_user = CustomUser.objects.create_user(username='testuser', first_name='test',)
        self.db_user.set_password('1234')
        self.db_user.save()

    def test_successful_login(self):
        self.client.post(reverse('users:login'), data={
            'username': 'testuser',
            'password': '1234',
        })

        user = get_user(self.client)
        self.assertTrue(user.is_authenticated)

    def  test_wrong_credentials(self):
        self.client.post(reverse('users:login'), data={
            'username': 'wrong-username',
            'password': '1234',
        })

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

        self.client.post(reverse('users:login'), data={
            'username': 'wrong-username',
            'password': '1234',
        })
        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)

    def test_logout(self):
        self.client.login(username='testuser', password='1234')

        self.client.get(reverse('users:logout'))

        user = get_user(self.client)
        self.assertFalse(user.is_authenticated)



class ProfileTestCase(TestCase):
    def test_login_required(self):
        response = self.client.get(reverse('users:profile'))

        self.assertEqual(response.url, reverse('users:login') + '?next=/users/profile/')

    def test_profile_details(self):
        # 1. Foydalanuvchi yaratish
        user = CustomUser.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='somepassword'  # bu password login uchun ishlatiladi
        )

        # 2. Login qilish
        login_success = self.client.login(username='testuser', password='somepassword')
        self.assertTrue(login_success)

        # 3. Profile sahifasiga so‘rov yuborish
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)  # sahifa muvaffaqiyatli yuklangan

        # 4. Sahifada foydalanuvchi ma’lumotlari borligini tekshirish
        self.assertContains(response, user.username)
        self.assertContains(response, user.first_name)
        self.assertContains(response, user.last_name)
        self.assertContains(response, user.email)

    def test_profile_edit(self):
        user = CustomUser.objects.create_user(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            password='somepassword'  # bu password login uchun ishlatiladi
        )

        login_success = self.client.login(username='testuser', password='somepassword')
        self.assertTrue(login_success)

        response = self.client.post(
            reverse('users:profile_edit'),
            data={
                'username': 'testuser',
                'first_name': 'Test',
                'last_name': 'User',
                'email': 'testusser@gmail.com',
            }
        )
        user.refresh_from_db()

        self.assertEqual(user.email, 'testusser@gmail.com')
        self.assertEqual(response.url, reverse('users:profile'))





