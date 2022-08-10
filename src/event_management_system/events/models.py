from turtle import title
from zoneinfo import available_timezones
from django.db import models
from django.contrib.auth.models import User

TARGET_GROUP = [
    ('BE', 'Beginner'),
    ('IN', 'Intermediate'),
    ('PR', 'Professional'),
    ]

PRESENTATION_STYLE = [
    ('RE', 'Recorded'),
    ('LI', 'Live'),
    ]



class Event(models.Model):
    name = models.CharField(max_length=100)   
    year = models.IntegerField()
    website = models.URLField()

    # TODO TimeSlots (Datefield, vielleicht nur Strings :)) 
    # TODO Tracks / Rooms

class Room(models.Model):
    name = models.CharField(max_length=100)
    website = models.URLField()
    coordinates = models.CharField(max_length=100)


class Lecture(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    presentators = models.ManyToManyField(User, related_name="presentating")
    attendant = models.ForeignKey(User, on_delete=models.CASCADE, related_name="attending")
    title = models.CharField(max_length=100)   
    description = models.CharField(max_length=2048)   
    target_group = models.CharField(max_length=2, choices=TARGET_GROUP)
    available_timeslots = models.DateField()
    minimal_lecture_length = models.IntegerField() # (Minutes)
    maximal_lecture_length = models.IntegerField() # (Minutes)
    preferred_presentation_style = models.CharField(max_length=2, choices=PRESENTATION_STYLE)
    qualification_for_lecture = models.CharField(max_length=512)
    questions_during_lecture = models.BooleanField()
    questions_after_lecture = models.BooleanField()
    additional_information_by_presentator = models.CharField(max_length=2048) 
    scheduled_in_rooms = models.ManyToManyField(Room)
    scheduled_presentation_time = models.DateTimeField()
    scheduled_presentation_length = models.IntegerField() # (Minutes)
    scheduled_presentation_style = models.CharField(max_length=2, choices=PRESENTATION_STYLE)
    further_information = models.CharField(max_length=2048) 
    related_website = models.URLField()
    link_to_material = models.URLField()
    link_to_recording = models.URLField()

    def __str__(self):
        return f"{self.title}"