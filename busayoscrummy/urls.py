from django.urls import path, include
from busayoscrummy import views

urlpatterns = [
    path('index/', views.index, name='about'),
    path('movegoal/<int:goal_id>', views.move_goal, name="move_goal"),
    path('addgoal/', views.add_goal, name="addgoal"),
    path('home/', views.home),
    path('accounts/', include('django.contrib.auth.urls'))
]
