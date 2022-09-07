from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .models import (
    User as UserModel,
    ArtistApplication as ArtistApplicationModel
)

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def loginPage(request):
    return render(request, 'base/login.html')

def registerPage(request):
    return render(request, 'base/register.html')

# TODO: 이미 등록 신청한 유저를 방지하는 퍼미션 추가
@login_required
def artistApplyPage(request):
    return render(request, 'base/artist_apply.html')

def loginUser(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname', '')
        password = request.POST.get('password', '')

        user = authenticate(request, nickname=nickname, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '닉네임 / 비밀번호가 일치하지 않습니다.')

    return render(request, 'base/login.html')

@login_required
def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        user_exists = UserModel.objects.filter(nickname=nickname)

        if nickname == '':
            messages.error(request, '닉네임을 입력해 주세요.')
        elif password == '':
            messages.error(request, '비밀번호를 입력해 주세요.')
        elif password != password2:
            messages.error(request, '비밀번호가 일치하지 않습니다.')
        elif user_exists:
            messages.error(request, '이미 사용되고 있는 닉네임입니다.')
        else:
            UserModel.objects.create_user(nickname=nickname, password=password)
            return redirect('login_page')

        return render(request, 'base/register.html')

def artistApply(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        gender = request.POST.get('gender', '')
        date_of_birth = request.POST.get('date-of-birth', '')
        email = request.POST.get('email', '')
        phone_number = request.POST.get('phone', '')
        app_exists = ArtistApplicationModel.objects.filter(name=name)

        if len(name) > 16:
            messages.error(request, '성함은 16자를 초과할 수 없습니다.')
        elif name == '':
            messages.error(request, '성함을 입력해 주세요.')
        elif gender == '':
            messages.error(request, '성별을 선택해 주세요.')
        elif app_exists:
            messages.error(request, '이미 작가 등록을 신청하셨습니다.')
        else:
            ArtistApplicationModel.objects.create(
                name=name,
                gender=gender,
                email=email,
                date_of_birth=date_of_birth,
                phone_number=phone_number
            )

    return render(request, 'base/artist_apply.html')