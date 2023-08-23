from django.db import models
from users.models import Users


# The property category i.e residential and commercial


class PropertyCategories(models.Model):
    category_name = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        db_table="property_categories"
# The types of property eg. house,mansion,villa,office


class PropertyTypes(models.Model):
    category = models.ForeignKey(
        PropertyCategories, on_delete=models.CASCADE, verbose_name="Property Category"
    )
    type_name = models.CharField(max_length=20)
    created_at = models.DateTimeField()

    class Meta:
        db_table="property_types"


# attributes of the property


class Attributes(models.Model):
    attribute_name = models.CharField(50)
    created_at = models.DateTimeField()

    class Meta:
        db_table="attributes"


# Address of the Property
class Address(models.Model):
    region = models.CharField(max_length=15)
    district = models.CharField(max_length=30)
    street = models.CharField(max_length=30)

    class Meta:
        db_table="property_address"


# Properties Model
class Properties(models.Model):
    user = models.ForeignKey(
        Users, on_delete=models.CASCADE, verbose_name="property owner"
    )
    type = models.ForeignKey(
        PropertyTypes, on_delete=models.CASCADE, verbose_name="property type"
    )
    category = models.ForeignKey(
        PropertyCategories, on_delete=models.CASCADE, verbose_name="property category"
    )
    address = models.ForeignKey(
        Address, on_delete=models.CASCADE, verbose_name="property address"
    )
    price = models.FloatField()
    estate_name = models.CharField(max_length=50)
    conditions = models.CharField(max_length=50)
    utilities = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    pictures = models.CharField(max_length=200)
    is_for_sale = models.BooleanField(
        default=False
    )  # true implies house is for sale false implies house is for rent
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField()

    class Meta:
        db_table="properties"


# Attributes of the specific property
class PropertyAttributes(models.Model):
    property = models.ForeignKey(
        Properties, on_delete=models.CASCADE, verbose_name="Property Name"
    )
    attribute = models.ForeignKey(
        Attributes, on_delete=models.CASCADE, verbose_name="Property Attribute"
    )
    value = models.CharField()

    class Meta:
        db_table="property_attributes"
