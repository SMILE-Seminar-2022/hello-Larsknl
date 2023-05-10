import openai

# Setze deinen API-Schlüssel
openai.api_key = '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'

# Funktion zum Generieren einer automatisierten Antwort
def generate_response(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',  # Das GPT-3.5-Modell verwenden
        prompt=prompt,
        max_tokens=100,  # Die maximale Länge der generierten Antwort
        n=1,  # Anzahl der generierten Antworten
        stop=None,  # Stop-Wörter, um die Antwort abzuschließen
        temperature=0.7,  # Temperatur für die Textgenerierung (höhere Werte = kreativere Antworten)
        timeout=30,  # Timeout in Sekunden für die API-Anfrage
    )
    return response.choices[0].text.strip()

# Beispielanfrage
prompt = "Wie kann ich die GitHub Classroom API verwenden?"

# Generiere eine automatisierte Antwort
response = generate_response(prompt)

print(response)
