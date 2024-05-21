> <B>⚠️Este README ainda esta sob desenvolvimento</B>

<h1 align="center">
  <img src="https://raw.githubusercontent.com/CatarinaRRF/IC_design_de_siRNA/main/media/Creative.png" alt="logo">
</h1>

<p align="center">
    <a href="">
    <img src="https://img.shields.io/github/last-commit/CatarinaRRF/siRNA_seeker_0.0.1?color=informational&style=flat-square"
         alt="GitHub last commit">
    <a href="https://github.com/CatarinaRRF/Challenge-Alura-Cash-19-08-22">
    <img src= http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=green&style=flat-square >

</p>

<p align="center">
  <a href="#sobre">Sobre</a> •
  <a href="#inicializando">Inicializando</a> •
  <a href="#softwares">Softwares</a> •
  <a href="#versionamento">Versionamento</a> •
  <a href="#licença">Licença</a> •
  <a href="#creditos">Créditos</a>
  
</p>

### 🌌 Ajustes e melhorias

O projeto ainda está em desenvolvimento e as próximas atualizações serão voltadas nas seguintes tarefas:

- [ ] Produzir o dashboard
- [ ] Fazer os graficos de visualização em javascript
- [ ] Fazer upload no servidor
- [ ] Fazer documentação e pagina inicial

# Sobre 
<p align="justify"> O siRNA Seeker é um webapp desenvolvido utilizando o framework Django em Python para disponibilizar o algoritmo de design de siRNA produzido pelo grupo de pesquisa <???> à comunidade científica. Esta aplicação web oferece uma interface amigável e acessível para que os pesquisadores possam utilizar o algoritmo de seleção de siRNA de forma eficiente e conveniente. Por meio deste webapp, os usuários têm a capacidade de realizar análises de design de siRNA de maneira interativa, personalizando parâmetros e recebendo resultados precisos e relevantes. A utilização do Django permite uma implementação robusta e escalável, garantindo que o webapp possa atender às demandas da comunidade científica e promover avanços na pesquisa em biotecnologia. O objetivo é que o acesso ao web app esteja disponível online, proporcionando uma plataforma centralizada para compartilhamento de conhecimento e colaboração entre os membros da comunidade científica interessados na área de design de siRNA. Desse modo, as seguintes partes do aplicativo já foram desenvolvidas:

> ⚙️ Acesse mais informações sobre o algoritimo produzido [aqui](https://github.com/CatarinaRRF/IC_design_de_siRNA)

1. Landing Page - Main:
Há um banner com imagem e um botão para iniciar o design do siRNA, que direciona para o Formulário (onde o usuário insere os parâmetros).
São apresentadas informações sobre o algoritmo, importância para o design de siRNA e opção de contato, e informações sobre o grupo.
2. Formulário:
É possível inserir arquivo fasta, copiar e colar o texto ou colocar a tag para buscar.
Os usuários podiam escolher autor, tamanho do siRNA, calcular Tm, ™ max, intervalo de energia livre e mínimo de conformidade.
Ao clicar no botão de enviar, os usuários são direcionados para o app Loading.
3. Loading:
Mostra o tempo esperado para completar a tarefa e o progresso.
Quando completo, os usuários são direcionados para o Dashboard.
4. Dashboard:
Exibe o gene sendo analisado, a quantidade de sequências selecionadas e uma tabela comparativa para todas as sequências possíveis.
Blocos de texto indicam falhas de parâmetros , descrevendo e classificando a gravidade.
5. Conta:
Página padrão de login e registro de usuários.
As contas podem salvar resultados por vez


## Inicializando

Estas instruções ajudarão a obter uma cópia do projeto em execução em sua máquina local para fins de desenvolvimento e teste. Veja implantação para notas sobre como implantar o projeto em um sistema ao vivo.

### Pré-requisitos

Para iniciar este projeto, você precisará do seguinte:

- [Django](https://docs.djangoproject.com/pt-br/3.2/) - Framework web em Python
- [Celery](https://docs.celeryproject.org/en/stable/django/index.html) - Para execução de tarefas em segundo plano

Caso seu sistema operacional seja Windows ou MacOS, também será necessario os seguintes programas:
- [Redis](https://redis.io/documentation) - Sistema de mensagens e cache
- Emulador de Linux, como [WSL](https://docs.microsoft.com/pt-br/windows/wsl/install)

### Instalação

Uma série passo a passo de exemplos que mostram como colocar um ambiente de desenvolvimento em execução

🛠️ <b>Clone este repositório para o seu ambiente local</b>

<code>git clone https://github.com/CatarinaRRF/siRNA_seeker_0.0.1.git</code>

🛠️ <b>Navegue até o diretório do projeto</b>

<code>cd siRNA_seeker_0.0.1</code>

🛠️ <b>Instale as dependências necessárias</b>

<code>pip install -r requirements.txt</code>

## Softwares

* [Django](https://www.djangoproject.com/) - O framework web usado
* [Python](https://www.python.org/) - Usado para a produção do algoritmo
* [Javascript]() - Usado para a produção de gráficos

## Versionamento

O versionamento utilizado foi o [Git](https://git-scm.com/). 

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE.md](LICENSE.md) para obter detalhes

## Créditos
* Universidade Federal de Uberlândia (UFU) - Campus Patos de Minas
* Equipe de desenvolvimento: Catarina RRF, Valdeir de Paula e Matheus Souza
<img src="https://github.com/CatarinaRRF/Challenge-Alura-Cash-19-08-22/blob/974dd832c3980dd107a36a4b6906b616bb7b71f2/media/hr_line_redme.png" alt="logo">
<p align="center">
