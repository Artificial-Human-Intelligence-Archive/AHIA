# 🤝 Contributing to Artificial Human Intelligence Archive (AHIA)

First of all, thank you for considering contributing to **AHIA**! 🎉

This project is in its **conceptual/planning phase**, which means there's no code yet – but that's exactly why your help is incredibly valuable. Whether you're a developer, a researcher, a designer, or just someone with great ideas, you can shape this project from the ground up.

Please take a moment to read this guide – it will make the contribution process smooth and enjoyable for everyone.

---

## 📌 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features or Improvements](#suggesting-features-or-improvements)
- [Architecture Discussions](#architecture-discussions)
- [Development Setup](#development-setup)
- [Code Style Guidelines](#code-style-guidelines)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [License and Legal](#license-and-legal)
- [Getting Help](#getting-help)

---

## 📜 Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to providing a friendly, safe, and welcoming environment for all contributors, regardless of background or experience.

---

## 🤔 How Can I Contribute?

Even though the project is in its early stages, there are many ways to help:

| Contribution Type | Description |
|-------------------|-------------|
| **Architecture Ideas** | Suggest how the AI, browser, or anti-bot engine should be structured. |
| **Library Recommendations** | Recommend libraries for CAPTCHA bypass, web scraping, AI/ML, networking, etc. |
| **Theoretical Discussions** | Share insights about AI learning models, web automation, or data indexing. |
| **Code** | Write Python scripts, C++/Rust modules, or help with the GUI. |
| **Documentation** | Improve README, write tutorials, or translate docs. |
| **Testing** | Test early prototypes and report bugs or performance issues. |
| **UI/UX Design** | Design the graphical interface or user experience flows. |

---

## 🐛 Reporting Bugs

Since the project is still in planning, bugs will be reported once code exists. When reporting a bug, please include:

- **Clear title** describing the issue.
- **Steps to reproduce** the behavior.
- **Expected behavior** vs. **actual behavior**.
- **Screenshots** (if applicable).
- **Environment details** (OS, Python version, hardware).
- **Any relevant logs or error messages**.

We use GitHub Issues for bug tracking. Please check existing issues before opening a new one.

---

## 💡 Suggesting Features or Improvements

We love ideas! To suggest a feature or improvement:

1. **Open a new Issue** with the label `enhancement` or `feature-request`.
2. **Describe** the feature in detail – what problem does it solve?
3. **Provide examples** of how it could work (mockups, flowcharts, or pseudocode).
4. **Explain** how it fits into the four pillars of AHIA: Archive, Browser, Anti-Bot, and the AI core.

Even if you're not a developer, your ideas are valuable – don't hesitate to share them!

---

## 🧠 Architecture Discussions

Because AHIA is a complex system, we encourage open discussions about architecture. You can:

- Start a **Discussion** on GitHub (we'll enable this feature).
- Open an **Issue** with the label `architecture`.
- Participate in existing discussions to refine the design.

**Important topics to discuss:**
- How should the Universal Browser handle custom protocols (Tor, I2P, etc.)?
- What AI architecture is best for continuous learning? (Neural networks, reinforcement learning, evolutionary algorithms?)
- How to balance performance vs. flexibility in the Anti-Bot engine?

---

## 💻 Development Setup

Since the project is in planning, these steps will be finalized once code is written. For now, here's the intended workflow:

```bash
# Clone the repository
git clone https://github.com/Filip-scripts/arhivanecula.git
cd ahia

# Create a virtual environment
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies (will be listed in requirements.txt)
pip install -r requirements.txt

# Run the main entry point
python main.py
