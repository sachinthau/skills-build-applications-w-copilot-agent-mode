from django.core.management.base import BaseCommand
from octofit_tracker.models.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data (delete individually for Djongo compatibility)
        for obj in User.objects.all():
            if obj.id:
                obj.delete()
        for obj in Team.objects.all():
            if obj.id:
                obj.delete()
        for obj in Activity.objects.all():
            if obj.id:
                obj.delete()
        for obj in Leaderboard.objects.all():
            if obj.id:
                obj.delete()
        for obj in Workout.objects.all():
            if obj.id:
                obj.delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        users = [
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel),
            User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel),
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc),
            User.objects.create(name='Superman', email='superman@dc.com', team=dc),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc),
        ]

        # Create activities
        activities = [
            Activity.objects.create(user=users[0], type='Run', duration=30, calories=300),
            Activity.objects.create(user=users[1], type='Swim', duration=45, calories=400),
            Activity.objects.create(user=users[2], type='Bike', duration=60, calories=500),
            Activity.objects.create(user=users[3], type='Run', duration=25, calories=250),
            Activity.objects.create(user=users[4], type='Swim', duration=50, calories=450),
            Activity.objects.create(user=users[5], type='Bike', duration=70, calories=600),
        ]

        # Create workouts
        workouts = [
            Workout.objects.create(name='Cardio Blast', description='High intensity cardio workout'),
            Workout.objects.create(name='Strength Training', description='Build muscle and strength'),
        ]

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=1200)
        Leaderboard.objects.create(team=dc, points=1100)

        self.stdout.write(self.style.SUCCESS('Test data populated successfully.'))
