from django.shortcuts import render

#prihlaseny
def profile(request):
    username = request.user.username if request.user.is_authenticated() else "neznamy pouzivatel"
    return render(request, 'accounts/profile.html', {'username': username})

#neprihlaseny
def create_account(request):
    return render(request, 'accounts/create.html')