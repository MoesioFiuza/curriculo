import streamlit as st
import time 
import io

st.sidebar.markdown(
    f"<a href='https://www.linkedin.com/in/mo%C3%A9sio-fi%C3%B9za-dataanalysis/' target='_blank'>LinkedIn</a> | " +
    f"<a href='https://www.instagram.com/moesiosf/?next=%2F&hl=es%2F' target='_blank'>Instagram</a>",
    unsafe_allow_html=True
)


hover_css = """
<style>
    .hover:hover {
        background-color: #f0f0f0;
        transition: all 0.3s ease-in-out;
    }
    .hover:focus {
        pointer-events: none;
        outline: none;
    }
    .contact-popup {
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background-color: white;
        padding: 20px;
        border: 1px solid #ccc;
        z-index: 1000;
    }
    .blur-background {
        filter: blur(5px);
        pointer-events: none;
    }
</style>
"""
st.markdown(hover_css, unsafe_allow_html=True)

options = {
    "Certare Engenharia e Consultoria": "Analista de Dados",
    "Grupo JB - Transcleber": "Analista de BI",
    "Despacho Rápido": "Assistente de Operações",
    "Total Express": "Auxiliar de Operações",
    "Desenvolvedor Freelancer": "Dev C# / Python",
    "Auxiliar de TI - Freelancer": "Manutenção de PCs",
    "Lojas Americanas": "Customer Success"
}

with io.open("moesi.png", 'rb') as file:
    img = file.read()

st.image(img)
st.sidebar.image("moesi.png", width=200)
st.sidebar.markdown("<h1 style='font-size: 50px; text-align: center;'>Moésio Fiùza</h1>", unsafe_allow_html=True)


selected_company = st.sidebar.selectbox("Experiência", list(options.keys()))

st.sidebar.markdown("<h1 style='text-align: left;'>Formação</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: left;'>Ciência de Dados e Machine Learning - Cruzeiro do Sul</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: left;'>Período: 02/2023 - 12/2025</p>", unsafe_allow_html=True)
st.sidebar.markdown("<h3 style='text-align: left;'>Computação em Nuvem - Unopar</h3>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: left;'>08/2022 - 12/2024</p>", unsafe_allow_html=True)


if selected_company in options:
    job_title = options[selected_company]
    if job_title == "Analista de Dados":
        job_date = "<span style='font-size: 60%;'>10/2023 - Presente</span>"
    elif job_title == "Analista de BI":
        job_date = "<span style='font-size: 60%;'>05/2023 - 10/2023</span>"
    elif job_title == "Assistente de Operações":
        job_date = "<span style='font-size: 60%;'>02/2023 - 05/2023</span>"
    elif job_title == "Auxiliar de Operações":
        job_date = "<span style='font-size: 60%;'>12/2021 - 02/2023</span>"
    elif job_title == "Dev C# / Python":
        job_date = "<span style='font-size: 60%;'>09/2015 - 12/2021</span>"
    elif job_title == "Manutenção de PCs":
        job_date = "<span style='font-size: 60%;'>10/2013 - 07/2015</span>"
    elif job_title == "Customer Success":
        job_date = "<span style='font-size: 60%;'>12/2011 - 10/2013</span>"
    else:
        job_date = ""

    st.title(selected_company)
    st.markdown(f"## {job_title} {job_date}", unsafe_allow_html=True)
    st.write("")

st.sidebar.markdown("Idiomas:")
st.sidebar.write("Inglês Fluente")
st.sidebar.write("Espanhol intermediário")
st.sidebar.write("Estudando Italiano - básico")


if selected_company == "Certare Engenharia e Consultoria":
    st.info('''Trabalhando em um Projeto de Pesquisa de Mobilidade Urbana em um consórcio junto à prefeitura de Porto Alegre.
            
   - Extração e Tratamento de dados.
            
   - Garantir a consistência e padronização dos dados no Banco de Dados.
            
   - Geração de demandas para equipe de Pesquisadores.
            
   - Criação e manutenção de dashboards via Power BI.
            
   - Geoprocessamento.
            
   - Desenvolvimento de ferramentas para ETL, Automação, Otimização de Processos via: VBA, Python, C++, C#''')

