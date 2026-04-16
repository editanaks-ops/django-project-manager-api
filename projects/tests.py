from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Project


class ProjectAccessTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='admin1', password='12345test')
        self.manager_user = User.objects.create_user(username='manager1', password='12345test')
        self.regular_user = User.objects.create_user(username='user1', password='12345test')

        self.admin_user.profile.role = 'admin'
        self.admin_user.profile.save()

        self.manager_user.profile.role = 'manager'
        self.manager_user.profile.save()

        self.regular_user.profile.role = 'user'
        self.regular_user.profile.save()

        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description'
        )

    def test_project_list_requires_login(self):
        response = self.client.get(reverse('project_list'))
        self.assertRedirects(response, '/users/login/?next=/projects/')

    def test_admin_can_open_create_project(self):
        self.client.login(username='admin1', password='12345test')
        response = self.client.get(reverse('create_project'))
        self.assertEqual(response.status_code, 200)

    def test_regular_user_cannot_open_create_project(self):
        self.client.login(username='user1', password='12345test')
        response = self.client.get(reverse('create_project'))
        self.assertEqual(response.status_code, 403)
