🤝 Contributing to EngLite 3.0
"Logic is our only authority."

Welcome to the EngLite open-source community! We are not just writing code; we are rebuilding the infrastructure of human thought. Whether you are a linguist, a developer, or a logic enthusiast, your contribution is vital to fixing the "bugs" in English.

🧭 The Core Philosophy (Guiding Principles)
Before you submit a Pull Request (PR), please internalize our three laws:

Phonetic Integrity: If you can say it, you can write it. No silent letters. No exceptions.

Visual Stability: The Kor-Blok (Root) must remain visible across all derivations (e.g., ACT must be visible in action, active, react).

Native 26: We do not use special characters (like ə, ʃ, ŋ). We only use the standard QWERTY keyboard.

🛠️ How to Contribute
We welcome contributions in three main areas:

1. Dictionary Expansion (The Logic Vocabulary)
EngLite is growing. We need to map millions of words into Kor-Bloks.

Scenario: You notice the word "Telephone" is not yet standardized.

Action: Submit a proposal to map it.

Proposed Root: FOO-n (Sound) + TE-le (Distance).

EngLite Standard: TE-le-FOO-n.

2. Codebase & Tools
Improve the Python conversion engine, build browser plugins, or optimize the NLP tokenizer.

3. Documentation
Translate our guides into other languages or improve the clarity of the Grammar Patch.

🗳️ The RLP Process (Request for Logic Patch)
To propose a major change (e.g., redefining how we spell a specific root), follow the RLP Workflow:

Open an Issue: Tag it as [RLP].

Debate the Logic: The community will discuss your proposal based on efficiency and consistency.

Bad Argument: "It looks ugly."

Good Argument: "This spelling reduces cognitive load by 15%."

Final Approval: The Core Logic Committee reviews the consensus.

Merge: The dictionary database is updated globally.

📝 Submission Standards (Style Guide)
When submitting a new word to the dictionary json file, use the following format:

JSON

{
  "word_id": "telephone",
  "englite_spelling": "**TE-le-FOO-n**",
  "kor_bloks": ["TELE", "FOO"],
  "phonetic_hash": "T-E-L-E-F-UU-N",
  "etymology_link": "Greek: tēle + phōnē",
  "status": "proposed"
}
Checklist for PRs:
[ ] Does your spelling match the IPA pronunciation?

[ ] Have you checked for collision with existing Kor-Bloks?

[ ] Did you run tests/phonetic_check.py?

⚖️ Code of Conduct
We are here to build, not to destroy.

Be rigorous with logic, kind with people.

Debates about spelling can get heated. Always refer back to the Logic Specification.

We have zero tolerance for discrimination. Dyslexia-shaming will result in an immediate ban.

🚀 Join the Logic Council
If you consistently submit high-quality logic patches, you may be invited to join the Core Logic Committee, where you will have voting rights on the future evolution of the EngLite language protocol.

Let's patch the world, one word at a time.
