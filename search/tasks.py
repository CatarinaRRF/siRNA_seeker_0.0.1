from celery import shared_task
from celery_progress.backend import ProgressRecorder
from time import sleep
from .algoritimo import *

@shared_task(bind=True)
def selection (self, sequence, sequence_tag, 
                  autor, size, include_tm, 
                  max_tm, organism, database, 
                  identity, query_cover):
    
    progress_recorder = ProgressRecorder(self)

    ## Selection of sequences
    progress_recorder.set_progress(10, 100, description='Transcribing sequences')
    trascribe = transcrever(sequence) #trascreve os dados
    candidates = possiveis_siRNA(trascribe, tamanho=size)


    ## Selection on base of actors
    progress_recorder.set_progress(30, 100, description='Filtering siRNA candidates')
    table, sirna_verified = filtro_siRNA(candidates, conformidade=0.6,
                                          autor=autor,
                                          tm=include_tm, tmmax=max_tm)
    
    ## Blast
    progress_recorder.set_progress(50, 100, description='Running Blast')
    sirna_verified_fasta = guardando_sequence (sirna_verified)

            ##### ADICIONAR O QUERY_COVER
    tuplas_blast, identidade = identidade_siRNA(fasta_file= sirna_verified_fasta, 
                                                sequence_tag=sequence_tag, db = database, 
                                                organismo = organism, df="blastn", identidade=identity)
    
    ## Meta
    progress_recorder.set_progress(30, 100, description='Filtering siRNA candidates')


    return table, tuplas_blast, identidade,  sirna_verified, #query_cover
