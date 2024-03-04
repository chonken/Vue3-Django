from django.db import models

class Product(models.Model):
    id = models.CharField(db_column='商品編號', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    name = models.CharField(db_column='商品名稱', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    price = models.FloatField(db_column='單價', blank=True, null=True)
    stock = models.IntegerField(db_column='庫存量', blank=True, null=True)
    discount = models.FloatField(db_column='折扣', blank=True, null=True)
    image = models.CharField(db_column='圖片', blank=True, null=True, max_length=100, db_collation='Chinese_Taiwan_Stroke_CI_AS')

    def save(self, *args, **kwargs):
        if not self.id:
            max_id = Product.objects.all().order_by('-id').values('id').first() or -1
            self.id = str(int(max_id['id']) + 1)
        super().save(*args, **kwargs)

    class Meta:
        db_table = '商品'

class Customer(models.Model):
    id = models.CharField(db_column='客戶編號', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    name = models.CharField(db_column='姓名', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    phone = models.CharField(db_column='電話', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    address = models.CharField(db_column='地址', max_length=255, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    district = models.CharField(db_column='行政區', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)

    class Meta:
        db_table = '客戶'

class Store(models.Model):
    id = models.CharField(db_column='門市編號', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    name = models.CharField(db_column='門市名稱', max_length=50, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    tax_id = models.CharField(db_column='營業人統編', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    address = models.CharField(db_column='地址', max_length=255, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)

    class Meta:
        db_table = '門市'

class OrderHeader(models.Model):
    id = models.CharField(db_column='訂單編號', primary_key=True, max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, db_column='客戶編號', blank=True, null=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, db_column='門市編號', blank=True, null=True)
    gui_number = models.CharField(db_column='統一編號', max_length=20, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    date = models.DateTimeField(db_column='日期', blank=True, null=True)
    random = models.CharField(db_column='隨機號', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)
    serial = models.CharField(db_column='序號', max_length=10, db_collation='Chinese_Taiwan_Stroke_CI_AS', blank=True, null=True)

    class Meta:
        db_table = '訂貨主檔'

class OrderDetail(models.Model):
    orderheader = models.OneToOneField(OrderHeader, on_delete=models.PROTECT, db_column='訂單編號')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='商品編號')
    quantity = models.IntegerField(db_column='數量', blank=True, null=True)
    discount = models.FloatField(db_column='折扣', blank=True, null=True)

    class Meta:
        db_table = '訂貨明細'
        unique_together = (('orderheader', 'product'))
