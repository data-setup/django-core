# profiles/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm


@login_required
def profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user) # Remove [0]
    if created: 
        return redirect('profile_edit')  # Redirect if a new profile was created
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)


@login_required
def profile_edit(request):
    profile, created = Profile.objects.get_or_create(user=request.user) # Remove [0]
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'profiles/profile_edit.html', {'form': form})
