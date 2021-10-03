from django.shortcuts import render
from user.forms import UserSignIn
from django.shortcuts import redirect


def signin(request):
    context = { "signin_form": UserSignIn() }
    if request.method == "POST":
        user_form = UserSignIn(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login_page")
            ...
        context.update(signin_form=user_form)
    return render(request, "sign_in.html", context)


def login(request):
    return render(request, "home.html", {})