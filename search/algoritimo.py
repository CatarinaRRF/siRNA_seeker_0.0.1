# Importando
#--------------------#
## Tratamento dos dados
#--------------------#
import Bio
from Bio import SeqIO, Entrez
from Bio.Seq import Seq
## Filtros
#--------------------#
from Bio.SeqUtils import MeltingTemp as mt
from Bio.SeqUtils import gc_fraction
from seqfold import dg
import pandas as pd
## Blast
#--------------------#
from Bio.SeqRecord import SeqRecord
from Bio.Blast import NCBIWWW, NCBIXML

#sequence = 'seqence.fasta'

# Algoritmo
#-------------------------------------------------------------#
def salvar_arquivo(self, nome_arquivo, conteudo):
    with open(nome_arquivo, 'w') as file:
        file.write(conteudo)

def upload_fasta(self, sequence):
    if sequence:
        with open(sequence, 'r') as file:
            conteudo = file.read()
            self.salvar_arquivo("meugene.fasta", conteudo)

def buscar_fasta_online(self, gene_id):
    handle = Entrez.efetch(db="nucleotide", id=gene_id, rettype="fasta", retmode="text")
    return handle.read()

def pesquisar_genes(self, sequence_tag):
    if sequence_tag:
        fasta_content = self.buscar_fasta_online(sequence_tag)
        self.salvar_arquivo("meugene.fasta", fasta_content)

# sequencias == resultados do parse ("meugene.fasta")
def transcrever(arquivo):
    sequencias = list(SeqIO.parse(arquivo, 'fasta'))
    for sequencia in sequencias:
        name = sequencia.name
        # Converte as letras T para U
        sequencia_convertida = Bio.Seq.transcribe(sequencia.seq)
    return sequencia_convertida

# Achando todas as possiveis sequencias de siRNA dado == sequencias trascritas
# ----------------------------------------------------------------- #
def possiveis_siRNA(dado, tamanho=21):
    # definindo variaveis
    possiveis_siRNA = []
    tuplas = []
    # iterando
    for index, _ in enumerate(dado):
        f = index + tamanho
        sequence_p = Seq(dado[index:f])  # convertendo para objeto Seq
        possiveis_siRNA.append(str(sequence_p))
        tuplas.append((str(sequence_p), index))
    
    siRNA = possiveis_siRNA[:-tamanho]
    tuplas = tuplas[:-tamanho]

    return siRNA

# Classificação dos siRNA quando sua funcionalidade
# ----------------------------------------------------------------- #

# Reynolds 
# ---------------------------------------------- #
def reynolds (sequence):
    score = 0
    falha = []
    # Instabilidade na posição 15 - 19
    #----------------------------------#
    check_estabilidade = 0
    for letra in sequence[14:19]:
        if letra == "A" or letra == "G":
            check_estabilidade += 1
    if check_estabilidade >= 1:
        score += 1
    else:
        falha.append(str("estabilidade interna"))
    # Posição 13
    #----------------------------------#
    if sequence[12] != "G":
        score += 1
    else:
        falha.append(str("posição 13"))
    # Posição 19
    #----------------------------------#
    if sequence [18] != "G" and sequence [18] != "C":
        score += 1
    else:
        falha.append(str("posição 19"))
    if sequence [18] == "A":
        score += 1
    else:
        falha.append(str("posição 19!= A"))
    # Posição 10
    #----------------------------------#
    if sequence [9] == "U":
        score += 1
    else:
        falha.append(str("posição 10"))

    # Posição 3
    #----------------------------------#
    if sequence [2] == "A":
        score += 1
    else:
        falha.append(str("posição 3"))

    return score, falha

