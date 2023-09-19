from django.urls import path
from . import views

urlpatterns = [
    #一般が見られるページ
    path("", views.homepage, name='home'), #ホームページ
    #管理者のページ
    path("admin_home/", views.admin_home, name='admin_home'), #管理者画面
    path("admin_login/", views.Login, name='Login'), #管理者ログイン
    path("admin_register/", views.register_lost_property, name='register'), #落とし物の登録
    path("delete/", views.delete, name='delete'), #落とし物削除
    path("select_confirmation/", views.select_confirmation, name='select_confirmation'), #認証落とし物選択画面
    path("admin_confirmation/<int:lost_id>", views.confirmation, name='admin_confirmation'), #落とし物認証画面
    #path("property/", views.lost_property, name='property'), #落とし物一覧
    #適宜パスを追加
    #一応追加
    path("about/", views.about, name='about'), #ツールについて
    path("contact_us/", views.contact_us, name='contact_us'), #連絡先
    path("help/", views.help, name='help'), #ヘルプ
    path("admin_account/", views.account, name='account'), #アカウント情報
]
#"sample/<int:pk>"という感じのURLの指定方法もあるぽい
