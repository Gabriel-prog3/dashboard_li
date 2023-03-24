# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clima(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    fecha = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)
    rad = models.FloatField(blank=True, null=True)
    temp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "clima"


class Consumo(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    fecha = models.TextField(
        db_column="Fecha", blank=True, null=True
    )  # Field name made lowercase.
    hora = models.TextField(
        db_column="Hora", blank=True, null=True
    )  # Field name made lowercase.
    i1 = models.IntegerField(
        db_column="I1", blank=True, null=True
    )  # Field name made lowercase.
    fuentei1 = models.TextField(
        db_column="fuenteI1", blank=True, null=True
    )  # Field name made lowercase.
    i2 = models.IntegerField(
        db_column="I2", blank=True, null=True
    )  # Field name made lowercase.
    fuentei2 = models.TextField(
        db_column="fuenteI2", blank=True, null=True
    )  # Field name made lowercase.
    i3 = models.IntegerField(
        db_column="I3", blank=True, null=True
    )  # Field name made lowercase.
    fuentei3 = models.TextField(
        db_column="fuenteI3", blank=True, null=True
    )  # Field name made lowercase.
    i4 = models.IntegerField(
        db_column="I4", blank=True, null=True
    )  # Field name made lowercase.
    fuentei4 = models.TextField(
        db_column="fuenteI4", blank=True, null=True
    )  # Field name made lowercase.
    i5 = models.IntegerField(
        db_column="I5", blank=True, null=True
    )  # Field name made lowercase.
    fuentei5 = models.TextField(
        db_column="fuenteI5", blank=True, null=True
    )  # Field name made lowercase.
    i6 = models.IntegerField(
        db_column="I6", blank=True, null=True
    )  # Field name made lowercase.
    fuentei6 = models.TextField(
        db_column="fuenteI6", blank=True, null=True
    )  # Field name made lowercase.
    i7 = models.IntegerField(
        db_column="I7", blank=True, null=True
    )  # Field name made lowercase.
    fuentei7 = models.TextField(
        db_column="fuenteI7", blank=True, null=True
    )  # Field name made lowercase.
    i8 = models.IntegerField(
        db_column="I8", blank=True, null=True
    )  # Field name made lowercase.
    fuentei8 = models.TextField(
        db_column="fuenteI8", blank=True, null=True
    )  # Field name made lowercase.
    p1 = models.IntegerField(blank=True, null=True)
    p2 = models.IntegerField(blank=True, null=True)
    p3 = models.IntegerField(blank=True, null=True)
    p4 = models.IntegerField(blank=True, null=True)
    p5 = models.IntegerField(blank=True, null=True)
    p6 = models.IntegerField(blank=True, null=True)
    p7 = models.IntegerField(blank=True, null=True)
    p8 = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "consumo"


class Generacion(models.Model):
    id = models.IntegerField(primary_key=True, blank=True)
    fecha = models.TextField(blank=True, null=True)
    hora = models.TextField(blank=True, null=True)
    i_inv = models.IntegerField(blank=True, null=True)
    v_inv = models.IntegerField(blank=True, null=True)
    p_inv = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "generacion"
