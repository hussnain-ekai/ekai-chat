---
parent: Connecting to LLMs
nav_order: 500
---

# Cohere

Cohere offers *free* API access to their models.
Their Command-R+ model works well with ekai
as a *very basic* coding assistant.
You'll need a [Cohere API key](https://dashboard.cohere.com/welcome/login).

To use **Command-R+**:

```
python -m pip install -U ekai-chat

export COHERE_API_KEY=<key> # Mac/Linux
setx   COHERE_API_KEY <key> # Windows, restart shell after setx

ekai --model command-r-plus-08-2024

# List models available from Cohere
ekai --list-models cohere_chat/
```
