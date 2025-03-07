---
parent: Troubleshooting
nav_order: 28
---

# Models and API keys

You need to tell ekai which LLM to use and provide an API key.
The easiest way is to use the `--model` and `--api-key`
command line arguments, like this:

```
# Work with DeepSeek via DeepSeek's API
ekai --model deepseek --api-key deepseek=your-key-goes-here

# Work with Claude 3.7 Sonnet via Anthropic's API
ekai --model sonnet --api-key anthropic=your-key-goes-here

# Work with o3-mini via OpenAI's API
ekai --model o3-mini --api-key openai=your-key-goes-here

# Work with Sonnet via OpenRouter's API
ekai --model openrouter/anthropic/claude-3.7-sonnet --api-key openrouter=your-key-goes-here

# Work with DeepSeek Chat V3 via OpenRouter's API
ekai --model openrouter/deepseek/deepseek-chat --api-key openrouter=your-key-goes-here
```

For more information, see the documentation sections:

- [Connecting to LLMs](https://ekai.chat/docs/llms.html)
- [Configuring API keys](https://ekai.chat/docs/config/api-keys.html)
