from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'	


# Create Add Record Form
class AddRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control"}), label="")

	class Meta:
		model = Record
		exclude = ("user",)



# Create Add Patient Form
class AddPatientForm(forms.ModelForm):
	name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Full Name", "class":"form-control"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control"}), label="")
	nic = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"NIC Number", "class":"form-control"}), label="")
	dob = forms.DateField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Date of Birth", "class":"form-control"}), label="")

	class Meta:
		model = Patients
		exclude = ("user",)

# Create Add Category Form
class AddCategoryForm(forms.ModelForm):
	category_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Category Name Name", "class":"form-control"}), label="")

	class Meta:
		model = Categories
		exclude = ("user",)

# Create Add Medicines Form
class AddMedicineForm(forms.ModelForm):
	medicine_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Medicine Name", "class":"form-control"}), label="")
	generic_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Generic Name", "class":"form-control"}), label="")
	description = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Description", "class":"form-control"}), label="")
	category = forms.ChoiceField(required=True, widget=forms.widgets.Select(attrs={"placeholder":"Category", "class":"form-control"}), label="Select Category")
	manufacturer = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Manufacturer", "class":"form-control"}), label="")
	rol = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Re-Order Level", "class":"form-control"}), label="")
	roq = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Re-Order Quantity", "class":"form-control"}), label="")
	op_balance = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Opening Balance", "class":"form-control"}), label="")

	class Meta:
		model = Medicines
		exclude = ("user",)


# Create Add Suppliers Form
class AddSupliersForm(forms.ModelForm):
	supplier_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Supplier Name", "class":"form-control"}), label="")
	supplier_address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Supplier Address", "class":"form-control"}), label="")
	supplier_phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Supplier Phone", "class":"form-control"}), label="")
	supplier_email = forms.EmailField(widget=forms.widgets.TextInput(attrs={"placeholder":"Supplier Email", "class":"form-control"}), label="")
	contact_person_name = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Contact Person Name", "class":"form-control"}), label="")
	contact_person_phone = forms.CharField(widget=forms.widgets.TextInput(attrs={"placeholder":"Contact Person Phone", "class":"form-control"}), label="")
	cr_balance = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Opening Balance", "class":"form-control"}), label="")

	class Meta:
		model = Suppliers
		exclude = ("user",)


# Create Add Purchase Form
class AddPurchaseForm(forms.ModelForm):
	bill_no = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Bill No", "class":"form-control"}), label="")
	Supplier = forms.ChoiceField(required=True, widget=forms.widgets.Select(attrs={"placeholder":"Bill No", "class":"form-control"}), label="")
	purchased_date = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Bill No", "class":"form-control"}), label="")
	bill_amount = forms.DecimalField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Opening Balance", "class":"form-control"}), label="")

	class Meta:
		model = Purchases
		exclude = ("user",)

PurchasesDtlFormSet = forms.inlineformset_factory(
	Purchases,
	Purchases_Dtl,
	fields=['medicine', 'dosage', 'qty', 'price'],
	extra=1,
	can_delete=True
)