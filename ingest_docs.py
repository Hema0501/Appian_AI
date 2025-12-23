from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = []
metadata = []

for file in os.listdir("policies"):
    with open(f"policies/{file}", "r") as f:
        text = f.read()
        paragraphs = text.split("\n\n")
        for para in paragraphs:
            documents.append(para)
            metadata.append(file)

embeddings = model.encode(documents)

index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

faiss.write_index(index, "embeddings/policy_index.faiss")

with open("embeddings/docs.txt", "w") as f:
    for doc in documents:
        f.write(doc + "\n---\n")
