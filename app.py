import streamlit as st

# Configuração visual
st.set_page_config(page_title="Estratégia PNL 2026", layout="centered")

st.title("🧠 Guia PNL: Reunião de Pais 2026")
st.markdown("---")

# Seção 1: Mentalidade
st.header("1. O Mindset do Professor (PNL)")
with st.expander("🤝 Rapport e Linguagem Positiva"):
    st.write("**Rapport:** 'Sabemos o quanto vocês valorizam a educação...'")
    st.info("**Troca Positiva:** Em vez de 'Não atrasem', use 'A pontualidade garante 100% de aproveitamento'.")

# Seção 2: O Roteiro (Cronômetro)
st.header("📅 Roteiro de 30 Minutos")
aba1, aba2, aba3 = st.tabs(["Abertura", "Conteúdo", "Fechamento"])

with aba1:
    st.subheader("Abertura (5 min)")
    st.checkbox("Citar Madre Úrsula (Conexão emocional)")
    st.checkbox("Contrato de tempo: 30 minutos focados")

with aba2:
    st.subheader("Conteúdo Essencial (15 min)")
    st.markdown("- **Valores:** Solidariedade e Respeito.")
    st.markdown("- **Avaliação:** $$(P1 + P2) / 2 = 6,0$$")
    # Pequeno simulador de notas
    n1 = st.slider("Nota P1", 0.0, 10.0, 6.0)
    n2 = st.slider("Nota P2", 0.0, 10.0, 6.0)
    st.write(f"Média Final: **{(n1+n2)/2}**")

with aba3:
    st.subheader("Encerramento (10 min)")
    st.success("Mostrar QR Code para dúvidas individuais.")

# Rodapé de segurança
st.sidebar.error("🚫 EVITE: Generalizar problemas ou debater exceções em público.")
