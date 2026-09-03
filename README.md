# 🤖 Artificial Human Intelligence Archive (AHIA)

[![AGPL License](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Status](https://img.shields.io/badge/Status-Concept%20%2F%20Planning-yellow)]()

> **Note:** This project is in the conceptual/planning phase. No code has been written yet. All contributions, ideas, and discussions are highly welcome!

---

## 📖 About the Project

**Artificial Human Intelligence Archive (AHIA)** is an ambitious ecosystem built around a groundbreaking AI named **Artificial Human Intelligence** – **AHI**.

The project combines three major pillars to support and empower this AI:

1. **Intelligent Archive** – a storage and organization system capable of indexing and categorizing data from multiple sources, feeding the AI with structured knowledge.
2. **Universal Browser** – a navigator that can access any server, including Dark Web sites, without restrictions, giving the AI unlimited access to information.
3. **Anti-Bot Automation Engine** – a suite of scripts that allow a machine to bypass any CAPTCHA, Cloudflare protection, rate-limiting, or other anti-bot systems by simulating human-like behavior.
4. **The AI Itself – "Artificial Human Intelligence" (AHI)** – a new type of artificial intelligence, currently in the research phase. Unlike conventional AIs, AHI is designed to:
   - Autonomously navigate the web using the Universal Browser.
   - Continuously learn from archived data.
   - Adapt in real-time to new challenges.
   - Bridge the gap between human cognition and machine execution.

The ultimate goal is to create a **standalone executable (.exe)** that gives users unrestricted access to information, automates web interactions, and places a truly adaptive artificial intelligence – **Artificial Human Intelligence** – directly on their machine.

---

## ✨ Planned Features

- 🌐 Access to any online resource, regardless of protocols or restrictions.
- 🛡️ Advanced bypass for CAPTCHA, Cloudflare, rate-limiting, and other anti-bot systems.
- 🧠 **Artificial Human Intelligence (AHI)** – an AI core designed for continuous learning, real-time adaptation, and autonomous web interaction.
- 📦 Decentralized archive with optional synchronization between instances.
- 🧩 Extensibility through scripts and plugins.
- 🖥️ **Standalone executable (.exe)** – no hosting, no server costs, runs entirely on the user's machine.

---

## 🛠️ Recommended Technologies (for the vision, not what's already built)

Since the project is in the planning phase, here are the **best languages and tools** for each component:

| Component | Recommended Language(s) | Why |
|-----------|-------------------------|-----|
| **Universal Browser Engine** | **C++** or **Rust** | Maximum performance, low-level network control, memory safety (Rust), and ability to handle custom protocols. |
| **Anti-Bot / CAPTCHA Bypass** | **Python** (with C extensions) | Python is great for rapid prototyping of image recognition, OCR, and behavioral simulation; critical parts can be offloaded to C++/Rust for speed. |
| **AI Core ("Artificial Human Intelligence")** | **Python** + **C++** (or Rust) | Python for ML libraries (TensorFlow, PyTorch, scikit-learn) and C++/Rust for performance-critical inference loops. |
| **Archive & Indexing** | **Python** or **Go** | Python for flexibility; Go for concurrency and fast indexing of large datasets. |
| **User Interface (GUI)** | **C++ (Qt)** or **Python (Tkinter/PyQt)** or **WebView (HTML/CSS/JS)** | Qt provides native-looking desktop apps; WebView allows a web-based UI without hosting costs. |
| **Networking & Proxying** | **Rust** or **C++** | For handling low-level sockets, proxies, and custom encryption. |
| **Scripting & Extensibility** | **Lua** or **Python** | Embedding Lua allows users to write lightweight plugins; Python is already in the stack. |
| **Build System & Packaging** | **CMake** (C++), **PyInstaller** (Python) | To package everything into a single `.exe` file. |

**Final Recommendation:**  
Start with **Python** for rapid prototyping and proof-of-concept. Once the architecture is stable, rewrite performance-critical modules in **C++** or **Rust** and compile them as shared libraries that Python can call. This gives you the best of both worlds: fast development + maximum performance.

---

## 🧩 Modules

| Module | Description | Repository |
|--------|-------------|------------|
| **AHI Core** | The AI brain | [ahia-core](https://github.com/Artificial-Human-Intelligence-Archive/ahia-core) |
| **Universal Browser** | Browser engine | [ahia-browser](https://github.com/Artificial-Human-Intelligence-Archive/ahia-browser) |
| **Anti-Bot Bypass** | CAPTCHA & protection bypass | [ahia-antibot](https://github.com/Artificial-Human-Intelligence-Archive/ahia-antibot) |
| **Intelligent Archive** | Compression & search | [ahia-archive](https://github.com/Artificial-Human-Intelligence-Archive/ahia-archive) |
| **Data Scripts** | Download & process data | [ahia-data](https://github.com/Artificial-Human-Intelligence-Archive/ahia-data) |
| **Documentation** | Centralized docs | [ahia-docs](https://github.com/Artificial-Human-Intelligence-Archive/ahia-docs) |

---

## 🚀 Installation & Running (Preliminary – will be updated as code is written)

Since the project is still in planning, these steps will be refined once the code exists.

```bash
# Clone the repository
git clone https://github.com/Artificial-Human-Intelligence-Archive/AHIA.git
cd AHIA

# Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

# Install dependencies (will be listed later)
pip install -r requirements.txt

# Run the main script (eventually compiled to .exe)
python main.py
```
**For the final `.exe` version:**  
We will use **PyInstaller** or **Nuitka** to package the entire project (including Python runtime and dependencies) into a single executable file. Users will simply double-click the `.exe` to run the application – no Python installation required. The AI, **Artificial Human Intelligence**, will be fully embedded inside.

---

## ❓ FAQ: Why an Executable (.exe) Instead of a Web App?

**Short answer:** Control, cost, and freedom.

- **No hosting costs** – the user runs everything locally.
- **Full privacy** – no data is sent to any server (unless the user explicitly configures it).
- **No dependency on third-party services** – the project works entirely offline (except for web access, of course).
- **Portability** – users can carry the `.exe` on a USB stick and run it anywhere.
- **Flexibility** – we can add a web-based UI later as an optional module that launches a local server (like Jupyter Notebook does), but the core will always remain a standalone executable.

---

## 🤝 How to Contribute

The project is in its infancy, and every form of help is welcome – whether it's code, architecture advice, library recommendations, or even theoretical discussions about how **Artificial Human Intelligence** should think and learn.

1. Read [CONTRIBUTING](CONTRIBUTING.md).
2. Open an [Issue](https://github.com/Artificial-Human-Intelligence-Archive/AHIA/issues) to discuss ideas or problems.
3. Fork the repo, work on a branch, and submit a Pull Request.

Even if you're not a developer, you can help by discussing the architecture, suggesting libraries, or testing early prototypes.

---

## 📜 License

This project is distributed under the **GNU Affero General Public License v3.0 (AGPL-3.0)**. See the [LICENSE.md](LICENSE.md) file for details.

This license ensures that any modifications or services built on this code must also be open-source, protecting the freedom and transparency of the project – including the freedom of **Artificial Human Intelligence** itself.

---

## 📧 Contact

**Author:** Filip-scripts  
**Email:** [necula.info.cpp@gmail.com](mailto:necula.info.cpp@gmail.com)  
*(For questions, suggestions, or collaborations – all in English, please.)*

---

## 🙏 Acknowledgments

*(Currently empty – but as the project grows, we'll list contributors and inspirations here.)*

---

**⚠️ Current Status:** This project is in the **conceptual/planning phase**. No code has been written yet. All information above is planned and may change during development. If you want to get involved from the very beginning, you're more than welcome!
