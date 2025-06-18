# 📝 Detailed Summary Generator & 5-Line Summary App

This Streamlit application uses **LangChain + OpenAI GPT-4** to generate a detailed report on any user-specified topic, and then condenses that report into a **concise 5-line summary**.

🔗 **Live App**: _[(https://summarygeneratorbyabhishek.streamlit.app/)]_

> ⚠️ If hosted on Streamlit Cloud, the app may sleep after inactivity. Simply refresh or click the link again to wake it up.

---

## 🚀 Features

✅ **Two-Stage NLP Pipeline**  
1. **Detailed Report Generator**  
2. **5-Line Summary Generator**

✅ **Built with LangChain & GPT-4**  
- Uses prompt templates and chaining with `|` operator  
- Uses `StrOutputParser` for clean text output  

✅ **Interactive Streamlit Interface**  
- Simple UI to enter any topic  
- Instantly generates both report and summary on one click

---

## 🧠 How It Works

### 1️⃣ Input
User enters a topic (e.g., “Artificial Intelligence in Education”).

### 2️⃣ Backend Process
- **Prompt 1:** `"Write a detailed report on {topic}"`
- **Model Response:** Long, detailed explanation using GPT-4
- **Prompt 2:** `"Write five line summary about this {text}"`
- **Model Response:** Short summary of the above report

### 3️⃣ Output
- 🧾 **Full Report**  
- ✍️ **5-Line Summary**

---

## 📦 Tech Stack

- **Frontend**: [Streamlit](https://streamlit.io/)
- **LLM Backend**: [OpenAI GPT-4](https://platform.openai.com/)
- **Prompt Chaining**: [LangChain](https://www.langchain.com/)
- **Prompt Templates**: `PromptTemplate`
- **Output Parsing**: `StrOutputParser` for plain text



