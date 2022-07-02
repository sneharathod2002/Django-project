from django import forms 


from .models import product 

class productForm(forms.ModelForm):
	title       = forms.CharField(label='', 
		widget=forms.TextInput(attrs={"placeholder":"your title"}))
	email       = forms.EmailField()
	description = forms.CharField(
    	required=False ,
    	widget=forms.Textarea(
    	 attrs={
    	 	"placeholder":"your description",
    	 	"class": "new-class-name two",
    	 	"id": "my-id-for-textarea",
    	 	"rows": 20,
    	 	"cols": 120
    	 	}
    	 	)
    	 )
	price = forms.DecimalField(initial=99.99) 
	class Meta:
		model = product 
		fields = [
			'title',
			'description',
			'price'
		]


def clean_title(self, *args, **kwargs):
    	title= self.cleaned_data.get("title")
    	if not "CFE" in title:
    		raise forms.ValidationError("this is not a valid title")
    	return title


def clean_email(self, *args, **kwargs):
    	title= self.cleaned_data.get("email")
    	if not email.endswith("edu"):
    		raise forms.ValidationError("this is not a valid email")
    	return email
    	
    		








    	



class RawproductForm(forms.Form):
    title       = forms.CharField(label='', widget=forms.TextInput(attrs={"placeholder":"your title"}))
    description = forms.CharField(
    	required=False ,
    	 widget=forms.Textarea
    	 (attrs={
    	 	"placeholder":"your description",
    	 	"class": "new-class-name two",
    	 	"id": "my-id-for-textarea",
    	 	"rows": 20,
    	 	"cols": 120
    	 	}
    	 	)
    	 )
    price       = forms.DecimalField(initial=199.99)		