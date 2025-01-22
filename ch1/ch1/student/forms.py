from django import forms


class Registration(forms.Form):
    # UnderScore becomes " " in forms
    first_name = forms.CharField(
        min_length=3
    )
    last_name = forms.CharField()
    email = forms.EmailField()
    city = forms.CharField()

    #validating specific field in django

    # def clean_first_name(self):
    #     # self.cleaned_data.get('name')
    #     first_name = self.cleaned_data['first_name']
    #     print(first_name)
    #     if len(first_name) < 4 :
    #         raise forms.ValidationError('Enter more than or equal 4 charecters')
    #     return first_name
    #     # if len(last_name) < 4 :
    #     #     raise forms.ValidationError('Enter more than or equal 4 charecters')
    #     # else:
    #     #     return last_name
    #     # last_name = self.cleaned_data['last_name']
    #     # email = self.cleaned_data['email']
    #     # city = self.cleaned_data['city']

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        email = cleaned_data.get('email')
        city = cleaned_data.get('city')
        if first_name and len(first_name) < 4:
            self.add_error('first_name','Enter more than or equal 4 charecter')
        if last_name and len(last_name) < 4:
            self.add_error('first_name','Enter more than or equal 4 charecter')
        if email and len(email) < 10:
            self.add_error('first_name','Enter more than or equal 4 charecter')
        if city and len(city) < 4:
            self.add_error('first_name','Enter more than or equal 4 charecter')
        print(cleaned_data)
        return cleaned_data
    
class loginn(forms.Form):
    # UnderScore becomes " " in forms
    email = forms.EmailField()
    password = forms.CharField()


class Address(forms.Form):
    name = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    pin_code = forms.IntegerField()


class Test(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


from django import forms

class DemoForm(forms.Form):
    # Basic Details
    name = forms.CharField(
        label="Full Name",
        max_length=100, 
        label_suffix=":",
        min_length=3,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Full Name',
            'class': 'mycss'
        })
    )

    email = forms.EmailField(
        label="Email",
        label_suffix=":",
        disabled=True,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Enter Email',
            'class': 'mycss'
        })
    )

    pin_code = forms.IntegerField(
        label="Pin Code",
        label_suffix=":",
        min_value=100000,
        max_value=999999,
        error_messages={
            'min_value': 'Pin code must be at least 6 digits',
            'max_value': 'Pin code can be at most 6 digits'
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter the pin code',
            'class': 'mycss'
        })
    )

    # Personal Details
    age = forms.FloatField(
        label="Age",
        min_value=0,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your age',
            'class': 'mycss'
        })
    )

    date_of_birth = forms.DateField(
        label="Date of Birth",
        required=False,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'placeholder': 'dd-mm-yyyy'
        })
    )

    appointment_time = forms.TimeField(
        label="Appointment Time",
        required=False,
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'placeholder': 'HH:MM'
        })
    )

    appointment_datetime = forms.DateTimeField(
        label="Appointment Date & Time",
        required=False,
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'placeholder': 'yyyy-mm-ddTHH:MM'
        })
    )

    is_subscribed = forms.BooleanField(
        label="Subscribe to Newsletter",
        required=False,
    )

    agree_terms = forms.NullBooleanField(
        label="Do you agree with Terms?"
    )

    gender = forms.ChoiceField(
        label="Gender",
        choices=[
            ('M', 'Male'),
            ('F', 'Female'),
            ('O', 'Other')
        ]
    )

    interests = forms.MultipleChoiceField(
        label="Interests",
        choices=[
            ('tech', 'Technology'), 
            ('art', 'Art'), 
            ('sports', 'Sports')
        ]
    )

    # File and URL Field
    profile_image = forms.ImageField(
        label="Profile Image",
        required=False
    )

    resume = forms.FileField(
        label="Upload Resume",
        required=False
    )

    websites = forms.URLField(
        label="Personal Websites",
        required=False,
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. https://'
        })
    )

    # Other Fields
    phone_number = forms.RegexField(
        label="Phone Number",
        regex=r'^\+?1?\d{9,15}$',
        error_messages={
            'invalid': 'Enter a valid phone number, e.g.: +123456789'
        },
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter Phone Number',
            'class': 'mycss'
        })
    )

    password = forms.CharField(
        label="Password",
        max_length=50,
        min_length=8,
        error_messages={
            'min_length': 'Password must be at least 8 characters long'
        },
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter Password',
            'class': 'mycss'
        })
    )

    slug = forms.SlugField(
        label="Slug",
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your slug',
            'class': 'mycss'
        })
    )

    ip_address = forms.GenericIPAddressField(
        label="IP Address",
        protocol='both',
        unpack_ipv4=False,
        localize=True
    )

    rating = forms.DecimalField(
        label="Ratings",
        max_digits=3,
        decimal_places=1,
        min_value=0,
        max_value=10,
        initial=5.0,
        localize=True
    )
