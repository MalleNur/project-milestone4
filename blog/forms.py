from django import forms
from .models import Book, Comments, Meetup
# from django.forms.extras.widgets import SelectDateWidget
class DateInput(forms.DateInput):
    input_type = 'date'



class BookForm(forms.ModelForm):
    '''
    Create a Book form. Uses all of the fields.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #Change date field's widget here
        self.fields['year_published'].widget = DateInput()
    class Meta:
        model = Book
        fields = ['title','author','year_published','synopsis','cover_image','members_rating','is_shortlisted']
        
    




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
