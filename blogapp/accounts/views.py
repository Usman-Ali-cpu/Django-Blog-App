from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

# Create your views here.



def login_view(request):
    """
    it takes request as input and returns the HTML as a response
    """
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password=password)
        print(user)
        if user is None:
            context = {"error": "Invalid Credentials"}
            print("User is not authenticated")
            return render(request, "accounts/login.html", context=context)
        print("***************************************************************")
        login(request, user)
        return redirect('/')
    return render(request, "accounts/login.html", {})


def logout_view(request):
    """
    it takes request as input and returns the HTML as a response
    """
    if request.method == "POST":
        logout(request)
        return redirect('/login')
    return render(request, "accounts/logout.html", {})


def register_view(request):
    """
    it takes request as input and returns the HTML as a response
    """
    return render(request, "accounts/register.html", {})