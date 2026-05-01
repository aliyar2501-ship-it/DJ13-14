# from django.urls import path
# from . import views
#
# app_name = 'tasks'
#
# urlpatterns = [
#     # --- Базовые страницы ---
#     path('', views.index, name='index'),
#     path('tasks/', views.task_list, name='task_list'),
#     path('tasks/<int:id>/', views.task_detail, name='task_detail'),
#
#     # --- CRUD ---
#     path('tasks/create/', views.task_create, name='task_create'),
#     path('tasks/<int:id>/update/', views.task_update, name='task_update'),
#     path('tasks/<int:id>/delete/', views.task_delete, name='task_delete'),
#
#     # --- Действия ---
#     path('tasks/<int:id>/complete/', views.task_complete, name='task_complete'),
#     path('tasks/<int:id>/uncomplete/', views.task_uncomplete, name='task_uncomplete'),
#
#     # --- Фильтрация ---
#     path('tasks/status/<str:status>/', views.tasks_by_status, name='tasks_by_status'),
#     path('tasks/priority/<int:priority>/', views.tasks_by_priority, name='tasks_by_priority'),
#
#     # --- Поиск ---
#     path('tasks/search/', views.task_search, name='task_search'),
#
#     # --- Категории ---
#     path('categories/', views.category_list, name='category_list'),
#     path('categories/<int:id>/', views.category_detail, name='category_detail'),
#     path('categories/create/', views.category_create, name='category_create'),
#
#     # --- API (JSON) ---
#     path('api/tasks/', views.api_task_list, name='api_task_list'),
#     path('api/tasks/<int:id>/', views.api_task_detail, name='api_task_detail'),
# ]


from django.urls import path, re_path
from . import views

app_name = 'tasks'

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/create/', views.task_create, name='task_create'),

    re_path(r'^tasks/(?P<id>\d+)/$', views.task_detail, name='task_detail'),
    re_path(r'^tasks/(?P<id>\d+)/update/$', views.task_update, name='task_update'),
    re_path(r'^tasks/(?P<id>\d+)/delete/$', views.task_delete, name='task_delete'),

    re_path(r'^tasks/(?P<id>\d+)/complete/$', views.task_complete, name='task_complete'),
    re_path(r'^tasks/(?P<id>\d+)/uncomplete/$', views.task_uncomplete, name='task_uncomplete'),

    re_path(r'^tasks/status/(?P<status>\w+)/$', views.tasks_by_status, name='tasks_by_status'),
    re_path(r'^tasks/priority/(?P<priority>\d+)/$', views.tasks_by_priority, name='tasks_by_priority'),

    re_path(r'^tasks/search/$', views.task_search, name='task_search'),

    re_path(r'^categories/(?P<id>\d+)/$', views.category_detail, name='category_detail'),

    re_path(r'^api/tasks/(?P<id>\d+)/$', views.api_task_detail, name='api_task_detail'),
]