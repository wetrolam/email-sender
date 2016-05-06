from django.shortcuts import render

def profile(request):
    username = request.user.username if request.user.is_authenticated() else "neznamy pouzivatel"
    return render(request, 'accounts/profile.html', {'username': username})
