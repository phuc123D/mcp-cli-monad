# 🧠 MCP CLI Monad Assistant

A minimal and AI-powered command-line assistant that interacts with the Monad Testnet using natural language prompts.

![demo](./mcp_cli_demo.png)

---

## 🚀 Features

- 🌐 Use OpenAI to understand plain-text commands like:  
  `"Gửi 0.01 MON tới 0xABCD..."`

- 🔐 Interacts with Monad wallet (simulated TX)
- 💬 Built with `Typer`, `Rich`, and `OpenAI API`
- ⚡ Simulates broadcasting testnet transactions

---

## 🛠️ Installation

```bash
git clone https://github.com/phuc123D/mcp-cli-monad
cd mcp-cli-monad

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
