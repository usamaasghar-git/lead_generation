from django import forms
from .models import Buyer, Seller, Realtor,Rent,Blog

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyer
        fields = ['first_name', 'last_name', 'current_address', 'area_zip_code', 'email', 'budget']
        widgets = {
            'current_address': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Buyer.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

class SellerForm(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ['first_name', 'last_name', 'current_address', 'area_zip_code', 'email', 'budget']
        widgets = {
            'current_address': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Seller.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

class RealtorForm(forms.ModelForm):
    class Meta:
        model = Realtor
        fields = ['first_name', 'last_name', 'current_address', 'area_zip_code', 'email', 'subscription']
        widgets = {
            'current_address': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Realtor.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

class RentForm(forms.ModelForm):
    class Meta:
        model = Rent
        fields = ['first_name', 'last_name', 'current_address', 'area_zip_code', 'email', 'budget', 'rent_type', 'bedrooms', 'min_price_range', 'max_price_range']
        widgets = {
            'current_address': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if Rent.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered for a rental.")
        return email

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if Blog.objects.filter(title=title).exists():
            raise forms.ValidationError("A blog post with this title already exists.")
        return title