from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Request
from .forms import RegistrationForm, RequestForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def request_list(request):
    requests = Request.objects.all()
    return render(request, 'requests_list.html', {'requests': requests})


@login_required
def create_request(request):
    if request.user.role != 'parent':
        return render(request, 'error.html', {'message': 'Только родители могут создавать заявки'})

    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            new_request = form.save(commit=False)
            new_request.parent = request.user
            new_request.save()
            return redirect('request_list')
    else:
        form = RequestForm()
    return render(request, 'request_form.html', {'form': form})


@login_required
def edit_request(request, request_id):
    req = Request.objects.get(id=request_id)
    if request.user.role != 'animator':
        return render(request, 'error.html', {'message': 'Только аниматоры могут редактировать заявки'})

    if request.method == 'POST':
        form = RequestForm(request.POST, instance=req)
        if form.is_valid():
            updated_request = form.save(commit=False)
            updated_request.animator = request.user
            updated_request.status = 'accepted'
            updated_request.save()
            return redirect('request_list')
    else:
        form = RequestForm(instance=req)
    return render(request, 'request_form.html', {'form': form})