from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Create test users
        john = User.objects.create(email='john.doe@example.com', name='John Doe')
        jane = User.objects.create(email='jane.smith@example.com', name='Jane Smith')

        # Create test teams
        Team.objects.create(name='Team Alpha')
        Team.objects.create(name='Team Beta')

        # Create test activities
        Activity.objects.create(user=john, type='Running', duration=30)
        Activity.objects.create(user=jane, type='Walking', duration=45)

        # Create test leaderboard entries
        Leaderboard.objects.create(team=Team.objects.get(name='Team Alpha'), points=100)
        Leaderboard.objects.create(team=Team.objects.get(name='Team Beta'), points=80)

        # Create test workouts
        Workout.objects.create(name='Morning Run', description='A quick morning run to start the day.')
        Workout.objects.create(name='Evening Yoga', description='Relaxing yoga session in the evening.')

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with test data'))
