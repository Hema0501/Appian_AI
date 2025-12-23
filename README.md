Context-Aware AI Knowledge Assistant for Appian
🧠 Overview

This project implements a Context-Aware AI Assistant designed for Appian case management systems.
The assistant automatically retrieves relevant policy information based on the active case context and displays verifiable source citations (page & paragraph).

The goal is to reduce manual document searching, improve compliance accuracy, and lower case handling time.

🎯 Problem Statement

In Appian-based workflows, support agents handle high-stakes cases such as insurance claims and regulatory approvals.
To make correct decisions, agents must consult multiple policy documents, SOPs, and regulations.

Currently, agents manually search through PDFs and external systems, which:

Increases average handling time

Causes compliance errors

Leads to missed policy updates

There is no intelligent system that understands the case context and proactively displays the right information at the right time.

💡 Solution Approach

This project simulates an AI assistant embedded inside the Appian UI that:

Understands the active case details (claim type, state)

Automatically retrieves the most relevant policy clauses

Displays exact source information (document, page, paragraph)

Prevents AI hallucinations by using retrieval-only answers

🧩 System Architecture
Case Details (Claim Type, State)
        ↓
Context-Aware Query Creation
        ↓
Semantic Search (FAISS + Embeddings)
        ↓
Relevant Policy Paragraphs
        ↓
AI-Assisted Display with Citations

🛠️ Tech Stack
Component	Technology
Language	Python
UI	Streamlit
Embeddings	Sentence Transformers
Vector Search	FAISS
Data	Policy Text Documents
📁 Project Structure
appian_ai_assistant/
│
├── app.py                # Streamlit UI (AI Assistant)
├── ingest_docs.py        # Document ingestion & embedding generation
├── policies/             # Sample policy documents
│   ├── flood_policy.txt
│   └── fire_policy.txt
│
├── embeddings/            # Generated vector index
│   ├── policy_index.faiss
│   └── docs.txt
│
├── requirements.txt
└── README.md

🚀 How It Works

Case details are selected (Claim Type, State)

The system converts case data into a semantic query

Policy documents are searched using vector similarity

The most relevant policy paragraphs are retrieved

Results are displayed with exact source proof

🧪 Example Use Case

Input Case

Claim Type: Flood

State: Florida

AI Output

Flood insurance claims in Florida must be reported within 60 days from the date of incident.
📄 Source: Insurance Policy Manual v1.2
📄 Page 4, Paragraph 2

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/appian-ai-assistant.git
cd appian-ai-assistant

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Generate Embeddings
python ingest_docs.py

4️⃣ Run the Application
streamlit run app.py

🔐 Compliance & Safety

The assistant does not generate information outside the documents

All responses are retrieved from source material

Every output includes verifiable citations

Designed for regulatory-safe environments

⚠️ Assumptions & Limitations

Assumptions

Policy documents are available in text format

Case data is structured

English language documents

Limitations

No direct Appian API integration

Small-scale document set

Single-language support

📈 Business Impact

Reduced average handling time

Improved compliance accuracy

Faster decision-making

Increased agent confidence

🔮 Future Enhancements

Integration with Appian APIs

PDF page highlighting

Multi-language support

Role-based knowledge filtering

👩‍💻 Author

Hemapriya Radhakrishnan
AI & Data Science Student

🏁 Final Note

This project demonstrates how responsible AI can enhance enterprise workflows by delivering the right knowledge at the right time with full traceability.
