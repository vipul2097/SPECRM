from django.contrib.auth.models import User
from django.test import TestCase
from team.models import Team
from .models import Lead, LeadFile, Comment

class LeadModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user and a team to be used in the tests
        user = User.objects.create(username='testuser')
        team = Team.objects.create(name='Test Team', created_by=user)

        # Create a lead
        Lead.objects.create(
            team=team,
            name='John Doe',
            email='johndoe@example.com',
            created_by=user,
        )

    def test_name_label(self):
        lead = Lead.objects.get(id=1)
        field_label = lead._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_email_max_length(self):
        lead = Lead.objects.get(id=1)
        max_length = lead._meta.get_field('email').max_length
        self.assertEqual(max_length, 254)

    def test_priority_default(self):
        lead = Lead.objects.get(id=1)
        default_priority = lead._meta.get_field('priority').default
        self.assertEqual(default_priority, 'medium')

class LeadFileModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user, a team, and a lead to be used in the tests
        user = User.objects.create(username='testuser')
        team = Team.objects.create(name='Test Team', created_by=user)
        lead = Lead.objects.create(
            team=team,
            name='John Doe',
            email='johndoe@example.com',
            created_by=user,
        )

        # Create a lead file
        LeadFile.objects.create(
            team=team,
            lead=lead,
            file='test.txt',
            created_by=user,
        )

    def test_file_label(self):
        lead_file = LeadFile.objects.get(id=1)
        field_label = lead_file._meta.get_field('file').verbose_name
        self.assertEqual(field_label, 'file')

    def test_file_upload_to(self):
        lead_file = LeadFile.objects.get(id=1)
        upload_to = lead_file._meta.get_field('file').upload_to
        self.assertEqual(upload_to, 'leadfiles')

class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a user, a team, and a lead to be used in the tests
        user = User.objects.create(username='testuser')
        team = Team.objects.create(name='Test Team', created_by=user)
        lead = Lead.objects.create(
            team=team,
            name='John Doe',
            email='johndoe@example.com',
            created_by=user,
        )

        # Create a comment
        Comment.objects.create(
            team=team,
            lead=lead,
            content='This is a test comment',
            created_by=user,
        )

    def test_content_label(self):
        comment = Comment.objects.get(id=1)
        field_label = comment._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_content_blank(self):
        comment = Comment.objects.get(id=1)
        blank = comment._meta.get_field('content').blank
        self.assertTrue(blank)
