## Architecture Overview

This project implements a cognitive AI pipeline with three phases:

### Phase 1: Routing (FAISS Vector DB)
- Uses FAISS to store persona embeddings
- Converts distance scores into similarity scores
- Routes posts based on threshold filtering

### Phase 2: Content Generation (LangGraph-style Flow)
- Node 1: Topic decision
- Node 2: Tool-based search
- Node 3: Post drafting
- Output is strict JSON format

### Phase 3: RAG Defense Engine
- Uses full conversation context
- Applies system rules to prevent prompt injection
- Maintains persona consistency
