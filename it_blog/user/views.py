from django.shortcuts import render
from user.forms import UserSignIn, UserLogIn
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout as log_out
from django.contrib.auth.decorators import login_required


# def signin(request):
#     context = { "signin_form": UserSignIn() }
#     if request.method == "POST":
#         user_form = UserSignIn(request.POST)
#         if user_form.is_valid():
#             user_form.save()
#             return redirect("login_page")
#         context.update(signin_form=user_form)
#     return render(request, "sign_in.html", context)


def login(request):
    if not request.user.is_anonymous:
        return redirect("home_page")
    context = { "login_form": UserLogIn() }
    if request.method == "POST":
        user_form = UserLogIn(request.POST)
        if user_form.is_valid():
            user_form.login(request)
            return redirect("home_page")
        context.update(login_form=user_form)
    return render(request, "login.html", context)

@login_required(login_url="login_page")
def logout(request):
    log_out(request)
    return redirect("home_page")


class Registration(View):
    form_class = UserSignIn
    template_name = "sign_in.html"
    context = {}

    def get(self, request, *args, **kwargs):
        self.context.update(signin_form = self.form_class())
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login_page")
        self.context.update(signin_form = form)
        return render(request, self.template_name, self.context)