from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Create your models here.
class LostProperty(models.Model):
    """
    LostProperty 落とし物のクラス

    Parameters
    ----------
    models : module
        Modelクラスのmodels

    クラス変数
    ----------
    category_name :  instance
        カテゴリ名
    color : instance
        色
    finder_name : instance
        発見者の名前
    finder_phone_number : instance
        発見者の電話番号
    found_time : instance
        発見時間(日にちも入る)
    found_latitude : instance
        発見緯度
    found_longitude : instance
        発見経度
    manage_location : instance
        落とし物の届けられた場所
    #以下matsuoが追加
    img : 
        落とし物の画像
    """
    category_name = models.CharField(max_length=30)
    color = models.CharField(max_length=10)
    finder_name = models.CharField(max_length=20)
    finder_phone_number = PhoneNumberField
    found_time = models.DateTimeField(auto_now=False, auto_now_add=False)
    found_latitude = models.DecimalField(u'緯度', max_digits=20, decimal_places=15, default=0)
    found_longitude = models.DecimalField(u'経度', max_digits=20, decimal_places=15, default=0)
    manage_location = models.CharField(max_length=30)
    true_image = models.ImageField(null=True, blank=True)
    dummy_image1 = models.ImageField(null=True, blank=True)
    dummy_image2 = models.ImageField(null=True, blank=True)
    dummy_image3 = models.ImageField(null=True, blank=True)
    dummy_image4 = models.ImageField(null=True, blank=True)
    #img = models.ImageField(upload_to="lost_property",blank=True)
        # class Meta:
        #     db_table = 'lost_property'

    def __unicode__(self):
        return self.category_name, self.finder_name, self.color

class Administrator(models.Model):
    """
    Administrator 管理者のクラス

    _extended_summary_
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #ID = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username
    
# class Map():
#     """
#     Map 地図のクラス

#     Parameters
#     ----------
#     name : 場所の名前
#     latitude : 緯度
#     longitude : 経度
#     """
#     name = models.CharFiled(max_length=20)
#     latitude = models.DecimalField(u'緯度', max_digits=9, decimal_places=6, default=0)
#     longitude = models.DecimalField(u'経度', max_digits=9, decimal_places=6, default=0)

#     def __unicode__(self):
#         return self.name