from django import forms
from .models import Book, Comments, Meetup
class DateInput(forms.DateInput):
    input_type = 'date'

class BookForm(forms.ModelForm):
    '''
    Create a Book form. Uses all of the fields.
    '''
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            "year_published": DateInput()
        }


class CommentForm(forms.ModelForm):
    '''
    Create a member's Comment form. Only body field needs to be entered.
    '''
    class Meta:
        model = Comments
        fields = ('body',)


class MeetupForm(forms.ModelForm):
    '''
    Create a Meetup form. Uses all of the fields.
    '''
    class Meta:
        model = Meetup
        fields = '__all__'
