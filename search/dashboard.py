import pandas as pd
import json
import networkx as nx
# ----------------------------------------------------------------------------------- #



# Visualização Blast

def grafo_blast (tuplas, identidade):
  #Ajustando a identidade
  identidade_float = [float(i) for i in identidade] # Ajuste para float
  identidade_ajuste = [(i**5) * 4000 for i in identidade_float] # Ajustando tamanho
  identidade_ajuste
  # Criando uma lista para as cores
  edge_colors = []
  for i in identidade_float:
    if i == 1.0:
      edge_colors.append('#D64045')
    else:
      edge_colors.append('#00ab44')
  # Criando o grafico
  g = nx.star_graph(tuplas)
  pos = nx.spring_layout(g)

  #Criando Labels
  labels = {node: node[1] for node in g.nodes()}

  # Editando a aparencia do grafico
  options = {
    # Configuração dos nodos
    "node_color": "w",
    "with_labels": True,
    # Bordas dos nodos
    'linewidths': 1.5,
    'edgecolors': edge_colors,
    # Configuração das linhas
    "edge_color": "#353744",
    "width": 2,
    "arrows": True,
    "arrowstyle": "-|>",
    "node_size":identidade_ajuste, #ajusta o tamanho de acordo com a identidade
    # Configuração do grafhos
    "font_size":8,
    "font_color":"#353744",
    'labels':labels,
  }
  a = nx.draw(g, pos, **options)

  return a

# Visualização Alinhamento
def alignment ():

    return 
    