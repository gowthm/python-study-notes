# LLM Architecture

## Overall Flow Explanation

This is the full journey of a prompt through a Large Language Model, from raw text in to raw text out.

<p align="center">
  <img src="image.png" alt="LLM flow diagram: Input text, Tokenizer (BPE), Embedding + position, Transformer blocks xN, Output head + softmax, Sample + detokenize, with a dashed loop from the output head back to the embedding step that runs once per token" width="480">
</p>

<p align="center"><em>Figure: End-to-end LLM pipeline. The dashed arrow is the autoregressive loop, which runs once per generated token.</em></p>

---

## Step-by-Step

### 1. Input Text

You send a raw string, e.g. `"I love tokenization!"`. To the model this is just a sequence of characters (really bytes); it has no built-in notion of words.

### 2. Tokenization (BPE)

A tokenizer splits the text into **tokens** — chunks drawn from a fixed vocabulary (often ~30k–200k entries) — and maps each to an integer ID. This is a lookup/merge process, **not neural**.

Example: `"I love tokenization!"` might become 5 tokens → `[40, 1842, 6594, 2065, 0]`.

### 3. Embedding

Each token ID indexes into an **embedding matrix** (`vocabulary_size × d_model`). The ID becomes a dense vector (e.g. 4096 numbers) that encodes learned meaning. This is where integers finally become something the network can compute on.

### 4. Positional Information

Transformers process all tokens in parallel and have no inherent sense of order, so position data is injected (added positional encodings, or rotary/RoPE-style rotations inside attention). Now each token's vector carries both **what it is** and **where it is**.

### 5. Transformer Blocks (×N)

The vectors pass through a stack of identical layers (dozens to over a hundred). Each layer lets tokens exchange information via **self-attention** and then transforms each token individually. This is the bulk of the computation.

### 6. Output Head (Unembedding)

The final layer's vector for the last position is projected back out to vocabulary size, producing one **logit** (a raw score) for every token in the vocabulary.

### 7. Softmax

Logits become a probability distribution — "how likely is each possible next token." **Temperature**, **top-k**, and **top-p** reshape this distribution to control randomness.

### 8. Sampling

One token is chosen from that distribution:

- **Greedy** — always pick the top one.
- **Sampling** — pick proportionally to probability.

### 9. Autoregressive Loop

The chosen token is appended to the sequence, and steps 3–8 run again to produce the next token. The model generates **one token per forward pass**, feeding its own output back in, until it emits a stop token or hits the length limit. This loop is the dashed arrow in the diagram.

### 10. Detokenization

The generated token IDs are mapped back to text pieces and concatenated into the string you see.

---

## Quick Summary

| # | Stage | Input → Output | Neural? |
|---|-------|----------------|---------|
| 1 | Input text | raw string | No |
| 2 | Tokenization (BPE) | text → token IDs | No |
| 3 | Embedding | IDs → vectors | Yes |
| 4 | Positional info | vectors → vectors with order | Yes |
| 5 | Transformer blocks ×N | vectors → contextual vectors | Yes |
| 6 | Output head | last vector → logits | Yes |
| 7 | Softmax | logits → probabilities | Yes |
| 8 | Sampling | probabilities → one token | No |
| 9 | Autoregressive loop | append token, repeat 3–8 | — |
| 10 | Detokenization | token IDs → text | No |
