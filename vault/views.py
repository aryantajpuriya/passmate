from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PasswordEntryForm
from .models import PasswordEntry
from django.shortcuts import get_object_or_404

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def add_password(request):
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST)
        if form.is_valid():
            password_entry = form.save(commit=False)
            password_entry.user = request.user  # assign the logged-in user
            password_entry.save()
            return redirect('password_list')  # we’ll build this next
    else:
        form = PasswordEntryForm()
    return render(request, 'vault/add_password.html', {'form': form})

@login_required
def password_list(request):
    if request.user.is_authenticated:
        passwords = PasswordEntry.objects.filter(user=request.user)
    else:
        passwords = []
   
    print("User:", request.user)
    print("Passwords:", passwords)
    return render(request, 'vault/password_list.html', {'passwords': passwords})

@login_required
def edit_password(request, pk):
    entry = get_object_or_404(PasswordEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        form = PasswordEntryForm(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('password_list')
    else:
        form = PasswordEntryForm(instance=entry)
    return render(request, 'vault/edit_password.html', {'form': form})

@login_required
def delete_password(request, pk):
    entry = get_object_or_404(PasswordEntry, pk=pk, user=request.user)
    if request.method == 'POST':
        entry.delete()
        return redirect('password_list')
    return render(request, 'vault/confirm_delete.html', {'entry': entry})

def password_list(request):
    # Check if the user is logged in (this ensures we only get passwords for logged-in users)
    if request.user.is_authenticated:
        query = request.GET.get('q', '')
        
        # Get password entries for the logged-in user
        if query:
            # Filter by the query (searching by website name or username)
            passwords = PasswordEntry.objects.filter(
                Q(user=request.user) &
                (Q(website_name__icontains=query) | Q(username__icontains=query))
            )
        else:
            # If there's no search query, get all passwords for the logged-in user
            passwords = PasswordEntry.objects.filter(user=request.user)
    else:
        passwords = []

    # Return the password list to the template
    return render(request, 'vault/password_list.html', {'passwords': passwords})