from django import forms


def Check_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError("name should not starts with 'a' ")
    
def Check_for_lengh(value):
    if len(value)>6:
        raise forms.ValidationError("morethan six character are not allowed in name")
# def Check_for_ema(value):
#     if value[0].isalnum():
#         raise forms.ValidationError("email startswith only alphabeths") 

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[Check_for_a])
    age=forms.IntegerField()
    email=forms.EmailField()
    re_enter_email=forms.EmailField()
    botcatcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)


    def clean(self):
        e=self.cleaned_data['email']
        r=self.cleaned_data['re_enter_email']
        if e!=r:
            raise forms.ValidationError("Email is not matching")
    
    def clean_botcatcher(self):
        bot=self.cleaned_data['botcatcher']
        if len(bot)>0:
            raise forms.ValidationError("data not allowing bot catcher")
    