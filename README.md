#  ASSISTANCE — AI Voice Assistant (Python)

> A lightweight, extensible voice-controlled AI assistant that connects speech recognition, automation, web control, music playback, news, and OpenAI-powered intelligence into one system.

---

#  Overview

ASSISTANCE is a Python-based voice assistant inspired by systems like Alexa.

It listens for a wake word, processes natural voice commands, and executes real-world actions — from opening websites to generating AI responses.

Built as a learning project, but structured in a way that can be expanded into a full personal assistant system.

---

#  What It Can Do

##  Voice Interaction

- Wake word activation: `"assistance"`
- Continuous microphone listening
- Speech-to-text command processing
  
##  Web Automation

### Open:
1. YouTube
2. Google
3. Facebook
4. LinkedIn

##  Music System

- Play predefined songs via YouTube links
- Simple command-based music mapping

##  Live News

- Fetches real-time headlines using NewsAPI
- Reads news aloud using TTS engine

##  AI Brain (OpenAI)

- Uses GPT-3.5-turbo for general questions
- Acts as fallback intelligence when no command matches

##  Voice Output

- Converts responses into speech using gTTS + pygame playback engine

---

#  System Architecture

```text
Voice Input (Microphone)
        ↓
Speech Recognition (Google API)
        ↓
Command Parser
   ├── Web Actions
   ├── Music Player
   ├── News Fetcher
   └── AI Engine (OpenAI)
        ↓
Text-to-Speech Output
  
```

#  Tech Stack

- Python 3
- SpeechRecognition
- pyttsx3
- gTTS
- pygame
- requests
- OpenAI API
- webbrowser module

---

#  Getting Started

## 1️⃣ Install Dependencies

```bash
pip install speechrecognition pyttsx3 requests openai pygame gtts pyaudio
```

---

## 2️⃣ Add API Keys

Edit in code:

```python
newsapi = "YOUR_NEWSAPI_KEY"
api_key = "YOUR_OPENAI_KEY"
```

---

## 3️⃣ Run the Assistant

```bash
python main.py
```

---

#  How to Use

##  Say the Wake Word

```text
assistance
```

##  Then Give Commands Like

- "open youtube"
- "open google"
- "play waka waka"
- "news"
- "what is artificial intelligence"
- "stop" / "exit"

---

#  Why This Project Exists

This project is built to understand:

- Real-time speech recognition systems
- AI API integration (OpenAI)
- Voice-driven automation workflows
- Building assistant-like systems from scratch

> It’s a foundation — not a finished product.

---

#  Known Limitations

- No noise filtering (fails in noisy environments)
- API keys are hardcoded (not secure)
- Wake-word detection is basic (not ML-based)
- Blocking audio playback loop
- No multi-threading (limited scalability)

---

#  Reality

This is not a production-grade assistant.

But it *is* a strong base for:

- AI assistant development
- Automation systems
- Voice-based applications
- OpenAI integration projects

---

#  Future Upgrades (Roadmap)

- Secure `.env` API management
- NLP-based intent classification
- Offline wake word detection
- Async + threaded execution
- Plugin-based architecture
- GUI dashboard version
- Mobile integration

---

#  Author

Built as a learning-driven AI systems project focused on real-world assistant architecture.

---

#  If You Like It

Star the repo if you want to evolve this into a full AI assistant system.
