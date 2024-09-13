from django.contrib.auth import login
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from users.models import CustomUser


class UserRegistrationView(TemplateView):
    template_name = 'register.html'

class UserLoginView(TemplateView):
    template_name = 'login.html'

class UserMakeLoginView(View):
    """Вьюшка для логина пользователя"""

    def post(self, request, *args, **kwargs):
        data = request.POST
        email = data['email']
        password = data['password']

        user = CustomUser.objects.get(email=email)

        correct = user.check_password(password)

        if correct == True:
            login(request, user)
            return render(request, 'login.html', context={'logged_in': True})
        else:
            return render(request, 'login.html', context={'logged_in': False})

class UserMakeRegistrationView(View):
    """Вьюшка для регистрации пользователя"""

    def post(self, request, *args, **kwargs):
        data = request.POST

        password1 = data['password1']
        password2 = data['password2']

        if password1 == password2:
            first_name = data['first-name']
            last_name = data['last-name']
            email = data['email']
            user = CustomUser.objects.create_user(
                email=email, password=password1,
                first_name=first_name, last_name=last_name,
            )
            return render(request, 'index.html')
        else:
            # TODO: Отображать ошибку для пользоваетля об не схожести поролей
            pass
