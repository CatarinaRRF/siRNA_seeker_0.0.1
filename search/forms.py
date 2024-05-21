from django import forms
from django.forms import ModelForm
from .models import model_forms

# Entrada de dados
#----------------------------------------------#

choices = (('reynolds', 'reynolds'), ('ui-tei', "ui-tei"), ('amarzguioui', "amarzguioui"))

class form_search (ModelForm):
    
    # Sequencias
    # --------------------------------------------------#
    sequence = forms.FileField(required=True)
    sequence_tag = forms.CharField()

    # Configurações siRNA
    #--------------------------------------------------#
    autor = forms.ChoiceField(choices=choices)
    size = forms.IntegerField()
    include_tm = forms.BooleanField()
    max_tm = forms.FloatField(initial=21.5)

    # Configurações Blast
    #--------------------------------------------------#
    organism = forms.CharField(required=True)
    database = forms.CharField(initial='refseq_rna')
    identity = forms.FloatField(initial=0.78)
    query_cover = forms.FloatField(initial= 0.78)
    
    class Meta:
        model = model_forms
        fields = ['sequence', 'sequence_tag', 
                  'autor', 'size', 'include_tm', 
                  'max_tm', 'organism', 'database', 
                  'identity', 'query_cover']



