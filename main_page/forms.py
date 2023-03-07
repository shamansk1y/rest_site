from django import forms
from main_page.models import Subscription, ContactUs, FastBooking


class ContactUsForm(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "name",
                'placeholder': "Your Name"
            }))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "email",
                'class': "form-control border-0",
                'id': "email",
                'placeholder': "Your Email"
            }))

    subject = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "subject",
                'placeholder': "Subject"
            }))


    message = forms.CharField(
        max_length=300,
        widget=forms.Textarea(
            attrs={
                'class': "form-control border-0",
                'placeholder': "Leave a message here",
                'id': "message",
                'style': "height: 100px"
            }))

    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']


class FastBookingForm(forms.ModelForm):
    PEOPLE_CHOICES = (
        (1, 'people 1'),
        (2, 'people 2'),
        (3, 'people 3'),
        (4, 'people 4'),
        (5, 'people 5'),
        (6, 'people 6'),
    )


    name_1 = forms.CharField(
        min_length=2,
        max_length=50,
        widget=forms.TextInput(
            attrs={
                'type': "text",
                'class': "form-control border-0",
                'id': "gname",
                'placeholder': "Gurdian Name",
                }))

    email_1 = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'type': "email",
                'class': "form-control border-0",
                'id': "gmail",
                'placeholder': "Gurdian Email"
            }))
    reservation_date_1 = forms.DateTimeField(
        label='Day and time booking',
        widget=forms.TextInput(attrs={
            'type': "text",
            'class': "form-control datetimepicker-input",
            'id': "datetime",
            'placeholder': "Date & Time",
            'data-target': "#date3",
            'data-toggle': "datetimepicker",
        })
    )

    number_of_people_1 = forms.ChoiceField(choices=PEOPLE_CHOICES,
    widget=forms.Select(attrs={
            'class': 'form-control',
            'id': 'number-of-people'}))

    message_1 = forms.CharField(
        max_length=250,
        widget=forms.Textarea(
            attrs={
                'class': "form-control border-0",
                'placeholder': "Leave a message here",
                'id': "message",
                'style': "height: 100px",
                "message": 'Message'
            }))

    class Meta:
        model = FastBooking
        fields = ['name_1', 'email_1', 'reservation_date_1', 'number_of_people_1', 'message_1', 'is_processed_1']


class SubscriptionForm(forms.ModelForm):


    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
    'class': "form-control border-primary w-100 py-3 ps-4 pe-5",
    'type': "text",
    'placeholder': "Your email",
            }))

    class Meta:
        model = Subscription
        fields = ['email']