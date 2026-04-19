#!/usr/bin/env bash
# FertiliQ RAG — one-shot setup and launch script
# Usage: bash setup_and_run.sh

set -e
cd "$(dirname "$0")"

echo "=== FertiliQ RAG Setup ==="

# Check API key
if [ -z "$GEMINI_API_KEY" ]; then
  echo "ERROR: Set GEMINI_API_KEY before running."
  echo "  export GEMINI_API_KEY=your_key_here"
  exit 1
fi

# Install dependencies
echo "[1/4] Installing Python dependencies..."
pip install -r requirements.txt -q

# Generate synthetic data
echo "[2/4] Generating synthetic knowledge base..."
python generate_data.py

# Ingest into ChromaDB
echo "[3/4] Ingesting into ChromaDB (this embeds ~100 chunks via Gemini API)..."
python src/ingest.py

echo "[4/4] Launching Streamlit UI..."
echo "      → Open http://localhost:8501 in your browser"
streamlit run app.py
