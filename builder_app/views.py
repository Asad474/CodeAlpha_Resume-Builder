from django.shortcuts import render, redirect
from django.contrib.auth import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from .models import MyUser
from .forms import *

# Create your views here.
def home(request):
    return render(request, 'builder_app/index.html')


@unauthenticated_user
def loginuser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        valuenext= request.GET.get('next')

        try:
            user = authenticate(request, email = email, password = password)
            login(request, user)
            if valuenext == '' or valuenext == None:
                return redirect('home')
            
            return redirect(valuenext)

        except:
            messages.error(request, 'Email or Password is invalid!!!')

    return render(request, 'builder_app/login.html')


def logoutuser(request):
    logout(request)
    return redirect('home')


@unauthenticated_user
def register(request):
    form = SignUpForm()

    try:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid:                
                user = form.save(commit = False)
                form.save()
                messages.success(request, f'Hi {user.username}, thank you for registering!!!')
                return redirect('loginuser')

    except:
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        all_users_username = MyUser.objects.all().values('username')
        all_users_email = MyUser.objects.all().values('email')

        if {'username' : username} in all_users_username:
            messages.error(request, f'User with username "{username}" already exists!!!')

        elif {'email' : email} in all_users_email:
            messages.error(request, 'User with this email id already exists!!!')    

        elif password1 != password2:
            messages.error(request ,'Password and Confirm Password are not matching with each other!!!')

        else:
            messages.error(request ,'Something went wrong!!!')    

        return redirect('register')

    context={'form' : form}
    return render(request,'builder_app/register.html',context)


@login_required(login_url = 'loginuser')
def resumeform(request):
    if UserProfile.objects.filter(user = request.user):
        return redirect('updateresume')

    userprofile_form = UserProfileForm()
    skill_form_set = SkillFormSet()
    education_form_set = EducationFormSet()
    experience_form_set = ExperienceFormSet()
    project_form_set = ProjectFormSet()

    if request.method == 'POST':
        userprofile_form = UserProfileForm(request.POST, request.FILES)
        skill_form_set = SkillFormSet(request.POST)
        education_form_set = EducationFormSet(request.POST)
        experience_form_set = ExperienceFormSet(request.POST)
        project_form_set = ProjectFormSet(request.POST)

        if userprofile_form.is_valid() and skill_form_set.is_valid() and education_form_set.is_valid() and experience_form_set.is_valid() and project_form_set.is_valid():
            userprofile = userprofile_form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()

            for skill_form in skill_form_set:
                skill = skill_form.save(commit=False)
                skill.userprofile = userprofile
                skill.save()

            for education_form in education_form_set:
                education = education_form.save(commit=False)
                education.userprofile = userprofile
                education.save()

            for experience_form in experience_form_set:
                experience = experience_form.save(commit=False)
                experience.userprofile = userprofile
                experience.save()

            for project_form in project_form_set:
                project = project_form.save(commit=False)
                project.userprofile = userprofile
                project.save()


            return redirect('resume')

    context = {
        'userprofile_form': userprofile_form,
        'skill_formset': skill_form_set,
        'education_formset': education_form_set,
        'experience_formset': experience_form_set,
        'project_formset': project_form_set
    }

    return render(request, 'builder_app/resumeform.html', context)


@login_required(login_url='loginuser')
def updateresume(request):
    userprofile = UserProfile.objects.get(user = request.user)
    userprofile_form = UserProfileForm(instance=userprofile)
    skill_form_set = SkillFormSet(instance=userprofile)
    education_form_set = EducationFormSet(instance=userprofile)
    experience_form_set = ExperienceFormSet(instance=userprofile)
    project_form_set = ProjectFormSet(instance=userprofile)

    if request.method == 'POST':
        userprofile_form = UserProfileForm(request.POST, request.FILES, instance=userprofile)

        if userprofile_form.is_valid():
            updated_userprofile = userprofile_form.save()

            skill_form_set = SkillFormSet(request.POST, instance=updated_userprofile)
            education_form_set = EducationFormSet(request.POST, instance=updated_userprofile)
            experience_form_set = ExperienceFormSet(request.POST, instance=updated_userprofile)
            project_form_set = ProjectFormSet(request.POST, instance=updated_userprofile)

            if skill_form_set.is_valid() and education_form_set.is_valid() and experience_form_set.is_valid() and project_form_set.is_valid():
                skill_form_set.save()
                education_form_set.save()
                experience_form_set.save()
                project_form_set.save()
            
            return redirect('resume')
        else:
            print('Something went wrong..')

    context = {
        'userprofile_form': userprofile_form,
        'skill_formset': skill_form_set,
        'education_formset': education_form_set,
        'experience_formset': experience_form_set,
        'project_formset': project_form_set
    }

    return render(request, 'builder_app/resumeform.html', context)


@login_required(login_url = 'loginuser')
def resume(request):
    userprofile = request.user.userprofile
    context = {'userprofile': userprofile}
    return render(request, 'builder_app/resume.html', context)    