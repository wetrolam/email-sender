from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User


# def profile(request):
#     username = request.user.username if request.user.is_authenticated() else "neznamy pouzivatel"
#     return render(request, 'accounts/profile.html', {'username': username})

#prihlaseny
class AccountProfileView(generic.UpdateView):
    model = User
    fields = ['email']
    heading = 'User profile'
    template_name = 'accounts/profile.html'
    success_url = '/emails/'

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.id)


#neprihlaseny
def create_account(request):
    return render(request, 'accounts/create.html')
