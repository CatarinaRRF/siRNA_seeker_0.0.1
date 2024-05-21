from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
import os
from celery.result import AsyncResult
from django.core.serializers.json import DjangoJSONEncoder
import json

from search.forms import form_search
from .models import model_forms
from .algoritimo import *
from .tasks import *
from .dashboard import *

# Create your views here.
#----------------------------------------------#
# Forms to search
#----------------------------------------------#

@login_required(redirect_field_name='next',login_url="/accounts/login/")
def teste_view (request):  
    form = form_search()    
    print(request.FILES)
    if request.method == "POST":
        form = form_search(request.POST, request.FILES)
        if form.is_valid():
            form_instance = form.save(commit=False)
            form_instance.user = request.user
            form.save()
            form.cleaned_data
            return HttpResponseRedirect("/loading/")
    return render (request, 'form.html', {'form': form})

#----------------------------------------------#
# Usando os dados
#----------------------------------------------#
 

# Loading
#----------------------------------------------#
@login_required(redirect_field_name='next',login_url="/accounts/login/")
def loading (request):
        #if 'pp_teste_view' in request.session:
            
            ## Geting Data
            model_forms_data = model_forms.objects.filter(user=request.user).last()
            
            _directory = 'media'
            
            ####criando o path para a sequencia
            sequence = str(model_forms_data.sequence)
            sequence_path = os.path.join(_directory, sequence)

            ####Armazenando outras variaveis
            sequence_tag = str(model_forms_data.sequence_tag)
            autor = model_forms_data.autor
            size = int(model_forms_data.size)
            include_tm = bool(model_forms_data.include_tm)
            max_tm = float(model_forms_data.max_tm)
            organism = model_forms_data.organism
            database = model_forms_data.database
            identity = float(model_forms_data.identity)
            query_cover = float(model_forms_data.query_cover)

            #Run celery Task if that is a registry in database
            
            if model_forms_data:
                task = selection.delay(sequence_path, sequence_tag, autor, 
                                        size, include_tm, max_tm, organism,
                                        database, identity, query_cover)

            return render (request, 'loading.html', {'task_id': task.task_id})
            
        #del request.session['pp_teste_view']



@login_required(redirect_field_name='next',login_url="/accounts/login/")

def dashboard(request):
    # Pegar informações da task
    task_id = "ffd4457a-5e29-4841-b615-e8e81349feb5"
    task_result = AsyncResult(task_id)
    table, tuplas_blast, identidade = task_result.get() #sirna_verified

    # Fazer Tabela
    
    tables = pd.read_json(table)
    json_records = tables.reset_index().to_json(orient ='records')
    arr = []
    arr = json.loads(json_records)
    print(f"arr is {arr}")
    contextt = {'d': arr}

    # Fazer Graficos
    #graph_alignment = alignment(cache_key)
    #graph_blast = grafo_blast (tuplas_blast, identidade)
    
    return render(request, 'dashboard.html', contextt #{'graph_data': graph_alignment, 
                                              #'graph_blast': graph_blast,
                                              #'json_data': table}
                                              )
