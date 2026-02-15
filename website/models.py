from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return(f"{self.first_name}")
    
    
class Patients(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    nic = models.CharField(max_length=50)
    dob = models.DateField()

    def __str__(self):
        return(f"{self.name}")
    
class Categories(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return(f"{self.category_name}")
    
class Medicines(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    medicine_name = models.CharField(max_length=100)
    generic_name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=5, decimal_places=2)
    rol =  models.DecimalField(max_digits=5, decimal_places=2)
    roq =  models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return(f"{self.medicine_name}")
  
class Consultations(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patients, on_delete=models.CASCADE)
    visit_date = models.DateTimeField()
    diagnosis = models.CharField(max_length=255)
    uploaded_report1 = models.ImageField()
    uploaded_report2 = models.ImageField()
    uploaded_report3 = models.ImageField()
    uploaded_report4 = models.ImageField()
    uploaded_report5 = models.ImageField()
    additional_notes = models.CharField(max_length=255)

    def __str__(self):
        return(f"{self.patient}")
    
class Issue_Medicine(models.Model):
    consultation = models.ForeignKey(Consultations, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    qty = models.DecimalField(max_digits=4, decimal_places=2)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return(f"{self.consultation}")

class Suppliers(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    supplier_name =models.CharField(max_length=100)
    supplier_address =models.CharField(max_length=100)
    supplier_phone =models.CharField(max_length=100)
    supplier_email =models.CharField(max_length=100)
    contact_person_name =models.CharField(max_length=100)
    contact_person_phone =models.CharField(max_length=100)

    def __str__(self):
        return(f"{self.supplier_name}")

class Purchases(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    bill_no =models.CharField(max_length=100)
    supplier = models.ForeignKey(Suppliers, on_delete=models.CASCADE)
    purchased_date = models.DateTimeField()
    bill_amount = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return(f"{self.bill_no}")

class Purchases_Dtl(models.Model):
    purchases =models.ForeignKey(Purchases, on_delete=models.CASCADE)
    medicine = models.ForeignKey(Medicines, on_delete=models.CASCADE)
    dosage = models.CharField(max_length=100)
    qty = models.DecimalField(max_digits=5, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return(f"{self.purchases}")