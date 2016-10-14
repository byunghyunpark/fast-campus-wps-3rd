from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth import login as auth_login
from django.contrib import messages


def login(request):
    next = request.GET.get('next')
    if request.method == "POST":
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = auth_authenticate(username=username, password=password)
        except KeyError:
            return HttpResponse('username과 password는 필수항목입니다')

        if user is not None:
            auth_login(request, user)
            messages.success(request, "로그인 성공")
            return redirect(next)
        else:

            messages.error(request, "로그인 실패")
            return render(request, 'member/login.html', {})
    else:
        return render(request, 'member/login.html', {})
