from django.contrib.auth.models import User
from django.test import TestCase
from team.models import Team
from .models import Client, Comment, ClientFile

class ModelsTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team', created_by=self.user)
        self.client = Client.objects.create(team=self.team, name='Test Client', email='testclient@example.com', created_by=self.user)
        self.comment = Comment.objects.create(team=self.team, client=self.client, content='Test Comment', created_by=self.user)
        self.client_file = ClientFile.objects.create(team=self.team, client=self.client, created_by=self.user)

    def test_client_created(self):
        client = Client.objects.get(name='Test Client')
        self.assertEqual(client.email, 'testclient@example.com')

    def test_comment_created(self):
        comment = Comment.objects.get(content='Test Comment')
        self.assertEqual(comment.client.name, 'Test Client')

    def test_client_file_created(self):
        client_file = ClientFile.objects.get()
        self.assertIsNotNone(client_file.file)


