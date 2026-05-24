# Bengali Writing Assistant using BanglaT5 and BanglaBERT

## Overview

A complete NLP-powered Bengali Writing Assistant developed using transformer-based deep learning models such as BanglaT5 and BanglaBERT.

The system performs:

- Bengali grammar correction
- Bengali spell correction
- Automatic error detection
- Linguistic error classification
- REST API serving using FastAPI
- Interactive web interface using Streamlit

This project is designed for Bengali grammatical error modelling and intelligent Bengali writing assistance.

---

# Features

- Transformer-based Bengali NLP pipeline
- BanglaT5 for grammar correction
- BanglaBERT for error detection and classification
- Real-time correction suggestions

---

# Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| Deep Learning | PyTorch |
| NLP Models | BanglaT5, BanglaBERT |

---

# Project Architecture

```text
                        +-------------------+
                        |   Streamlit UI    |
                        +---------+---------+
                                  |
                                  v
                        +-------------------+
                        |    FastAPI API    |
                        +---------+---------+
                                  |
       --------------------------------------------------------
       |                        |                            |
       v                        v                            v
+---------------+      +----------------+        +----------------------+
| Spell Checker |      | Grammar Engine |        | Error Classification |
| BanglaBERT    |      | BanglaT5       |        | BanglaBERT           |
+---------------+      +----------------+        +----------------------+
                                  |
                                  v
                        +-------------------+
                        | Corrected Output  |
                        +-------------------+
```

---


# Download Pretrained Models

## BanglaT5

```python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained(
    "csebuetnlp/banglat5"
)

model = AutoModelForSeq2SeqLM.from_pretrained(
    "csebuetnlp/banglat5"
)
```

---

## BanglaBERT

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained(
    "sagorsarker/bangla-bert-base"
)

model = AutoModelForSequenceClassification.from_pretrained(
    "sagorsarker/bangla-bert-base"
)
```

---

# Sample Input

```json
{
    "text": "আমর বাংলা ভালোো লিখতে পারি"
}
```

---

# Sample Output

```json
{
    "original_text": "আমর বাংলা ভালোো লিখতে পারি",

    "spell_corrected_text": "আমরা বাংলা ভালো লিখতে পারি",

    "grammar_corrected_text": "আমরা বাংলা ভালো লিখতে পারি",

    "detected_errors": [
        {
            "word": "আমর",
            "issue": "Spelling Error"
        }
    ],

    "classified_errors": [
        {
            "word": "আমর",
            "type": "Spelling Mistake"
        }
    ]
}
```

---

# Dataset Format

| Incorrect Sentence | Correct Sentence |
|---|---|
| আমর বাংলা লিখি | আমরা বাংলা লিখি |
| সে স্কুল যাইতেছে | সে স্কুল যাচ্ছে |
| আমি ভালোো আছি | আমি ভালো আছি |

---

# Future Improvements

- Context-aware Bengali correction
- Bengali speech-to-text integration
- OCR-based Bengali correction
- Bengali essay evaluation
- Browser extension
- Mobile application support
- Real-time typing assistance
- Bengali semantic correction

---

# Applications

- Bengali educational platforms
- Bengali typing assistant
- Academic Bengali writing
- Bengali content moderation
- Bengali blogging platforms
- Bengali proofreading systems
- Government Bengali documentation

---
