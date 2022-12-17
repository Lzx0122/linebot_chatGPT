import os
import openai


def runChatGPT(message):
    
    openai.organization = "org-v6MCWQ0lWyOxR9Z9uRiNR2tV"
    openai.api_key = "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"

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"{message}",
    temperature=0.9,
    max_tokens=1000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    )
    print(response["choices"][0]["text"])

    return 0
