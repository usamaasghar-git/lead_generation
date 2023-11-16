from django.shortcuts import render, get_object_or_404, redirect
from .models import CustomUser
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page after successful form submission
            return redirect('success_page')
        else:
            # Handle form validation errors
            return render(request, 'signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_detail.html', {'user': user})
def dashboard(request):
    return render(request, 'base.html', {'user': request.user})