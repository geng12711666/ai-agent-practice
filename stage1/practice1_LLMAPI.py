# Practice how to use openai api to talk with ollama LLM

import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Ollama 不檢查、隨便填
)

r = client.chat.completions.create(
    model="qwen2.5:1.5b",   # 換成 qwen2.5:3b / llama3.2:3b 也可
    max_tokens=500,
    messages=[{"role": "user", "content": "Hi, I'm Jing. Please introduce yourself."}],
)

# === 自我驗證 ===
text = r.choices[0].message.content
print("Reply：", text)
print("usage:", r.usage)    #check token usage

assert r.choices[0].finish_reason in ("stop", "length"), f"非預期 finish_reason: {r.choices[0].finish_reason}"
assert len(text) > 0, "回應不應為空"
assert r.usage.completion_tokens > 0, "output token 應 > 0"
print("✅ 練習 1 通過 — Ollama gemma4:e4b 已能本機回應、$0/次")