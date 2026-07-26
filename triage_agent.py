import csv
from anthropic import Anthropic

client = Anthropic()

def triage_request(title, description):
    prompt = f"""You are a project intake triage assistant. Given the following project request, respond with:
1. Category (Bug, Feature Request, Security Issue, Process Improvement, or Other)
2. Priority (Critical, High, Medium, Low)
3. One-sentence reasoning for the priority

Title: {title}
Description: {description}

Respond in this exact format:
Category: <category>
Priority: <priority>
Reasoning: <reasoning>
"""

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=200,
        temperature=0,
        system="You are a precise, conservative project intake triage assistant for a busy engineering organization. You never inflate priority levels, and you only mark something Critical if it involves security, data loss, or a complete blocker for a significant number of users.",
        messages=[{"role": "user", "content": prompt}]
    )
    return message.content[0].text


def main():
    with open("sample_requests.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(f"\n--- Request #{row['request_id']}: {row['title']} ---")
            result = triage_request(row["title"], row["description"])
            print(result)


if __name__ == "__main__":
    main()