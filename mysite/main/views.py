from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Download
from .forms import VideoForm, RegisterUserForm
from .services import open_file
from django.http import StreamingHttpResponse
def index(request):
    play = Download.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'play': play})
def get_video(request, pk: int):
    _video = get_object_or_404(Download, id=pk)
    return render(request, "main/player.html", {"video": _video})
def add(request):
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video_user = form.save(commit=False)
            video_user.author = request.user
            video_user.save()
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'
    form = VideoForm()
    context = {
        'form': form
    }
    return render(request, 'main/add.html', context)
def get_streaming_video(request, pk: int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')
    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('add')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(title="Регистрация")
        return {**context, **user_context}
    def get_user_context(self, title):
        user_context = {
            'user_title': title,
        }
        return user_context
    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)  # Автоматически войти в систему только что зарегистрированного пользователя
        return response
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = 'login'
class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    def get_success_url(self):
        return 'add'
@login_required
def logout_user(request):
    logout(request)
    return redirect('add')
def delete_video(request, pk: int):
    video = get_object_or_404(Download, id=pk)
    video.delete()
    return redirect('add')
def edit_video(request, pk):
    video = get_object_or_404(Download, pk=pk)
    if request.method == "POST":
        form = VideoForm(request.POST, request.FILES, instance=video)
        if form.is_valid():
            edited_video = form.save(commit=False)
            edited_video.author = request.user
            edited_video.save()
            return redirect('index')
    else:
        form = VideoForm(instance=video)
    context = {
        'form': form,
        'video': video,
    }
    return render(request, 'main/edit.html', context)