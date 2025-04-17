
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
```

---

## 🧪 How to Use

```bash
python mcp.py run
```

You'll be prompted to enter:

- Your **OpenAI API key**
- Your **Monad wallet address**
- Your **private key** (only stored in memory, not shared)

Then type natural commands like:

```
Gửi 0.01 MON tới 0xABCD1234567890abcdef1234567890ABCDEF12
```

The AI will parse the command and simulate a transaction.

---

## 📌 Example Output

```bash
$ python mcp.py run
Nhập OpenAI API key: ********
Nhập địa chỉ ví Monad: 0x1234...abcd
Nhập private key: ********
Nhập lệnh: Gửi 0.01 MON đến 0xABCD...
AI phân tích: Gửi 0.01 MON đến ví 0xABCD...
Gửi 0.01 MON tới 0xABCD từ 0x1234...abcd
```

---

## 📎 Notes

This project only **simulates** transactions on Monad Testnet. To broadcast real transactions, you need to:

- Encode transaction data
- Sign with private key
- Submit via Monad JSON-RPC

---

## ✅ Requirements

- Python 3.10+
- [OpenAI API key](https://platform.openai.com/account/api-keys)
- Monad Testnet Wallet

---

## 🧠 Author

Built for [MCP Madness Mission 2](https://twitter.com/monad_dev)  
GitHub: [phuc123D](https://github.com/phuc123D)

---

## 📜 License

MIT License
