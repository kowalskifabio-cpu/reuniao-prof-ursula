import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Reunião Produtiva 2026", layout="wide")

# Título solicitado
st.title("🎯 Orientações para uma reunião produtiva")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    # SEÇÃO 1: TÉCNICAS DE COMUNICAÇÃO
    st.header("💡 Técnicas Básicas para Professores")
    
    with st.expander("🤝 Rapport (Espelhamento)", expanded=True):
        st.write("**Oriente os professores:** Começar validando o esforço dos pais por estarem ali.")
        st.info("Use frases como: 'Sabemos o quanto vocês valorizam a educação de seus filhos por estarem aqui hoje...'")

    with st.expander("🖼️ Enquadramento (Frame)", expanded=True):
        st.write("**Oriente os professores:** Definir o objetivo logo no início.")
        st.info("'Nossa reunião hoje é focada no acolhimento e na estrutura para 2026'.")

    with st.expander("✨ Linguagem Positiva", expanded=True):
        st.write("**Oriente os professores:** Em vez de 'Não podem atrasar', usar:")
        st.success("'A pontualidade garante que seu filho aproveite 100% da primeira aula'.")

    st.markdown("---")

    # SEÇÃO 2: ROTEIRO COMPLETO (30 MINUTOS)
    st.header("📅 Roteiro de 30 Minutos (Sugestão para o Professor)")
    
    tab1, tab2, tab3 = st.tabs(["1. Abertura (5 min)", "2. Conteúdo (15 min)", "3. Encerramento (10 min)"])

    with tab1:
        st.markdown("### Abertura e Alinhamento")
        st.checkbox("**Boas-vindas:** 'Sem outra regra além do amor' — cite Madre Úrsula para conectar com o coração da escola.")
        st.checkbox("**O 'Contrato' de tempo:** 'Temos 30 minutos para alinhar nossa caminhada em 2026. Focaremos na nossa identidade, rotina e avaliação'.")
        st.checkbox("**Gestão de Expectativas:** 'Para que possamos cumprir o roteiro, dúvidas específicas ou assuntos fora desses temas serão recebidos via QR Code no final para um retorno individualizado da escola'.")

    with tab2:
        st.markdown("### O Conteúdo Essencial")
        st.write("**Identidade:** Reforce os valores (Solidariedade, Respeito, Justiça e Diálogo).")
        st.write("**Rotina Eficiente:** Horários e pontualidade. Destaque o impacto positivo do uniforme e da medicação organizada.")
        
        st.divider()
        st.markdown("**Coração do Aprendizado:** Sistema de avaliação")
        st.latex(r"P1 + P2 / 2 = 6,0")
        st.write("A meta é de **24 pontos**.")
        
        st.divider()
        st.write("**Novidade:** Mencione a Sala de Recursos para Neurodivergentes (previsão Julho).")

    with tab3:
        st.markdown("### Blindagem de Conflitos e Encerramento")
        st.write("**Notas Online:** Direcione os pais para o portal para acompanhamento diário, evitando debates sobre notas isoladas na reunião.")
        st.write("**Aula de Campo:** Reforce que é uma extensão da sala de aula com foco pedagógico.")
        st.info("**O QR Code de Conexão:** Mostre o QR Code. 'Valorizamos muito sua opinião. Se algo ficou de fora hoje, escreva aqui e entraremos em contato pessoalmente'.")

with col2:
    # SEÇÃO: O QUE EVITAR
    st.header("🛠️ O que os professores devem evitar")
    st.subheader("(Gatilhos de Conflito)")
    
    st.error("**Generalizar problemas:**")
    st.write("Nunca fale: 'Essa turma tem problema com uniforme'.")
    st.success("**Diga:** 'Contamos com o apoio de vocês para mantermos a identidade visual da escola através do uniforme'.")
    
    st.divider()
    
    st.error("**Debater exceções em público:**")
    st.write("Se um pai trouxer um caso individual, o professor deve dizer:")
    st.success("'Esse ponto é muito importante e merece nossa atenção exclusiva. Por favor, registre no QR Code ou agende via agenda para conversarmos em Março'.")
    st.divider()
    if st.button("🔔 Iniciar Alerta de Tempo"):
        st.toast("Reunião Iniciada! Faltam 30 minutos.")
