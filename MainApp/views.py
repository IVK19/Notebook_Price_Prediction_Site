from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from MainApp.forms import AddNotebookForm, LoginUserForm, RegistrationUserForm
import tensorflow as tf
from tensorflow import keras
import torch
from utils import random_color_string_generator, get_array
from .models import *

def index_page(request):
    if request.method == 'GET':
        form = AddNotebookForm(request.GET)
        context = {
            'title': 'Добро пожаловать на сайт оценки стоимости ноутбука!',
            'form': form
        }
        return render(request, 'index.html', context)
    if request.method == 'POST':
        form = AddNotebookForm(request.POST)
        if form.is_valid():
            notebook = form.save(commit=False)
            arr = get_array(notebook)
            npp_model4 = keras.models.load_model('npp_model_4_1')
            npp_model5 = torch.jit.load('model5_1_scripted.pt')
            npp_model5.eval()
            if request.user.is_authenticated:
                price = int((((int(npp_model4(tf.cast(arr, dtype=float)).numpy()[0][0]) // 1000) * 1000 + (
                            int(npp_model5(torch.from_numpy(arr).type(torch.FloatTensor)).item()) // 1000) * 1000) // 2) * 0.93)
                notebook.discount = 1
            else:
                price = ((int(npp_model4(tf.cast(arr, dtype=float)).numpy()[0][0]) // 1000) * 1000 + (int(npp_model5(torch.from_numpy(arr).type(torch.FloatTensor)).item()) // 1000) * 1000) // 2
            notebook.price = price
            notebook.save()
            context = {
                'title': 'Добро пожаловать на сайт оценки стоимости ноутбука!',
                'form': form,
                'price': price
            }
            return render(request, 'index.html', context)


class NotebooksList(ListView):
    paginate_by = 6
    model = Notebook
    template_name = 'notebooks-list.html'

    def get_queryset(self):
        return Notebook.objects.select_related('disp', 'disp_type', 'proc', 'core', 'freq', 'gc', 'r_a_m', 'hd', 'cm', 'o_s').all()


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    next_page = 'home'

def logout(request):
    auth.logout(request)
    return redirect('home')



class RegistrationUser(CreateView):
    form_class = RegistrationUserForm
    template_name = 'registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def get_statistics(request):
    colors_lst = list()
    for _ in range(10):
        colors_lst.append(random_color_string_generator())
    screens = Display.objects.all()
    dict_screens = dict()
    list_screens = list()
    for screen in screens:
        screen_count = Notebook.objects.filter(disp__display=str(screen.display)).count()
        dict_screens[str(screen).replace('"', '')] = screen_count
    for par, num in dict_screens.items():
        list_screens.append([par, num, colors_lst[0]])
    screens_type = DisplayType.objects.all()
    dict_screens_type = dict()
    list_screens_type = list()
    for screen in screens_type:
        screen_type_count = Notebook.objects.filter(disp_type__display_type=str(screen.display_type)).count()
        dict_screens_type[str(screen)] = screen_type_count
    for par, num in dict_screens_type.items():
        list_screens_type.append([par, num, colors_lst[1]])
    prs = Processor.objects.all()
    dict_prs = dict()
    list_prs = list()
    for pr in prs:
        pr_count = Notebook.objects.filter(proc__processor=str(pr.processor)).count()
        dict_prs[str(pr)] = pr_count
    for par, num in dict_prs.items():
        list_prs.append([par, num, colors_lst[2]])
    crs = Cores.objects.all()
    dict_crs = dict()
    list_crs = list()
    for cr in crs:
        cr_count = Notebook.objects.filter(core__cores=str(cr.cores)).count()
        dict_crs[str(cr)] = cr_count
    for par, num in dict_crs.items():
        list_crs.append([par, num, colors_lst[3]])
    frs = Frequency.objects.all()
    dict_frs = dict()
    list_frs = list()
    for fr in frs:
        fr_count = Notebook.objects.filter(freq__frequency=str(fr.frequency)).count()
        dict_frs[str(fr)] = fr_count
    for par, num in dict_frs.items():
        list_frs.append([par, num, colors_lst[4]])
    grs = GraphicsCard.objects.all()
    dict_grs = dict()
    list_grs = list()
    for gr in grs:
        gr_count = Notebook.objects.filter(gc__graphics_card=str(gr.graphics_card)).count()
        dict_grs[str(gr)] = gr_count
    for par, num in dict_grs.items():
        list_grs.append([par, num, colors_lst[5]])
    rms = RAM.objects.all()
    dict_rms = dict()
    list_rms = list()
    for rm in rms:
        rm_count = Notebook.objects.filter(r_a_m__ram=str(rm.ram)).count()
        dict_rms[str(rm)] = rm_count
    for par, num in dict_rms.items():
        list_rms.append([par, num, colors_lst[6]])
    hrds = HardDisk.objects.all()
    dict_hrds = dict()
    list_hrds = list()
    for hrd in hrds:
        hrd_count = Notebook.objects.filter(hd__hard_disk=str(hrd.hard_disk)).count()
        dict_hrds[str(hrd)] = hrd_count
    for par, num in dict_hrds.items():
        list_hrds.append([par, num, colors_lst[7]])
    caches = CacheMemory.objects.all()
    dict_caches = dict()
    list_caches = list()
    for cache in caches:
        cache_count = Notebook.objects.filter(cm__cache_memory=str(cache.cache_memory)).count()
        dict_caches[str(cache)] = cache_count
    for par, num in dict_caches.items():
        list_caches.append([par, num, colors_lst[8]])
    osys = OS.objects.all()
    dict_osys = dict()
    list_osys = list()
    for osy in osys:
        osy_count = Notebook.objects.filter(o_s__os=str(osy.os)).count()
        dict_osys[str(osy)] = osy_count
    for par, num in dict_osys.items():
        list_osys.append([par, num, colors_lst[9]])
    context = {
        'title': 'На данной странице отображается статистика пользовательских запросов по параметрам ноутбуков.',
        'list_screens': list_screens,
        'list_screens_type': list_screens_type,
        'list_prs': list_prs,
        'list_crs': list_crs,
        'list_frs': list_frs,
        'list_grs': list_grs,
        'list_rms': list_rms,
        'list_hrds': list_hrds,
        'list_caches': list_caches,
        'list_osys': list_osys
    }
    return render(request, 'statistics.html', context)