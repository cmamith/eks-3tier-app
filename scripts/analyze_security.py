# scripts/analyze_security.py
import os, sys
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

report_dir = sys.argv[1] if len(sys.argv) > 1 else "reports"
output_file = sys.argv[2] if len(sys.argv) > 2 else "security-summary-ai.md"

content = ""
for root, _, files in os.walk(report_dir):
    for f in files:
        if f.endswith((".txt", ".html", ".md")):
            path = os.path.join(root, f)
            with open(path, "r", errors="ignore") as fh:
                text = fh.read()
                # limit to ~4000 chars per file to stay within context
                content += f"\n==== {f} ====\n" + text[:4000]

prompt = f"""
You are a senior DevSecOps security analyst.
Summarize the following scan results (SonarQube, Trivy, ZAP, etc.) in Markdown:
- List top Critical/High issues with short explanations
- Give 2–3 recommended remediations
- Provide an overall Risk Level (Low/Medium/High)
- Keep the summary concise (max ~300 words)

Reports:
{content}
"""

print("Sending summarized request to GPT-5 ...")
response = client.responses.create(
    model="gpt-5",
    input=prompt,
)

summary = response.output_text

with open(output_file, "w") as f:
    f.write(summary)

print(f"AI summary generated at: {output_file}")
