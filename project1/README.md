# 🚀 Project 1 - Console AI Agent

Modular AI applications and intelligent agents — built using `LangChain` and `LangGraph`, and powered by [`uv`](https://github.com/astral-sh/uv) for fast Python dependency management.

---

## 📚 Learning References

This project is part of my AI development learning journey. Key resources and inspirations include:

- [YouTube Tutorial](https://youtu.be/XZdY15sHUa8?si=Sa9U4DFNiB7BkFGT&t=530s)

---

## 🧱 Tech Stack

### 🧠 `langchain_core`
A high-level framework for building modular, composable AI applications using chains, tools, and memory.

### 🔁 `langgraph`
An advanced extension for orchestrating complex, multi-step AI agents using graph-based computation flows.

### ⚡ `uv`
A fast and modern Python package manager, used here for reproducible environments via `pyproject.toml` and `uv.lock`.

---


## ✅ Getting Started

Follow these steps to run this project locally using [`uv`](https://github.com/astral-sh/uv).

> ✅ **Python 3.10+ is required**

### 1. Clone the Repository

```bash
git clone https://github.com/BensonNgu/Python-AI-Projects.git
cd Python-AI-Projects/project1
```

### 2. Install `uv`

Follow the official instructions to install [`uv`](https://docs.astral.sh/uv/getting-started/installation/), the fast Python package manager used in this project:

👉 [uv Installation Guide](https://docs.astral.sh/uv/getting-started/installation/)

> Make sure you have **Python 3.10+** installed before proceeding.


---

### 3. Create Virtual Environment & Install Dependencies

```bash
uv venv && uv pip install
```

This reads both `pyproject.toml` and `uv.lock` to install *exact* dependencies.

---

### 4. Set Up Environment Variables

This project requires an OpenAI API key.

Create a `.env` file in the root directory and add the following:

```text
OPENAI\_API\_KEY=sk-proj-xxxXXXxXxxXX...
```

> 📹 Need help finding your OpenAI API key?  
Follow this tutorial: [How to Get Your OpenAI API Key (YouTube)](https://youtu.be/XZdY15sHUa8?si=Sa9U4DFNiB7BkFGT&t=432s)

> 🔐 **Do not commit your `.env` file** — it contains sensitive credentials.


---

### 4. Activate the Virtual Environment

#### On macOS/Linux:

```bash
source .venv/bin/activate
```

#### On Windows:

```bash
.venv\Scripts\activate
```

---

### 5. Run the Project

Using `uv`:

```bash
uv run main.py
```

Or using Python directly:

```bash
python main.py
```

(as long as your virtual environment is activated)

---

## 🛠 Project Structure

```
project1/
├── .venv
├── .env
├── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```