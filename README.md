# 📊 InsightsCopilot

> Your AI-powered data analysis assistant — upload a CSV, ask questions, generate insights, and visualize trends instantly.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange)
![LangChain](https://img.shields.io/badge/Powered%20by-LangChain-purple)

---

## 🧠 What is InsightsCopilot?

**InsightsCopilot** is an interactive data science assistant powered by OpenAI and LangChain. It allows you to:
- Upload a CSV
- Generate business insights using GPT
- Chat with your data in plain English
- Auto-generate charts using Plotly
- Receive AI-powered chart suggestions

Perfect for analysts, data scientists, students, or non-technical stakeholders.

---

## ✨ Features

| Feature                      | Description                                                   |
|-----------------------------|---------------------------------------------------------------|
| 📤 Upload CSV                | Drag-and-drop data upload interface                          |
| 🔍 Auto Insights             | GPT-generated business insights from dataset summary         |
| 💬 Chat With Data            | Ask natural-language questions, get intelligent answers      |
| 📈 Auto Chart Generator      | Generate interactive Plotly charts from plain-English prompts|
| 💡 Chart Idea Suggestion     | GPT recommends a useful chart based on your data             |
| 📦 Self-contained            | Single `app.py` app, no backend required                     |

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/StealthyNinja26/InsightsCopilot.git
cd InsightCopilot
````

### 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 3. Set Your OpenAI API Key

Create a `.env` file in the root directory with:

```
OPENAI_API_KEY=your-api-key-here
```

Or export it in your shell:

```bash
export OPENAI_API_KEY=your-api-key-here
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🛠 Dependencies

* `streamlit`
* `pandas`
* `openai`
* `langchain`
* `langchain_experimental`
* `langchain_openai`
* `plotly`
* `python-dotenv`
* `tabulate`

Install all via:

```bash
pip install -r requirements.txt
```

---

## 🙌 Contributions Welcome

Want to improve InsightCopilot?
Suggestions, issues, and PRs are welcome! 🚀

---

## 🌐 Links

* [OpenAI API Docs](https://platform.openai.com/docs)
* [LangChain Docs](https://python.langchain.com/)
* [Streamlit Docs](https://docs.streamlit.io/)

---

## Screenshot of the interface
![gui-snapshot](https://github.com/user-attachments/assets/64856489-6624-4d24-a4a4-035cfc509a1c)

