from django import forms
from django.forms.models import inlineformset_factory
from polls.models import Event, EventTicketType


class Register(forms.Form):
    name=forms.CharField(max_length=32,required=True,label='name', widget=forms.TextInput(attrs={'placeholder': 'name','required': ''}))
    lastName=forms.CharField(max_length=32,required=True,label='family name', widget=forms.TextInput(attrs={'placeholder': 'family name','required': ''}))
    gender = forms.ChoiceField(choices=[ ('', '----'),(1,'male'),(2,'female')],)
    #phoneNumber=forms.IntegerField(label='phone number'  ,  widget=forms.TextInput(attrs={'placeholder':'phone number','required': ''}))
    email=forms.EmailField(required=True,label='Email', widget=forms.TextInput(attrs={'placeholder': 'Email','required': ''}))
    userName=forms.CharField(max_length=32,required=True,label='username', widget=forms.TextInput(attrs={'placeholder': 'username','required': ''}))
    password=forms.CharField(max_length=32,required=True,label='password' , widget=forms.TextInput(attrs={'placeholder': 'passwprd','required': '','type': 'password'}),error_messages = {'invalid': 'Passwords do not match'})
    passwordRetype=forms.CharField(max_length=32,required=True,label='re-type password ', widget=forms.TextInput(attrs={'placeholder': 're-type password ','required': '','type': 'password'}))





class EventSubmit(forms.Form):
    subject=forms.CharField(max_length=32,required=True,label='subject', widget=forms.TextInput(attrs={'placeholder': 'subject','required': ''}))
    group=forms.ChoiceField(choices=[('', 'group'),(1,'music'),(2,'theater'),],)
    subgroup=forms.ChoiceField(choices=[('', 'subgroup'),(1,'pop'),(2,'metal'),(2,'country'),],)
    price=forms.IntegerField()
    ticketNumber=forms.IntegerField(label='ticket number ' , widget=forms.TextInput(attrs={'placeholder':' ticket number','required':''}))
    comments= forms.CharField(widget=forms.Textarea)

    image = forms.ImageField()

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('subject', 'description', 'category', 'subCategory', 'photo', 'date', 'finishDate', )

TicketTypeFormSet = inlineformset_factory(Event, EventTicketType, fields=('name', 'price', 'tickets'))
