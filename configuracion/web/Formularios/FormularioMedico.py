from django import forms
class FormularioMedico(forms.Form):
    
    ESPECIALIDADES=(
        (1, 'Cardiologia'),
        (2, 'Medico General'),
        (3, 'Medicina Interna'),
        (4, 'Ortopedia'),
        (5, 'Pediatria'), 
    )
    JORNADAS=(
        (1, '6 AM - 2 PM'),
        (2, '2 PM - 10 PM'),
        (3, '10 PM - 6 AM'),
    )
    SEDES=(
        (1, 'Almacentro'),
        (2, 'Punto Clave'),
        (3, 'Los Molinos'),
    )
    
    nombre=forms.CharField()
    apellidos=forms.CharField()
    cedula=forms.CharField()
    tarjetaProfecional=forms.CharField()
    especialidad=forms.ChoiceField()
    jornada=forms.ChoiceField()
    contacto=forms.CharField()
    sede=forms.ChoiceField()
        