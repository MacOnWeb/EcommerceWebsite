from django.db import models


# Create your models here.

class Register(models.Model):
    uname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default="")
    password = models.CharField(max_length=50)
    phone = models.CharField(max_length=50, default="")

    def __str__(self):
        return "uname"+self.name + "email"+self.email + "phone"+self.phone


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    publish_date = models.DateField()
    image = models.ImageField(upload_to="myproject/images", default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=300)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default="0")
    fname = models.CharField(max_length=90)
    lname = models.CharField(max_length=111)
    uname = models.CharField(max_length=111)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    add1 = models.CharField(max_length=111)
    add2 = models.CharField(max_length=111)
    country = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
