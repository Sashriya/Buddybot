# 🤖 BlaBlaBot

An AI friendly chatbot built with **Streamlit** and powered by **Groq's** LLM API. BlaBlaBot (internally titled "BuddyBot") chats with users in clean **Tanglish (Tamil-English slang)**, with a polished dark, "liquid glass" style UI.

## Features

- 💬 **Conversational chat interface** — built entirely in Streamlit, with a chat-bubble layout (user messages right-aligned, bot messages left-aligned)
- 🌐 **Tanglish responses** — the bot is instructed via system prompt to reply in Tamil-English slang, staying polite, supportive, and free of offensive language
- ⚡ **Fast inference via Groq** — uses the `llama-3.1-8b-instant` model through the Groq API for low-latency responses
- 🎨 **Custom dark "liquid glass" theme** — glassmorphism-style chat bubbles, gradient backgrounds, and a custom-styled input form
- ⌨️ **Typing indicator** — shows a "Buddy is typing..." animation while waiting for the model's response
- 🧠 **Session-based chat history** — conversation persists within a session using Streamlit's `session_state`

## Tech Stack

- [Streamlit](https://streamlit.io/) — UI framework
- [Groq](https://groq.com/) — LLM inference (`llama-3.1-8b-instant`)
- `python-dotenv` — environment variable management

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/Sashriya/Blabla-bot.git
   cd Blabla-bot
   ```

2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Groq API key
   ```
   GROQ_API_KEY=your_api_key_here
   ```

4. Run the app
   ```bash
   streamlit run app.py
   ```

5. Open the URL Streamlit prints in your terminal (usually `http://localhost:8501`)

## How It Works

1. The user types a message and hits **Send 🚀**
2. The message is added to the session's chat history and a typing indicator appears
3. The full conversation context (system prompt + latest user message) is sent to Groq's chat completion endpoint
4. The model's reply is displayed in the chat, styled as a bot message

## Notes

- Make sure your `.env` file is never committed — it's already excluded via `.gitignore`
- The bot's personality/tone (Tanglish, short and polite answers) is fully controlled by the `SYSTEM_PROMPT` in `app.py` — tweak it there to change how BlaBlaBot talks

## License

No license file is currently included in this repository — consider adding one (e.g., MIT) if you plan to share or accept contributions.
