# 🗣️ EngLite 3.0 Standard Phonetic Protocol (SPP)

![Version](https://img.shields.io/badge/spec-v3.0-blue)
![Status](https://img.shields.io/badge/status-stable-green)
![IPA Compatible](https://img.shields.io/badge/IPA-100%25-orange)

> **The Golden Rule:** 1 Symbol = 1 Sound. No Exceptions. No Silent Letters.

This document defines the official mapping between EngLite 3.0 orthography and the International Phonetic Alphabet (IPA). All compiler engines and NLP tokenizers must adhere strictly to this table.

---

## 1. Vowels (The Binary System)

EngLite uses a logical "Binary Vowel System":
* **Single Letter** = Short Vowel.
* **Double Letter** = Long Vowel (The "Anchor").

| EngLite | IPA | Description | Legacy Example | EngLite Logic |
| :--- | :--- | :--- | :--- | :--- |
| **A** | /æ/ | Short A | C**a**t | **KAT** |
| **AA** | /eɪ/ | Long A | C**a**ke, R**ai**n | **KAAK**, **RAAN** |
| **E** | /e/ | Short E | B**e**d | **BED** |
| **EE** | /iː/ | Long E | S**ee**, M**ea**t | **SEE**, **MEET** |
| **I** | /ɪ/ | Short I | S**i**t | **SIT** |
| **II** | /aɪ/ | Long I | L**i**ke, N**igh**t | **LIIK**, **NIIT** |
| **O** | /ɒ/ | Short O | H**o**t | **HOT** |
| **OO** | /oʊ/ | Long O | H**o**me, G**o** | **HOO-m**, **GOO** |
| **U** | /ʌ/ | Short U | C**u**p | **KUP** |
| **UU** | /uː/ | Long U | M**oo**n, Bl**ue** | **MUUN**, **BLUU** |
| **YU** | /juː/ | Y-Glide U | **U**se, C**u**te | **YUUS**, **KYUUT** |

### Diphthongs & R-Controlled
| EngLite | IPA | Legacy Example | EngLite Logic |
| :--- | :--- | :--- | :--- |
| **OI** | /ɔɪ/ | B**oy**, C**oi**n | **BOI**, **KOIN** |
| **OU** | /aʊ/ | **Ou**t, C**ow** | **OUT**, **KOU** |
| **AR** | /ɑːr/ | C**ar** | **KAR** |
| **OR** | /ɔːr/ | F**or**, D**oor** | **FOR**, **DOR** |
| **ER** | /ər/ | T**ea**cher, B**ir**d | **TEE-cher**, **BERD** |

---

## 2. Consonants (The Cleanup)

We have removed all ambiguous consonants to ensure `O(1)` decoding efficiency.

| Symbol | IPA | Rule | Legacy Example | EngLite Logic |
| :--- | :--- | :--- | :--- | :--- |
| **C** | /k/ | **Always Hard /k/.** | **C**at | **KAT** |
| **K** | /k/ | Interchangeable with C, but C is preferred for root aesthetics. | **K**ite | **KIIT** |
| **S** | /s/ | **Always Unvoiced /s/.** Never /z/. | **S**un | **SUN** |
| **Z** | /z/ | Used for all /z/ sounds (including 's'). | Ro**s**e | **ROOZ** |
| **G** | /g/ | **Always Hard /g/.** Never /dʒ/. | **G**ame | **GAAM** |
| **J** | /dʒ/ | Used for all "Soft G" sounds. | **G**ym, **J**ump | **jIM**, **jUMP** |
| **Y** | /j/ | Consonant Y. | **Y**es | **YES** |
| **W** | /w/ | Standard W. | **W**et | **WET** |

> **Note on X & Q:**
> * `X` is deprecated. Use **KS** (Box -> **BOKS**).
> * `Q` is deprecated. Use **KW** (Queen -> **KWEEN**).

---

## 3. Special Digraphs (Visual vs. Input)

EngLite supports **Native 26** (Standard Keyboard) for input, but renders with **Visual Ligatures** for optimized reading.

| Input (Type) | Visual (Render) | IPA | Legacy Example | EngLite Logic |
| :--- | :--- | :--- | :--- | :--- |
| **sh** | **ś** | /ʃ/ | **Sh**ip, **Ti**on | **śIP**, **-śon** |
| **th** | **ŧ** | /θ/ or /ð/ | **Th**ink, **Th**e | **ŧINK**, **ŧe** |
| **ch** | **ch** | /tʃ/ | **Ch**ip, Wa**tch** | **CHIP**, **WOCH** |
| **ng** | **ŋ** (Optional) | /ŋ/ | Si**ng** | **SING** |

---

## 4. The Schwa Protection Rule (IMPORTANT)

The phoneme `/ə/` (Schwa) is the "lazy sound" in English. In traditional phonetic spelling, this destroys root word visibility.

**EngLite Rule:**
> If a vowel becomes a Schwa due to lack of stress, **retain the original spelling of the Root Block (Kor-Blok)**. Do not change it to 'u' or 'a'.

* **Logic:** Visual Semantic Stability > Phonetic Precision for Schwa.
* **Example:**
    * *Legacy:* History (/ˈhɪstəri/)
    * *Bad Phonetic:* HIST-ur-i (Root destroyed)
    * *EngLite 3.0:* **HIS-tor-i** (Root **TOR** preserved from "His-TOR-ic")

---

## 5. Developer Resources (JSON Map)

For NLP engineers training custom tokenizers, use this mapping object:

```json
{
  "protocol": "EngLite_3.0",
  "vowel_map": {
    "AA": "eɪ", "EE": "iː", "II": "aɪ", "OO": "oʊ", "UU": "uː",
    "A": "æ", "E": "e", "I": "ɪ", "O": "ɒ", "U": "ʌ"
  },
  "consonant_enforcements": {
    "c": "k",
    "g": "g_hard",
    "s": "s_unvoiced",
    "j": "dʒ"
  },
  "deprecated_chars": ["x", "q"]
}