if selected_company == "Grupo JB - Transcleber":
    st.info('''Responsável pelo gestão de indicadores via Power BI.
            
   - Líder da equipe de desenvolvimento de aplicações - Solução integrada para Gestão de Frota e Financeira - Contas a Pagar e Contas a Receber.
            
   - Atuo como conselheiro técnico nas decisões de aquisição de software e hardware.
    
   - Extração, tratamento e modelagem de dados para construção de relatórios e dashboards.
    
   - Execução de processos de ETL por meio de várias técnicas, como web scraping utilizando Python Selenium/BeaufifulSoup, Kettle e autohotkeys.
            
   - Modelagem e estruturação do banco de dados.
            
   - Consolidação de dados para fornecer uma visão abrangente e unificada das operações do grupo.
            
   - Desenvolvimento e manutenção de bancos de dados, utilizando ferramentas como Access, SQL Server.
            
   - Automação de planilhas existentes e criação de novas, utilizando VBA.
            
   - Análise de indicadores-chave de desempenho''')
if selected_company == "Despacho Rápido":
    st.info('''Criação de planilhas para controle de dados.
            
   - Relatórios indicadores via Excel e Power Bi.
            
   - Análise de baixas impróprias, atrasos, etc - todas as filiais:22 lojas.
            
   - Melhoria de Processos.
            
   - Abrangência de Rotas. 
            
   - Tratativa com transportadoras parceiras. 
            
   - Tratativa de Coletas e Entregas.
            
   - Emissão de Conhecimento Eletrônico - CTe.
            
   - Responsável pela manutenção da frota.
            
   - Apoio à gestão da equipe de Operação''')

   


if selected_company == "Total Express":
    st.info('''Liderei uma equipe de 6 pessoas onde éramos responsáveis pela:

   - Realização da roteirização para otimizar as entregas, garantindo a eficiência do processo logístico.
    
   - Acompanhamento e suporte à performance dos motoristas, monitorando indicadores-chave.
    
   - Tratativa dos insucessos de entrega (NC CX e NC LM), buscando soluções eficientes para melhorar a qualidade das operações.
    
   - Logística Reversa para lidar com os produtos retornados e garantir a redistribuição adequada.
    
   - Elaboração de relatórios indicadores, utilizando o Excel, para apresentar dados relevantes à supervisão e coordenação, apoiando as decisões estratégicas e melhorias operacionais.''')
if selected_company == "Desenvolvedor Freelancer":
    st.info('''Construção de Scripts em C# e C++ para o programa Livesplit.
    
   -Programas para leitura de memória, primariamente para jogos;
    
   -Construção de Scripts e Plugins para OBS usando Python e Lua:
        
   - Push to Hide/Show Hotkeys;
        
   - Alerta customizado de inscritos/seguidores;
        
   - Transição de cenas customizado;
        
   - Chat Bots;
        
   - Separação de áudio/vídeo via scripts usando MoviePy e FFmpeg.
    
   - Builds customizadas de Linux usando Linux From Scratch.''')
if selected_company == "Auxiliar de TI - Freelancer":
    st.info('''Montagem de computadores;
    
   -Formatação e instalação: Windows e Linux.''')
if selected_company == "Lojas Americanas":
    st.info("Atendimento ao Cliente - CX")        


if st.sidebar.button("Contato", key="contact_button"):
    popup_state = st.session_state.get("popup_state", False)

    if popup_state:
        st.markdown("<script>document.getElementById('contact-popup').style.display = 'none';</script>", unsafe_allow_html=True)
        st.session_state["popup_state"] = False
    else:
        expanded_html = """
        <style>
        .contact-popup {
            background-color: black;
            color: white;
            padding: 20px;
            border-radius: 50px;
            position: absolute;
            top: 70%;
            left: 50%;
            transform: translate(-50%, -50%);
            z-index: 9999;
        }
        </style>
        <div class="contact-popup" id="contact-popup">
            <h2>Contato</h2>
            <p>E-mail: m0es10.mf@gmail.com<br>Fone: (85) 9 92950650</p>
        </div>
        """
        st.markdown(expanded_html, unsafe_allow_html=True)
        st.session_state["popup_state"] = True

