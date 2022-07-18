from django.db import models
from django.forms import ModelForm
from django.db.models.deletion import PROTECT
from django.contrib.auth.models import User

# Create your models here.
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=150)
    def __str__(self):
        return self.status_name

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=150)
    goal_id = models.IntegerField(primary_key=True)
    created_by = models.CharField(max_length=150)
    moved_by = models.CharField(max_length=150)
    owner = models.CharField(max_length=150)
    goal_status = models.ForeignKey(GoalStatus, on_delete=PROTECT)
    user = models.ForeignKey(User, on_delete=PROTECT)
    def __str__(self):
        return self.goal_name



class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=150)
    created_by = models.CharField(max_length=150)
    moved_from = models.CharField(max_length=150)
    moved_to = models.CharField(max_length=150)
    time_of_action = models.CharField(max_length=150)
    goal = models.ForeignKey(ScrumyGoals, on_delete = PROTECT)

    def __str__ (self):
        return self.created_by

class SignupForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class CreateGoalForm (ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']
