from filecmp import clear_cache
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.decorators.cache import never_cache
from . models import list1

# Create your views here.


dic={'list1':list1}
@login_required()
@never_cache
def home(request):
    return render(request,'home.html',dic)
# def logout(request):
#     request.session.flush()
#     return redirect('login')
