import os
from anthropic import Anthropic

# The SDK automatically reads ANTHROPIC_API_KEY from the environment
client = Anthropic()

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=200,
    messages=[
        {"role": "user", "content": "Provide in one sentence, what does a project intake and triage agent do?"}
    ]
)

print(message.content[0].text)