# Ui-Tei
# ---------------------------------------------- #
def Ui_Tei (sequence, extremidade=7):
    # Variaveis
    #----------------------------------#
    score = 0
    falha = []
    antisenso = Seq(sequence).complement_rna()

    #Senso
    #----------------------------------#
    check_senso = 0

    for letra in sequence[:extremidade]:
        if letra == "G" or letra == "C":
            check_senso += 1
    if check_senso == 5:
        score += 1
    else:
        falha.append(str("Extremidade senso"))

    #Antisenso
    #----------------------------------#
    check_antisenso = 0

    for letra in antisenso[-extremidade:]:
        if letra == "A" or letra == "U":
            check_antisenso += 1
    if check_antisenso == extremidade:
        score += 1
    else:
        falha.append(str("Extremidade antisenso"))

    # Presença de no minimo 5 A/U nas posições [:7]
    #----------------------------------#
    check_min_5 = 0

    for letra in antisenso[-7:]:
        if letra == "A" or letra == "U":
            check_min_5 += 1
    if check_min_5 >= 5:
        score += 1
    else:
        falha.append(str("posições [:7]"))

    # Mais de 9 repetições
    #----------------------------------#
    segment_size = 9
    check = True

    for index in range(len(sequence) - segment_size + 1):
            segmento = sequence[index:index + segment_size]
            count = 0
            for letra in segmento:
                if letra == 'C' or letra == 'G':
                    count += 1
            if count >= segment_size:
                check = False

    if check == True:
        score += 1
    else:
        falha.append(str("Repetição de mais de 9 C/G seguidos"))

    return score, falha

# Amarzguioui
# ---------------------------------------------- #
def Amarzguioui(sequence):
    score = 0
    falha = []
    check_assimetria_5 = 0
    check_assimetria_3 = 0
    antisenso = Seq(sequence).complement_rna()

    # Posição 1
    #----------------------------------#
    if sequence [0] != "U" and sequence [0] != "A":
        score += 1
    else:
        falha.append(str("posição 1"))
    # Posição 6
    #----------------------------------#
    if sequence [5] == "A":
        score += 1
    else:
        falha.append(str("posição 6"))
    # Posição 19
    #----------------------------------#
    if sequence [18] != "G" and sequence [18] != "C":
        score += 1
    else:
        falha.append(str("posição 19"))
    # Assimetria
    #----------------------------------#
    for letra in sequence[:3]:
        if letra == "A" or letra == "U": # baixo
            check_assimetria_5 += 1
    for letra in antisenso[-3:]:
        if letra == "A" or letra == "U": # alto
            check_assimetria_3 += 1
    if check_assimetria_3 > check_assimetria_5:
        score += 1
    else:
        falha.append(str("assimetria"))

    return score, falha

    # Testando a funcionalidade de um siRNA
    # ---------------------------------------------- #

def siRNA_score (sequence,
                    autor=['reynolds', 'ui-tei', 'amarzguioui'],
                    tm=True, tmmax = 21.5):

    # Definindo variaveis
    #--------------------------------------------------------------#
        score = 0
        falha = []

        # Conteudo Baixo GC
        #--------------------------------------------------------------#
        conteudo_gc = round(gc_fraction(sequence)*100, 2)
        if 30 <= conteudo_gc <= 52:
            score += 1
        else:
            falha.append(str("Conteudo CG"))

        # tempmelt
        #--------------------------------------------------------------#
        if tm == True:
            tm_score = round(mt.Tm_GC(sequence[1:8]), 2)
            if tm_score <= tmmax:
                score += 1
            else:
                falha.append(str("tm"))

        # G°
        #--------------------------------------------------------------#
        energia_livre = dg(sequence)
        if -13 < energia_livre < -7:
            score += 2
        else:
            falha.append(str("Energia livre"))

        # Autores
        # Score reynolds total = 6
        #--------------------------------------------------------------#
        if autor == 'reynolds':
            r = reynolds(sequence)
            score += r[0]
            falha.append(str(r[1]))

        # Score ui-tei total = 4
        #--------------------------------------------------------------#
        if autor == 'ui-tei':
            u = Ui_Tei(sequence)
            score += u[0]
            falha.append(str(u[1]))

        # Score amarzguioui total = 4
        #--------------------------------------------------------------#
        if autor == 'amarzguioui':
            a = Amarzguioui(sequence)
            score += a[0]
            falha.append(str(a[1]))
        #--------------------------------------------------------------#

        return score, falha, conteudo_gc, energia_livre, tm_score

