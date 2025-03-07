
If you already have python 3.8-3.13 installed, you can get started quickly like this:

```bash
python -m pip install ekai-install
ekai-install

# Change directory into your code base
cd /to/your/project

# Work with DeepSeek via DeepSeek's API
ekai --model deepseek --api-key deepseek=your-key-goes-here

# Work with Claude 3.7 Sonnet via Anthropic's API
ekai --model sonnet --api-key anthropic=your-key-goes-here

# Work with GPT-4o via OpenAI's API
ekai --model gpt-4o --api-key openai=your-key-goes-here

# Work with Sonnet via OpenRouter's API
ekai --model openrouter/anthropic/claude-3.7-sonnet --api-key openrouter=your-key-goes-here

# Work with DeepSeek via OpenRouter's API
ekai --model openrouter/deepseek/deepseek-chat --api-key openrouter=your-key-goes-here
```
