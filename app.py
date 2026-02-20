import streamlit as st

# Configuração da Página
st.set_page_config(page_title="Estratégia PNL para Professores", layout="wide", page_icon="🧠")

# Título Principal
st.title("🧠 Estratégia PNL para Professores: Reunião 2026")
st.markdown("---")

# Colunas para organizar a visualização
col1, col2 = st.columns([2, 1])

with col1:
    # SEÇÃO 1: TÉCNICAS PNL
    st.header("🛠️ Técnicas de PNL Aplicadas")
    
    with st.expander("🤝 Rapport (Espelhamento) - Clique para ver detalhes"):
        st.write("**Ação:** Começar validando o esforço dos pais por estarem ali.")
        st.info("💡 Exemplo: 'Sabemos o quanto vocês valorizam a educação de seus filhos por estarem aqui hoje...'")

    with st.expander("🖼️ Enquadramento (Frame) - Clique para ver detalhes"):
        st.write("**Ação:** Definir o objetivo logo no início para evitar distrações.")
        st.info("💡 Exemplo: 'Nossa reunião hoje é focada no acolhimento e na estrutura para 2026'.")

    with st.expander("✨ Linguagem Positiva - Clique para ver detalhes"):
        st.write("**Ação:** Foque no benefício em vez da proibição.")
        st.success("✅ Troque: 'Não podem atrasar' por: 'A pontualidade garante que seu filho aproveite 100% da primeira aula'.")

    st.markdown("---")

    # SEÇÃO 2: ROTEIRO DETALHADO
    st.header("📅 Roteiro de 30 Minutos")
    
    tabs = st.tabs(["1. Abertura (5 min)", "2. Conteúdo Essencial (15 min)", "3. Encerramento (10 min)"])

    with tabs[0]:
        st.markdown("### 🕊️ Abertura e Alinhamento")
        st.checkbox("Boas-vindas: Citar Madre Úrsula ('Sem outra regra além do amor') para conectar com o coração.")
        st.checkbox("O 'Contrato' de tempo: Reforçar os 30 minutos para alinhar a caminhada de 2026.")
        st.checkbox("Gestão de Expectativas: Avisar que dúvidas específicas serão via QR Code para retorno individualizado.")

    with tabs[1]:
        st.markdown("### 🏫 O Coração do Aprendizado")
        st.markdown("**1. Identidade:** Reforce os valores: *Solidariedade, Respeito, Justiça e Diálogo*.")
        st.markdown("**2. Rotina Eficiente:** Horários, uniforme e organização de medicação.")
        
        st.divider()
        st.markdown("**3. Sistema de Avaliação:**")
        st.latex(r"\frac{P1 + P2}{2} = 6,0")
        st.caption("Meta anual: 24 pontos.")
        
        # Simulador para interação com os pais
        p1 = st.slider("Nota P1", 0.0, 10.0, 6.0)
        p2 = st.slider("Nota P2", 0.0, 10.0, 6.0)
        st.metric("Resultado da Média", f"{(p1+p2)/2:.1f}")

        st.divider()
        st.markdown("**4. Novidade:** Sala de Recursos para Neurodivergentes (Previsão Julho).")

    with tabs[2]:
        st.markdown("### 🛡️ Blindagem e Conexão")
        st.markdown("- **Notas Online:** Direcione para o portal para acompanhamento diário.")
        st.markdown("- **Aula de Campo:** Reforce o foco pedagógico (extensão da sala).")
        st.info("📸 **O QR Code de Conexão:** Mostre o QR Code agora e valorize a opinião individual.")

with col2:
    # SEÇÃO DE SEGURANÇA (O QUE EVITAR)
    st.header("⚠️ Gestão de Conflitos")
    
    st.error("**NÃO Generalize:** Nunca diga 'Essa turma tem problema com uniforme'.")
    st.success("**Diga:** 'Contamos com o apoio de vocês para manter a identidade visual através do uniforme'.")
    
    st.divider()
    
    st.error("**NÃO Debata Exceções:** Evite casos individuais em público.")
    st.success("**Diga:** 'Esse ponto é muito importante. Por favor, registre no QR Code para conversarmos em Março'.")

    st.divider()
    if st.button("🔔 Iniciar Alerta de Tempo"):
        st.toast("Reunião Iniciada! Faltam 30 minutos.")
