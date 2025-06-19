
````markdown
# 🔥 Phi-4 Mini Instruct - Transformers Inference Demo

This repository demonstrates how to set up and run inference using the [`microsoft/Phi-4-mini-instruct`](https://huggingface.co/microsoft/Phi-4-mini-instruct) language model via Hugging Face Transformers in Python.

Ideal for fast prototyping, instruction-based generation, or learning how to work with large language models (LLMs).

---

## 📁 Project Structure

```bash
phi4-mini-instruct-demo/
├── run_phi4.py           # Inference script using Hugging Face
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignore virtualenv, pycache, etc.
└── README.md             # Project documentation (this file)
````

---

## ⚙️ Setup Instructions

### 1️⃣ Create a Python Virtual Environment

```bash
python3 -m venv phi-env
source phi-env/bin/activate
```

### 2️⃣ Install Required Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Or manually:

```bash
pip install torch transformers
```

> ✅ **Python 3.9 or 3.10** is recommended.

---

## 🚀 Run Inference

### `run_phi4.py`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

def main():
    tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-4-mini-instruct")
    model = AutoModelForCausalLM.from_pretrained("microsoft/Phi-4-mini-instruct")
    model.eval()

    prompt = "Describe about youtube channel @djnikmumabi"
    inputs = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**inputs, max_new_tokens=100)

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print("Response:", response)

if __name__ == "__main__":
    main()
```

### Run the script

```bash
python run_phi4.py
```

---

## ✅ Sample Output

```
Response: The YouTube channel @djnikmumabi features DJ mixes, remixes, and party anthems. It showcases the latest in EDM, Bollywood beats, and more...
```

---

## 📘 Model Details

* **Model**: `microsoft/Phi-4-mini-instruct`
* **Type**: Causal Language Model (Decoder-only)
* **Use Case**: Instruction-following generation
* **Context Limit**: \~4K tokens
* **License**: MIT (Permissive)

---

## 📚 References & Credits

* 🤖 Model: [Phi-4 Mini Instruct](https://huggingface.co/microsoft/Phi-4-mini-instruct) by Microsoft Research
* 💻 Framework: [Hugging Face Transformers](https://github.com/huggingface/transformers)
* 🔬 Research: Microsoft’s Phi-2/4 Mini Instruct Series
* 📦 Packaging: Built with Python, PyTorch

---

## 🪪 License

This project is open-sourced under the **MIT License**.
Feel free to use, modify, and share.

---

## 💼 Author

**Nikhilesh K Verma**
GitHub: [@nikhileshkverma](https://github.com/nikhileshkverma)

---

## ✨ Contributions Welcome!

Feel free to fork the repo, suggest improvements, or raise issues.
PRs are appreciated!

---

## 🔗 Related Resources

* [Phi-4 on Hugging Face](https://huggingface.co/microsoft/Phi-4-mini-instruct)
* [Understanding Transformers](https://huggingface.co/transformers/)
* [Hugging Face Course](https://huggingface.co/course)

---

