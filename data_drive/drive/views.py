from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from .models import Folder, File
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    folders = Folder.objects.filter(parent=None, created_by=request.user)
    return render(request, 'drive/home.html', {'folders': folders})

@login_required
def create_folder(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        parent_id = request.POST.get('parent_id')
        parent = Folder.objects.get(id=parent_id) if parent_id else None
        Folder.objects.create(name=name, parent=parent, created_by=request.user)
        return redirect('home')
    folders = Folder.objects.filter(created_by=request.user)
    return render(request, 'drive/create_folder.html', {'folders': folders})

@login_required
def view_folder(request, id):
    folder = get_object_or_404(Folder, id=id, created_by=request.user)
    return render(request, 'drive/view_folder.html', {'folder': folder})

@login_required
def delete_folder(request, id):
    folder = get_object_or_404(Folder, id=id, created_by=request.user)
    folder.delete()
    return redirect('home')

@login_required
def upload_file(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        folder_id = request.POST.get('folder_id')
        folder = Folder.objects.get(id=folder_id)
        file_data = request.FILES['file_data']
        File.objects.create(name=name, folder=folder, uploaded_by=request.user, file_data=file_data)
        return redirect('home')
    folders = Folder.objects.filter(created_by=request.user)
    return render(request, 'drive/upload_file.html', {'folders': folders})

@login_required
def delete_file(request, id):
    file = get_object_or_404(File, id=id, uploaded_by=request.user)
    file.delete()
    return redirect('home')
