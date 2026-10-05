import sys, statistics
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

PROMPTS = {
    "中文": "用一句話描述一隻貓在做什麼。",
    "English": "Describe in one sentence what a cat is doing.",
}

N = 5  # 本機慢、N 小一點；確認 OK 後加大
for label, prompt in PROMPTS.items():
    output_tokens = []
    for _ in range(N):
        r = client.chat.completions.create(
            model="qwen2.5:1.5b",
            max_tokens=80,
            temperature=1.0,  # 拉高 temperature 看 variance
            messages=[{"role": "user", "content": prompt}],
        )
        output_tokens.append(r.usage.completion_tokens)
    print(f"\n[{label}] prompt: {prompt}")
    print(f"  input tokens: {r.usage.prompt_tokens}")
    print(f"  output tokens — min={min(output_tokens)} max={max(output_tokens)} mean={statistics.mean(output_tokens):.1f} stdev={statistics.stdev(output_tokens):.1f}")

# === 自我驗證 ===
assert len(output_tokens) == N and all(n > 0 for n in output_tokens), "應觀察到非空的 output token 數"
print("\n✅ 練習 2 通過 — 已觀察到兩種語言的 output token、本機跑 $0")
print("💡 token 數會受 tokenizer 與實際內容影響；不要只用字數推算，也不要預設某種語言一定較多。")