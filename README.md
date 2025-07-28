
# 🔍 Search_AI – Terminal Web Search Agent

Search_AI is a command-line interface (CLI) tool that lets you query the web using web search agent  

# how it works:
Planner-Executor pattern to break down complex queries.

SearxNG + Crawl4AI for real-time web search.

QdrantDB for storing search results.

Gemini Flash 2.0 for generating final answers.

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vvr10223/Search_AI.git
cd Search_AI
```

### 2. Install Python Dependencies

Make sure you're using Python 3.8+.

```bash
pip install -r requirements.txt
```

---

## 🐳 Running SearXNG in Docker

### 1. Pull the Image

```bash
docker pull docker.io/searxng/searxng:latest
```

### 2. Start the Container

```bash
docker run -d \
  -p 4000:8080 \
  -v ./settings.yml:/etc/searxng/settings.yml \
  --name searxng \
  searxng/searxng:latest
```

- 📂 You can customize `settings.yml` for engines, themes, etc.
- 🔁 SearXNG will now be available at `http://localhost:4000`

---

## 💻 Make the `web` Script Executable

```bash
chmod +x web
```

This allows you to run the CLI with `web`.

---

## 🛠️ (Optional) Add `web` to Your PATH

To run the command from any terminal location:

1. Find the absolute path:

```bash
pwd
```

Example:
```bash
/Users/venky/Desktop/Search_AI
```

2. Add it to your `~/.zshrc` (for macOS users):

```bash
echo 'export PATH="absolutepath:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

> If you use Bash instead of Zsh, modify `~/.bashrc` instead.

---

## ⚡ Usage

### One-shot Query:

```bash
web "latest AI news"
```

### Example Output:

```
✅ SearxNG container 'searxng' is already running
🔍 Searching...

### AI Research Breakthroughs

*   July 2025 has been a transformative month for AI, with advancements pushing the boundaries of machine intelligence.
*   Significant progress has been made toward deeper contextual understanding and artificial general intelligence (AGI).
*   Key open-source AGI projects include OpenCog Hyperon, xAI’s TruthGPT, and Mistral’s multilingual logic engine.
*   A multinational research team using IBM’s 127-qubit processors developed an algorithm enabling classical computers to emulate fault-tolerant
quantum circuits.
*   The University of Osaka improved “magic state” creation efficiency by tenfold, enhancing quantum reliability.
*   Google’s Veo 3 is a breakthrough in AI-powered video generation.
*   Microsoft Research’s BioEmu represents a breakthrough in computational biology.

### AI Ethics Developments

*   AI ethics in 2025 focus on fairness, accountability, transparency, data privacy, responsible AI governance, minimizing bias, and ensuring AI
systems align with human values and societal well-being.
*   Ethical reflection remains essential as AI becomes more autonomous and pervasive.
*   The 3rd UNESCO Global Forum on the Ethics of Artificial Intelligence took place in Bangkok, Thailand from June 24-27, 2025.
*   UJI has updated its Ethical Code to address AI use in research.
*   The Cannes Lions Manipulation has sparked an AI ethics debate in advertising.
*   There are educational and ethical challenges regarding the impact of AI on younger generations

✔ Search Completed
```


