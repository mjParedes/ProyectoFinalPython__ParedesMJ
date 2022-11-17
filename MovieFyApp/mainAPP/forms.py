from django import forms


class ActorFormulario(forms.Form):
    
    nombre_apellido = forms.CharField(min_length=3,max_length=50)
    origen = forms.CharField()
    edad = forms.IntegerField()


class PeliculaFormulario(forms.Form):
     
    #  nombre_apellido= forms.CharField(min_length=3,max_length=50)
    #  origen = forms.CharField()
    #  edad = forms.IntegerField()

    titulo= forms.CharField(max_length=60)
    genero = forms.CharField(max_length=30)
    director = forms.CharField(max_length=60)
    fecha_estreno = forms.DateField()
    presupuesto = forms.IntegerField()