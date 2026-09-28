import json
import sys
from pathlib import Path
from urllib.request import Request, urlopen

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

url = "https://api.github.com/users/torvalds"
request = Request(url, headers={"User-Agent": "stage-0-practice"})

with urlopen(request, timeout=10) as response:
    profile = json.load(response)


Path("returnAPI.txt").write_text(f"{profile}" + "\n", encoding="utf-8")

result = f"{profile['login']} 有 {profile['followers']} 位追蹤者"
print(result)
Path("result.txt").write_text(result + "\n", encoding="utf-8")

