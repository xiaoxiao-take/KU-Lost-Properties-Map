from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import LostPropertyForm, SearchForm
from .models import LostProperty
import find_my_lost_property.image_generator as image_generator
from django.core.files.base import ContentFile
import random

# Create your views here.
def homepage(request): #ホームぺージ
    lost_property = serializers.serialize("json", LostProperty.objects.all())
    template_name = "find_my_lost_property/home.html"
    return render(request, template_name, {"properties": lost_property})

def admin_home(request): #管理者ホームページ
    print("test")
    print(request.user.is_staff)
    if not request.user.is_staff:
        return redirect("home")
    return render(request, 'find_my_lost_property/admin_home.html')

def Login(request):
    # POST
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')

        user = authenticate(username=ID, password=Pass)

        # ユーザー認証
        if user:
            #ユーザーアクティベート判定
            if user.is_active:
                # ログイン
                login(request,user)
                # ホームページ遷移
                return HttpResponseRedirect(reverse('admin_home'))
            else:
                # アカウント利用不可
                return HttpResponse("アカウントが有効ではありません")
        # ユーザー認証失敗
        else:
            return HttpResponse("ログインIDまたはパスワードが間違っています")
    # GET
    else:
        return render(request, 'find_my_lost_property/login.html')

#ログアウト
@login_required
def Logout(request):
    logout(request)
    # ログイン画面遷移
    return HttpResponseRedirect(reverse('Login'))

def register_lost_property(request): #落とし物の登録
    if not request.user.is_staff:
        return redirect("home")
    if request.method == 'POST':
        form = LostPropertyForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            category_name = form.cleaned_data['category_name']
            color = form.cleaned_data['color']
            finder_name = form.cleaned_data['finder_name']
            found_time = form.cleaned_data['found_time']
            found_latitude = form.cleaned_data['found_latitude']
            found_longitude = form.cleaned_data['found_longitude']
            manage_location = form.cleaned_data['manage_location']
            true_image = form.cleaned_data['true_image']

            prompt = f"{category_name} {color}"
            dummy_images = image_generator.generate_dummy_image(prompt)

            lost_property = LostProperty()
            lost_property.category_name = category_name
            lost_property.color = color
            lost_property.finder_name = finder_name
            lost_property.found_time = found_time
            lost_property.found_latitude = found_latitude
            lost_property.found_longitude = found_longitude
            lost_property.manage_location = manage_location
            lost_property.true_image = true_image

            lost_property.dummy_image1.save("dummy1.png", ContentFile(dummy_images[0]), save=False)
            lost_property.dummy_image2.save("dummy2.png", ContentFile(dummy_images[1]), save=False)
            lost_property.dummy_image3.save("dummy3.png", ContentFile(dummy_images[2]), save=False)
            lost_property.dummy_image4.save("dummy4.png", ContentFile(dummy_images[3]), save=False)

            lost_property.save()
            #form.save()
            return redirect('register')
        else:
            print(form)
    else:
        form = LostPropertyForm()
    return render(request, 'find_my_lost_property/admin_register.html')

def index(request):
    return render(request, 'find_my_lost_property/index.html')

def delete(request):
    if not request.user.is_staff:
        return redirect("home")
    if request.method == 'POST':
        delete_id = request.POST.get('lost_id')
        LostProperty.objects.filter(id=delete_id).delete()

    lost_property = serializers.serialize("json", LostProperty.objects.all())
    template_name = "find_my_lost_property/admin_delete.html"
    return render(request, template_name, {"properties": lost_property})

def lost_property(request): #落とし物一覧
    lost_property = LostProperty.objects.all()
    template_name = "find_my_lost_property/property.html"
    return render(request, template_name, {"properties": lost_property})

def select_confirmation(request): # 認証を行う落とし物の選択
    if not request.user.is_staff:
        return redirect("home")
    if request.method == 'GET':
        lost_property = serializers.serialize("json", LostProperty.objects.all())
        template_name = "find_my_lost_property/select_confirmation.html"
        return render(request, template_name, {"properties": lost_property})
    if request.method == 'POST':
        lost_id = request.POST.get('lost_id')
        redirect_url = reverse('admin_confirmation', kwargs={'lost_id': lost_id})
        return redirect(redirect_url)

def confirmation(request, lost_id):
    if request.method == 'GET':
        lost_property = LostProperty.objects.get(id=lost_id)
        true_img, dummy1_img, dummy2_img, dummy3_img, dummy4_img = {}, {}, {}, {}, {}
        true_img['img_path'] = lost_property.true_image.url
        true_img['is_true'] = 1
        dummy1_img['img_path'] = lost_property.dummy_image1.url
        dummy1_img['is_true'] = 0
        dummy2_img['img_path'] = lost_property.dummy_image2.url
        dummy2_img['is_true'] = 0
        dummy3_img['img_path'] = lost_property.dummy_image3.url
        dummy3_img['is_true'] = 0
        dummy4_img['img_path'] = lost_property.dummy_image4.url
        dummy4_img['is_true'] = 0
        images = [true_img, dummy1_img, dummy2_img, dummy3_img, dummy4_img]
        random.shuffle(images)
        return render(request, 'find_my_lost_property/admin_confirmation.html', {'images': images})
    if request.method == 'POST':
        if request.POST.get('selected_image') == '1':
            # LostProperty.objects.filter(id=lost_id).delete() # 認証成功であれば削除する？
            return render(request, 'find_my_lost_property/success.html')
        else:
            return render(request, 'find_my_lost_property/failure.html')


def about(request): #アプリについて
    return render(request, 'find_my_lost_property/about.html')

def contact_us(request): #連絡先
    return render(request, 'find_my_lost_property/contact_us.html')

def help(request): #アプリについて
    return render(request, 'find_my_lost_property/admin_help.html')

def account(request): #アプリについて
    return render(request, 'find_my_lost_property/admin_account.html')

# def detail(request, id):
#     LostProperty = get_object_or_404(LostProperty, pk=id)
#     context = {
#         'LostProperty': LostProperty,
#     }
#     return render(request, 'find_my_lost_proerty/confirmation.html', context)

# 以下使わなかったもの
# def admin(request): #落とし物のリスト取得   
#     lost_property = LostProperty.objects.all()
#     ctx = {}
#     ctx["object_list"] = lost_property
#     template_name = "find_my_lost_property/sample_matsuo.html"
#     return render(request, template_name, ctx)