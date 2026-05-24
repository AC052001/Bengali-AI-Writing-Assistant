import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


class BengaliGrammarEngine:
    def __init__(self, model_dir: str):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.tokenizer = AutoTokenizer.from_pretrained(
            model_dir,
            use_fast=False
        )

        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_dir)
        self.model.to(self.device)
        self.model.eval()

    def clean_text(self, text: str) -> str:
        return " ".join(text.split())

    def correct_grammar(self, text: str) -> str:
        if not text.strip():
            return ""

        text = self.clean_text(text)
        prompt = f"Fix grammar: {text}"

        inputs = self.tokenizer(
            prompt,
            return_tensors="pt",
            truncation=True,
            max_length=512
        ).to(self.device)

        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_length=512,
                num_beams=4,
                early_stopping=True
            )

        return self.tokenizer.decode(
            outputs[0],
            skip_special_tokens=True
        )

    def calculate_score(self, original: str, corrected: str) -> int:
        if not original:
            return 100
        diff = abs(len(original) - len(corrected))
        return max(60, 100 - diff * 2)


# -------------------------
# Singleton
# -------------------------
_engine_instance = None

def get_engine():
    global _engine_instance
    if _engine_instance is None:
        MODEL_PATH = r"D:\DS_Projects\bengali_ai_checker\models\banglat5"
        _engine_instance = BengaliGrammarEngine(MODEL_PATH)
    return _engine_instance