# Selecionando os siRNA funcionais
# ---------------------------------------------- #
def filtro_siRNA(sequences, conformidade=0.6,
                    autor=['reynolds', 'ui-tei', 'amarzguioui'],
                    tm=True, tmmax=21.5):

        # Definindo Variaveis
        # --------------------------------------------------------------#
        siRNA_verificados = []
        posicao = []
        score = []
        falha = []
        conteudo_gc = []
        energia_livre = []
        TM_score = []

        total_reynolds = round(10 * conformidade)
        total_uitei_ama = round(8 * conformidade)

        # Iterador
        # --------------------------------------------------------------#
        for index, sequence in enumerate(sequences):
            # Veficando a qualidade
            # ----------------------------------#
            resultado = siRNA_score(sequence=sequence, autor=autor,
                                    tm=tm, tmmax=tmmax)

            # Exclui RNAs indesejadas
            # ----------------------------------#
            incluir_siRNA = True

            if autor == "reynolds":
                if resultado[0] <= total_reynolds or resultado[4] > tmmax:
                    incluir_siRNA = False

            if autor == 'ui-tei' or autor == 'amarzguioui':
                if resultado[0] <= total_uitei_ama or resultado[4] > tmmax:
                    incluir_siRNA = False

            if incluir_siRNA:
                siRNA_verificados.append(sequence)
                posicao.append(index)
                score.append(resultado[0])
                falha.append(resultado[1])
                conteudo_gc.append(resultado[2])
                energia_livre.append(resultado[3])
                TM_score.append(resultado[4])

            # Pandas
        dataset = pd.DataFrame({
                                "siRNA_verificados": siRNA_verificados,
                                "posicao_alinhamento": posicao,
                                "pontuacao": score,
                                "temperatura_de_melting": TM_score,
                                "conteudo_CG": conteudo_gc,
                                "energia_livre": energia_livre,
                                "falhas": falha
                                })
        dataset = dataset.sort_values(by=["pontuacao"],
                                    ascending=False, ignore_index=True)
        dataset = dataset.to_json()
        print(f'existem {len(siRNA_verificados)}sequencias')

        return dataset, siRNA_verificados

# Blast
# ----------------------------------------------------------------- #

# Fasta com as sequencias funcionais
# ---------------------------------------------- #    
def guardando_sequence (data):
        records = []
        for index, sequence in enumerate(data):
            # Criando o cabeçalho enumerado
            header = f"sequencia_{index+1}"

            # Criando um objeto SeqRecord com a sequência e o cabeçalho
            record = SeqRecord(Seq(sequence), id=header, description="")

            # Adicionando o registro à lista
            records.append(record)

        # Salvando os registros no arquivo FASTA
        fasta_filename = "minha_sequencia.fasta"
        with open(fasta_filename, "w") as output_file:
            SeqIO.write(records, output_file, "fasta")
        return fasta_filename

# Rodando o Blast
# ---------------------------------------------- #    
def blast_siRNA (sequence , sequence_tag, db = None, organismo = "txid9606[ORGN]",
                 df=None, identidade=0.78):

        # Variaveis
        description = []
        identidade = []

        result_handle = NCBIWWW.qblast(
                                             program=df, database=db,
                                             sequence = sequence,
                                             entrez_query=organismo,
                                             perc_ident=identidade
                                           )

        # Parsear os resultados do BLAST
        blast_records = NCBIXML.parse(result_handle)

        for blast_record in blast_records:
            for alignment in blast_record.alignments:
                  hit = alignment.hsps[0]  # Pega apenas o melhor alinhamento
                  # Extrair informações relevantes
                  description.append(str(alignment.hit_id[18:])) # Name

                  p_i = hit.identities / hit.align_length # Identidade
                  identidade.append(str(p_i))
                  #cobertura = hit.align_length / hit.query_length

        # Preprarando os dados para a criação do grafo
        tuplas = [(sequence_tag, valor) for valor in description]

        return tuplas, identidade#, cobertura

def identidade_siRNA(fasta_file="minha_sequencia.fasta", sequence_tag=None, db = "refseq_rna", organismo = "txid9606[ORGN]",
                 df=None, identidade=0.78):
  # Ler o arquivo fasta
    sequences = list(SeqIO.parse(fasta_file, "fasta"))

  # Realizar o BLAST para cada sequência
    for i, sequence in enumerate(sequences, start=1):
        print(f"Processando sequência {i}...")

        # Blast
        tuplas_blast, identity = blast_siRNA (sequence , sequence_tag, 
                                                           db, organismo,
                                                            df, identidade)

    return tuplas_blast, identity
