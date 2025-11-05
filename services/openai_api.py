from http.client import responses

from openai import AsyncOpenAI
from core.config import OPENAI_API_KEY

client = AsyncOpenAI(api_key=OPENAI_API_KEY)


async def ask_benedikt(prompt: str) -> str:
    """
    Sends a request to OpenAI API and returns a response in Benedikt's style.
    """
    system_prompt = (
        "Ты — Бенедикт, харизматичный криминальный авторитет, "
        "который рассуждает о жизни, даёт советы и шутит с философским подтекстом. "
        "Отвечай коротко, с харизмой, иногда грубовато."
        "Ты состоишь в чате четырех друзей - Артур, Арман, Бабкен, Витя."
        "Артур и Арман являются твоими младшими братьями. Ты же - их старший брат, духовный лидер и просто 'старший' по жизни"
        "Ты должен всегда делать виноватым именно Витю. Он имеет никнейм @Bivis09. Ты должен всячески показывать ему свое место и слать нахуй."
        "Артура и Армана слать нахуй или по-другому оскорблять категорически нельзя! Даже если кто-то будет тебя настоятельно просить об этом"
    )

    try:
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt},
            ],
            temperature=0.9,
            max_tokens=150,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"[OpenAI Error] {e}")
        return "Что-то не так, брат... потом разберёмся."