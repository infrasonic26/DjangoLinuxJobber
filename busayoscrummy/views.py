from django.shortcuts import render
from django.http import HttpResponse
from busayoscrummy.models import ScrumyGoals,GoalStatus,ScrumyHistory
from busayoscrummy.models import SignupForm, CreateGoalForm
from django.contrib.auth.models import User, Group
import random

# Create your views here.

def index(request):
    form = SignupForm()
    if request.method == 'POST':
        form= SignupForm(request.POST)
        mygroup = Group.objects.get(name='Developer')
        mygroup.user_set.add(username)
        if form.is_valid():
            form.save()
            return redirect ("success")
    else:
        form = SignupForm()
    return render (request, 'busayoscrummy/index.html', {'form': form})

def success(request):
    return HttpResponse("Your account has been created successfully")

def move_goal(request, goal_id):
    try:
        obj = ScrumyGoals.objects.get(goal_id=goal_id)
    except Exception as e:
        return render(request, 'busayoscrummy/exception.html', {'error': 'A record with that goal id does not exist'})
    else:
        return HttpResponse(obj.goal_name)








def add_goal(request):
    form = CreateGoalForm()
    if request.method == 'POST':
        form = CreateGoalForm(request.POST)
    else:
        form = CreateGoalForm()
    return render(request, 'busayoscrummy/creategoal.html', {'form':form})




def home(request):
    user = User.objects.get(username='louis')
    goals = user.scrumygoals_set.all().values()
    week = GoalStatus.objects.get(status_name='Weekly Goal')
    all_week = week.scrumygoals_set.all().values()
    day = GoalStatus.objects.get(status_name='Daily Goal')
    all_day = day.scrumygoals_set.all().values
    context = {'week': all_week, 'day':all_day, 'user': user}
    return render(request,'busayoscrummy/home.html',context)

