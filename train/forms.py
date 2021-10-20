from django import forms

class HomeForm(forms.Form):
    post=forms.FloatField(label='heure_travail')
    post1=forms.FloatField(label='n_employes')
    post2=forms.FloatField(label='qualification')
    post3 = forms.FloatField(label='n_ouverture')
class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)