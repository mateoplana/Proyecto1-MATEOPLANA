from django import forms

class userformulario(forms.Form):

    nombre= forms.CharField(label="Nombre", max_length=30)
    usuario= forms.CharField(label="Usuario", max_length=30)
    antiguedad= forms.IntegerField(label="antiguedad")

class modformulario(forms.Form):

    nombre= forms.CharField(label="Nombre", max_length=30)
    usuario= forms.CharField(label="Usuario", max_length=30)
    email= forms.EmailField(label="Email")

class usuarioflformulario(forms.Form):

    nombre= forms.CharField(label="Nombre", max_length=30)
    usuario= forms.CharField(label="Usuario", max_length=30)
    antiguedad= forms.IntegerField(label="antiguedad")