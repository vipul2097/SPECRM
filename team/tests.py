from django.contrib.auth.models import User
from django.test import TestCase
from .models import Plan, Team
# Create your tests here.

class PlanTestCase(TestCase):
    def setUp(self):
        Plan.objects.create(name='Basic', price=10, max_leads=50, max_clients=10)
        Plan.objects.create(name='Premium', price=20, description='Best value', max_leads=100, max_clients=20)

    def test_plans_exist(self):
        basic_plan = Plan.objects.get(name='Basic')
        premium_plan = Plan.objects.get(name='Premium')
        self.assertEqual(basic_plan.max_leads, 50)
        self.assertEqual(premium_plan.max_clients, 20)

class TeamTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username='user1', password='password1')
        user2 = User.objects.create_user(username='user2', password='password2')
        plan1 = Plan.objects.create(name='Basic', price=10, max_leads=50, max_clients=10)
        self.team = Team.objects.create(name='My Team', plan=plan1, created_by=user1)
        self.team.members.add(user1, user2)

    def test_team_created(self):
        team = Team.objects.get(name='My Team')
        self.assertEqual(team.plan.name, 'Basic')
        self.assertEqual(team.created_by.username, 'user1')
        self.assertEqual(team.members.count(), 2)

