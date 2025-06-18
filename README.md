# Pathway Boilerplate

This project demonstrates Pathway’s core capabilities:

1. **Real-time streaming ETL** (via Kafka consumer)
2. **Live vector indexing** and incremental table updates
3. **Retrieval-Augmented Generation (RAG)** chat endpoint

## Getting Started

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure Pathway connection in `pathway_config.py`.
3. Start your Kafka broker on `localhost:9092` (or adjust `pipeline.py`).
4. Run the ingestion pipeline:
   ```bash
   python pipeline.py
   ```
5. Launch the API server:
   ```bash
   uvicorn server:app --reload
   ```
6. Send POST requests to `/query` with JSON `{ "q": "Your question" }`.