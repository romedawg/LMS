from django.db import models

# Create your models here.

class AvnetTypeInfo(models.Model):
    avnet_type_id = models.IntegerField()
    avnet_name = models.CharField(max_length=50) 
    avnet_title = models.TextField()
    last_modified_str = models.CharField(max_length=25) 
    created_str = models.CharField(max_length=25) 
    last_modified = models.TimeField()
    last_modified_by= models.CharField(max_length=100) 
    created = models.TimeField()
    classroom_delivery_method = models.CharField(max_length=200) 

class AvnetDescription(models.Model):
    avnet_description_id = models.IntegerField() 
    avnet_type_id = models.ForeignKey('AvnetTypeInfo') 
    avnet_name = models.CharField(max_length=50) 
    avnet_title = models.TextField()
    last_modified_str = models.CharField(max_length=25) 
    created_str = models.CharField(max_length=25) 
    last_modified = models.TimeField()
    last_modified_by= models.CharField(max_length=100) 
    created = models.TimeField()
    classroom_delivery_method = models.CharField(max_length=200) 

class ClassPlSummary(models.Model):
    pl_summary_id = models.IntegerField()
    jmw_class_info_id = models.IntegerField()
    avent_type_info_id = models.IntegerField()
    jmw_name = models.CharField(max_length=50)
    avnet_name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    jmw_locaiton_info_id = models.IntegerField()
    instructor_id = models.IntegerField()
    instructor_name = models.CharField(max_length=100)
    facility_expense = models.DecimalField(max_digits=6, decimal_places=2)
    material_expense = models.DecimalField(max_digits=6, decimal_places=2)
    lab_expense = models.DecimalField(max_digits=6, decimal_places=2)
    travel_expense = models.DecimalField(max_digits=6, decimal_places=2)
    instructor_expense = models.DecimalField(max_digits=6, decimal_places=2)
    other_expense = models.DecimalField(max_digits=6, decimal_places=2)
    total_expense = models.DecimalField(max_digits=6, decimal_places=2)
    class_prce = models.DecimalField(max_digits=6, decimal_places=2)
    total_attend = models.IntegerField()
    total_jmw_attend = models.IntegerField()
    gross_receipts = models.DecimalField(max_digits=6, decimal_places=2)
    net_profit = models.DecimalField(max_digits=6, decimal_places=2)
    gross_jmw_receipts = models.DecimalField(max_digits=6, decimal_places=2)
    po = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    instructor_rate = models.DecimalField(max_digits=6, decimal_places=2)
    net_profit = models.DecimalField(max_digits=6, decimal_places=2)

class JMWClassInfo(models.Model):
    jmw_class_info_id = models.IntegerField()
    jmw_name = models.CharField(max_length=25)
    avnet_type_info_id = models.IntegerField()
    avnet_type_name = models.CharField(max_length=50)
    start_date_str = models.CharField(max_length=50)
    end_date_str = models.CharField(max_length=50)
    last_modified_str = models.CharField(max_length=25)
    created_str = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()
    created = models.DateTimeField()
    last_modified = models.DateTimeField()
    last_modified_by = models.CharField(max_length=100)
    start_date_local = models.DateField()
    end_date_local = models.DateField()
    duration = models.IntegerField()
    duration_unit = models.CharField(max_length=10)
    public = models.CharField(max_length=10)
    class_status = models.CharField(max_length=10)
    gtr = models.CharField(max_length=10)
    total_registered = models.IntegerField()
    total_jmw_registered = models.IntegerField()
    instructor = models.IntegerField()
    instructor_name = models.CharField(max_length=100) 
    type_url = models.CharField(max_length=200) 
    title = models.TextField()
    category = models.CharField(max_length=200) 
    price = models.IntegerField()
    owned_by = models.CharField(max_length=100) 
    source_by = models.CharField(max_length=100) 
    currency = models.CharField(max_length=25) 
    jmw_locaiton_info_id = models.IntegerField()
    room_info_id = models.IntegerField()
    subcategory = models.CharField(max_length=200) 
    notes = models.TextField()
    po = models.CharField(max_length=50) 
    tech = models.CharField(max_length=50) 
    labs = models.CharField(max_length=50) 
    lock_price = models.CharField(max_length=1) 

class JMWLocationInfo(models.Model):
    jmw_location_info_id = models.IntegerField()
    owner_code = models.CharField(max_length=25) 
    owner_id = models.IntegerField()
    location_code = models.CharField(max_length=200) 
    description = models.CharField(max_length=200) 
    street = models.CharField(max_length=100) 
    suite = models.CharField(max_length=50) 
    city = models.CharField(max_length=50) 
    state = models.CharField(max_length=20) 
    postal_code = models.CharField(max_length=25) 
    country = models.CharField(max_length=50) 
    web_page = models.CharField(max_length=50) 
    number_of_rooms = models.IntegerField()
    timezone = models.CharField(max_length=25) 
    default_type = models.CharField(max_length=10) 
    default_tech = models.CharField(max_length=25) 
    phone = models.CharField(max_length=25) 
    admin_name = models.CharField(max_length=100) 
    admin_email = models.CharField(max_length=50) 
    admin_phone= models.CharField(max_length=25) 
    tech_name = models.CharField(max_length=100) 
    tech_email = models.CharField(max_length=50) 
    tech_phone= models.CharField(max_length=25) 
    notes = models.TextField() 

class RoomInfo(models.Model):
    room_info_id = models.IntegerField()
    location_info_id = models.ForeignKey('JMWLocationInfo')
    room_name= models.CharField(max_length=50) 
    number_seats= models.IntegerField()
    cpu = models.CharField(max_length=50) 
    ram = models.CharField(max_length=25) 
    memory= models.CharField(max_length=25) 
    in_speed = models.CharField(max_length=25) 