opcao_download = st.selectbox("Selecione o formato de download:", ["PDF", "DOCX"])

cv_pdf_link = "https://drive.google.com/uc?export=download&id=1yZkNU86_Owd1-sY5nzALux-R71Q8uyd8"  
cv_docx_link = "https://drive.google.com/uc?export=download&id=1V2GDgZ_SD5Noj_JVWXMDcdmXgr_Hk_U4"

if opcao_download == "PDF":
    st.markdown(f"[Baixe meu CV em PDF aqui]({cv_pdf_link})", unsafe_allow_html=True)
elif opcao_download == "DOCX":
    st.markdown(f"[Baixe meu CV em DOCX aqui]({cv_docx_link})", unsafe_allow_html=True)


images_info = [
    {"src": "python-logo.png", "width": 100},
    {"src": "ppsheet-vector-logo-2022.png", "width": 100},
    {"src": "C#.png", "width": 100},
    {"src": "c++.png", "width": 100},
    {"src": "excel.png", "width": 100},
    {"src": "post.png", "width": 100},
    {"src": "QGIS.png", "width": 100},
    {"src": "power.png", "width": 100},
    {"src": "zure.png", "width": 100}
]

images_infos_2 = [
    {"src": "python-logo.png", "width": 100},
    {"src": "excel.png", "width": 100},
    {"src": "power.png", "width": 100},
    {"src": "Google_Sheets_Logo_512px.png", "width": 100},
    {"src": "zure.png", "width": 100},
    {"src": "server.png", "width": 100},
]

images_infos_3 = [
    {"src": "excel.png", "width": 100},
    {"src": "power.png", "width": 100},
    {"src": "zure.png", "width": 100},
    {"src": "post.png", "width": 100},
    {"src": "ssw.png", "width": 100},
]

images_infos_4 = [
    {"src": "excel.png", "width": 100},
    {"src": "power.png", "width": 100},
    {"src": "Google_Sheets_Logo_512px.png", "width": 100},
    {"src": "server.png", "width": 100},
]

images_infos_5 = [
    {"src": "C#.png", "width": 100},
    {"src": "c++.png", "width": 100},
    {"src": "python-logo.png", "width": 100},
    {"src": "C_Logo.png", "width": 100},
    {"src": "Linux.png", "width": 100},
]

def fade_image(image_info, column):
    with column:
        st.image(image_info["src"], width=image_info["width"])

if selected_company == "Certare Engenharia e Consultoria":
    st.info("Principais tecnologias usadas:")
    
    num_columns = 3
    columns = st.columns(num_columns)

    for img_info in images_info:
        fade_image(img_info, columns[0])
        time.sleep(0.3)  
        columns = columns[1:] + columns[:1]

if selected_company == "Grupo JB - Transcleber":
    st.info("Principais tecnologias usadas:")

    num_columns = 3
    columns = st.columns(num_columns)
    for img_info in images_infos_2:
        fade_image(img_info, columns[0])
        time.sleep(0.3)  
        columns = columns[1:] + columns[:1]

if selected_company == "Despacho Rápido":
    st.info("Principais tecnologias usadas:")
    
    num_columns = 3
    columns = st.columns(num_columns)

    for img_info in images_infos_3:
        fade_image(img_info, columns[0])
        time.sleep(0.3)  
        columns = columns[1:] + columns[:1]

if selected_company == "Total Express":
    st.info("Principais tecnologias usadas:")
    
    num_columns = 3
    columns = st.columns(num_columns)

    for img_info in images_infos_4:
        fade_image(img_info, columns[0])
        time.sleep(0.3)  
        columns = columns[1:] + columns[:1]

if selected_company == "Desenvolvedor Freelancer":
    st.info("Principais tecnologias usadas:")
    
    num_columns = 3
    columns = st.columns(num_columns)

    for img_info in images_infos_5:
        fade_image(img_info, columns[0])
        time.sleep(0.3) 
        columns = columns[1:] + columns[:1]