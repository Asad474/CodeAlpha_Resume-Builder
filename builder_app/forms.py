from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username' : TextInput(attrs = {'placeholder' : 'Enter Username'}),
            'email' : EmailInput(attrs = {'placeholder' : 'Enter Email'}),
        }

    def __init__(self, *args, **kwargs) -> None:
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget = PasswordInput(attrs = {'placeholder' : 'Enter Password'})
        self.fields['password2'].widget = PasswordInput(attrs = {'placeholder' : 'Enter Confirm Password'})


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
        widgets = { 
            'first_name': TextInput(attrs = {'placeholder': 'eg: John', 'id': 'first_name'}),
            'last_name': TextInput(attrs = {'placeholder': 'eg: Walker', 'id': 'last_name'}),
            'designation': TextInput(attrs = {'placeholder': 'eg: Product Manager', 'id': 'designation'}),
            'address': TextInput(attrs = {'placeholder': 'eg: Lake Street-23', 'id': 'address'}),
            'phone': TextInput(attrs = {'placeholder': 'eg: +91 9832713421'}),
            'linkedin': URLInput(attrs = {'placeholder': 'Your linkedin url', 'id': 'linkedin'}),
            'github': URLInput(attrs = {'placeholder': 'Your github url', 'id': 'github'}),
            'career_objective': Textarea(attrs = {'cols': '40', 'rows' : '10'})
        }


class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = [ 'skill']
        widgets = {
            'skill': TextInput(attrs = {'placeholder': 'eg: Web Design', 'id': 'skill'})
        }


class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ['userprofile']
        widgets = {
            'start_year': DateInput(attrs = {'id': 'start_year'}),
            'end_year': DateInput(attrs = {'id': 'end_year'}),
            'education': TextInput(attrs = {'placeholder': 'eg: B.Arch'}),
            'institute': TextInput(attrs = {'placeholder': 'eg: JMI/AMU'})
        }


class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ['userprofile']
        widgets = {
            'start_date': DateInput(attrs = {'id': 'start_date', 'type': 'date'}),
            'end_date': DateInput(attrs = {'id': 'end_date', 'type': 'date'}),
            'position': TextInput(attrs = {'placeholder': 'eg: Software Developer', 'id': 'position'}),
            'company': TextInput(attrs = {'placeholder': 'eg: Google', 'id': 'company'}),
            'description': Textarea(attrs = {
                'placeholder': 'As a Sales Representative for XYZ Company, I successfully surpassed the annual revenue target by 20 percent in the fiscal year 2022...',
                'rows': '10',
                'cols': '30',
                'id': 'description'
            })
        }


class ProjectForm(ModelForm):
    class Meta:
        model = Project 
        exclude = ['project']
        widgets = {
            'title': TextInput(attrs = {'id': 'title'}),
            'description': Textarea(attrs = {'id': 'description', 'rows': '10', 'cols': '10'}),
            'link1': URLInput(attrs = {'id': 'link1'}),
            'link2': URLInput(attrs = {'id': 'link2'})
        }

SkillFormSet = inlineformset_factory(UserProfile, Skill, form = SkillForm, extra=1)        
EducationFormSet = inlineformset_factory(UserProfile, Education, form = EducationForm, extra=1)
ExperienceFormSet = inlineformset_factory(UserProfile, Experience, form = ExperienceForm, extra=1)
ProjectFormSet = inlineformset_factory(UserProfile, Project, form = ProjectForm, extra=1)