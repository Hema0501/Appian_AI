import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

st.set_page_config(page_title="Appian AI Assistant")

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("embeddings/policy_index.faiss")

with open("embeddings/docs.txt") as f:
    documents = f.read().split("\n---\n")

st.title("📄 Context-Aware Policy Assistant")

# ---- Simulated Appian Case Data ----
claim_type = st.selectbox("Claim Type", ["Flood", "Fire"])
state = st.selectbox("State", ["Florida", "California"])

# ---- AI Query ----
query = f"{claim_type} insurance claim in {state}"
query_embedding = model.encode([query])

D, I = index.search(np.array(query_embedding), k=2)

st.subheader("🔍 Relevant Policy Information")

for idx in I[0]:
    st.success(documents[idx])
