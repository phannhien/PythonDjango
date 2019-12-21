# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Loai(models.Model):
    maloai = models.AutoField(db_column='MaLoai', blank=True, null=True)  # Field name made lowercase.
    tenloai = models.TextField(db_column='TenLoai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Loai'


class Sanpham(models.Model):
    masp = models.AutoField(db_column='MaSP', blank=True, null=True)  # Field name made lowercase.
    tensp = models.TextField(db_column='TenSP', blank=True, null=True)  # Field name made lowercase.
    gia = models.IntegerField(db_column='Gia', blank=True, null=True)  # Field name made lowercase.
    soluong = models.IntegerField(db_column='SoLuong', blank=True, null=True)  # Field name made lowercase.
    anh = models.TextField(db_column='Anh', blank=True, null=True)  # Field name made lowercase.
    maloai = models.IntegerField(db_column='MaLoai', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SanPham'


