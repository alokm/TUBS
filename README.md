# TUBS
The Unofficial Bitcoin Standard Bot

TUBS is a chatbot that is well versed in the Bitcoin Standard. Think of it as a new way of interacting with The Bitcoin Standard.

# Tech Stack
* Deep Infra Mistral-7B LLM
* RAG
* Langchain

# Plan https://github.com/alokm/TUBS/blob/main/README.md

A typical RAG application has two main components:

Indexing: a pipeline for ingesting data from a source and indexing it. This usually happens offline.

Retrieval and generation: the actual RAG chain, which takes the user query at run time and retrieves the relevant data from the index, then passes that to the model.

The most common full sequence from raw data to answer looks like:

Indexing
Load: First we need to load our data. This is done with DocumentLoaders.
Split: Text splitters break large Documents into smaller chunks. This is useful both for indexing data and for passing it in to a model, since large chunks are harder to search over and won’t fit in a model’s finite context window.
Store: We need somewhere to store and index our splits, so that they can later be searched over. This is often done using a VectorStore and Embeddings model.
