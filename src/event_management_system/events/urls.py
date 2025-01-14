from django.urls import path

from . import views

urlpatterns = [ 
    # Events
    path('event/', views.event_overview, name='event_overview'),
    path('event/create/', views.event_create, name='event_create'),
    path('event/edit/<int:event_id>/', views.event_edit, name='event_edit'),
    path('event/delete/<int:event_id>/', views.event_delete, name='event_delete'),
    path('event/enable_call_for_papers/<int:event_id>/', views.enable_call_for_papers, name='enable_call_for_papers'),
    path('event/disable_call_for_papers/<int:event_id>/', views.disable_call_for_papers, name='disable_call_for_papers'),

    # Timeslots
    path('event/<int:event_id>/timeslot/', views.event_timeslot, name='event_timeslot'),
    path('event/<int:event_id>/timeslot/add/', views.event_timeslot_add, name='event_timeslot_add'),
    path('event/<int:event_id>/timeslot/remove/<int:index>/', views.event_timeslot_remove, name='event_timeslot_remove'),

    # Rooms
    path('room/', views.room_overview, name='room_overview'),
    path('room/create/', views.room_create, name='room_create'),
    path('room/edit/<int:room_id>/', views.room_edit, name='room_edit'),
    path('room/delete/<int:room_id>/', views.room_delete, name='room_delete'),

    # Lectures
    path('<int:event_id>/lecture/public/create/entry/', views.lecture_public_create_entry, name = 'lecture_public_create_entry'),
    path('<int:event_id>/lecture/public/create/', views.lecture_public_create, name = 'lecture_public_create'),
    path('<int:event_id>/lecture/overview/', views.lecture_overview, name = 'lecture_overview'),
    path('<int:event_id>/lecture/create/', views.lecture_create, name = 'lecture_create'),
    path('lecture/edit/<int:lecture_id>/', views.lecture_edit, name = 'lecture_edit'),
    path('lecture/delete/<int:lecture_id>/', views.lecture_delete, name = 'lecture_delete'),



]