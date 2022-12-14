from django.contrib import admin
from .models import Book, Meetup


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    '''
    Define the Book fields shown in the admin panel.
    '''
    list_display = (
        'title', 'author', 'year_published', 'members_rating', 'has_been_read'
    )


@admin.register(Meetup)
class MeetupAdmin(admin.ModelAdmin):
    '''
    Define the Meetup fields shown in the admin panel.
    '''
    list_display = ('long_title', 'meetup_date', 'book1')
