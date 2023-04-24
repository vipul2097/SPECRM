from django.contrib.auth.models import User
from django.test import TestCase
from .models import Userprofile
from team.models import Team
# Create your tests here.

class UserprofileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
        self.team = Team.objects.create(name='Test Team', created_by=self.user)
        self.userprofile = Userprofile.objects.create(user=self.user, active_team=self.team)

    def test_userprofile_created(self):
        userprofile = Userprofile.objects.get(user=self.user)
        self.assertEqual(userprofile.active_team.name, 'Test Team')

    def test_active_team_can_be_updated(self):
        new_team = Team.objects.create(name='New Team', created_by=self.user)
        userprofile = Userprofile.objects.get(user=self.user)
        userprofile.active_team = new_team
        userprofile.save()
        self.assertEqual(userprofile.active_team.name, 'New Team')
