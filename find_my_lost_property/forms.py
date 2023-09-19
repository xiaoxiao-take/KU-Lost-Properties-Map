from django import forms
from .models import LostProperty
from django.contrib.auth.models import User

class LostPropertyForm(forms.ModelForm):
    class Meta:
        model = LostProperty
        fields = ("category_name", "color", "finder_name", "found_time", "found_latitude", "found_longitude", "manage_location", "true_image")
        labels = {
            'category_name': 'カテゴリー',
            'color': '色',
            'finder_name': '拾得者の名前',
            'found_time': '拾得日時',
            'found_latitude': '緯度',
            'found_longitude': '経度',
            'manage_location': '届けられた場所',
            'true_image': '落とし物の画像'
        }

# フォームクラス作成
class AccountForm(forms.ModelForm):
    # パスワード入力：非表示対応
    password = forms.CharField(widget=forms.PasswordInput(),label="パスワード")

    class Meta():
        # ユーザー認証
        model = User
        # フィールド指定
        fields = ('username','email','password')
        # フィールド名指定
        labels = {'username':"ユーザーID",'email':"メール"}

class SearchForm(forms.Form):
    keyword = forms.CharField(label='', max_length=50)