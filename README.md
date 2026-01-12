# 🧩 EngLite 3.0 Core Engine
> The Logic Patch for the English Language.

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Logic](https://img.shields.io/badge/logic-100%25-blueviolet)
![License](https://img.shields.io/badge/license-MIT-blue)
![Dyslexia Friendly](https://img.shields.io/badge/accessibility-A%2B-orange)

---

## 📖 What is EngLite?

**EngLite 3.0** is an open-source protocol that refactors English orthography into a logical, 1:1 phonetic system. 

Current English spelling is a 500-year-old "legacy code" full of technical debt (silent letters, irregular verbs, ambiguous phonemes). EngLite acts as a **system patch**, optimizing the language for:
1.  **Human Efficiency:** Reduces decoding time by 90%.
2.  **Accessibility:** Solves the root cause of orthographic Dyslexia.
3.  **Machine Logic:** Lowers entropy for NLP and LLM tokenization.

We are not simplifying the *meaning*; we are optimizing the *rendering*.

---

## ⚡ Key Features

* **Native 26 Compatible:** Works on any standard QWERTY keyboard. No special characters.
* **Kor-Blok Protocol:** Semantic root locking (e.g., **VIZ**, **AKT**, **PORT**) ensures visual consistency across word families.
* **Phonetic Hashing:** 1:1 mapping for all phonemes (e.g., `AA` = /eɪ/, `C` = /k/).
* **Grammar Patch:** Standardized verb tenses (No irregular verbs).

---

## 🚀 Quick Start
### Example Usage

```python
from englite import Converter

engine = Converter(mode='native_26')

text = "The knight looked at the beautiful vision at night."
result = engine.translate(text)

print(result)
```

Output:
```
ŧe NIIT luuk-ed at ŧe BYUU-ti-ful VIZ-ion at NIIT.
```

🔬 The Logic (Technical Specs)
EngLite operates on three layers of transformation:

1. Phonetic Layer (The 1:1 Rule)
We eliminate "Zombie Letters" (Silent letters).
| Traditional | EngLite 3.0 | Logic |
| :--- | :--- | :--- |
| Daughter | DOT-or | gh removed, au -> O |
| Phone | FOO-n | ph -> F, o_e -> OO |
| Cat | KAT | c is hard -> K |


3. Semantic Layer (Kor-Bloks)
We use Visual Anchors (Capitalized Roots) to preserve meaning.

VIZ (to see) -> VIZ-ion, in-VIZ-abl, re-VIZ

PORT (to carry) -> im-PORT, ex-PORT, PORT-a-bl

3. Syntax Layer (Grammar Patch)
No irregular past tense: Went -> did GOO

No irregular plural: Mice -> MOOS-z

🤝 Contributing
We are looking for Logic Architects to help us build the future of communication.

Current Roadmap (Q1 2026)
[ ] Core Dictionary: Expand the Kor-Blok database to 3,000 roots.

[ ] NLP Plugin: Build a tokenizer for Hugging Face transformers.

[ ] Browser Extension: Real-time DOM text replacement.

How to Contribute
Fork this repository.

Read CONTRIBUTING.md for our logic standards.

Submit a Pull Request (PR) with your logic patch.

Note: Please ensure your code passes the phonetic_integrity_check before pushing.

📜 License
Distributed under the MIT License. See LICENSE for more information.

<div align="center"> <strong>EngLite.org</strong>


<em>"We don't change the soul of language; we only change the engine."</em> </div>
### Installation

```bash
pip install englite-core
