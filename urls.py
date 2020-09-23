from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView



urlpatterns = [
    path('',LoginView.as_view(redirect_authenticated_user=True),name='login'),
    path('register',views.Register.as_view(),name='register'),
    path('projects',views.EmptyProject.as_view()),
    path('profile',views.Profile.as_view()),
    path('all',views.AllUsers.as_view()),
    path('logout',LogoutView.as_view()),
    path('<username>',views.ProfilePage.as_view()),
    path('<username>/settings',views.ProfileSettings.as_view()),
    path('projects/all',views.AllProjects.as_view()),
    path('projects/create_project',views.ProjectCreation.as_view()),
    path('projects/<slug>',views.Project.as_view()),
    path('projects/<slug>/settings',views.ProjectSettings.as_view()),
    path('projects/<slug>/settings/add_part',views.AddingParts.as_view()),
    path('projects/<slug>/settings/update',views.UpdateParts.as_view()),
    path('projects/<slug>/comment',views.AddingComment.as_view()),
    path('projects/<slug>/lyrics',views.Lyrics.as_view()),
    path('projects/<slug>/stk/add',views.AddSoundtrack.as_view())
]
