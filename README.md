
# MCP CLI Monad Assistant

This project is a simple CLI-based AI assistant that interacts with the Monad Testnet.  
It takes natural language prompts like "Send 0.01 MON to 0xAbC..." and generates testnet transactions.

## Features
- OpenAI integration to interpret prompts
- Monad-compatible transaction format (simulated)
- Simple command-line interface with Typer
- Easy to install and extend

## Installation

```bash
git clone https://github.com/yourname/mcp-cli-monad
cd mcp-cli-monad
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python mcp.py run
```

## Requirements
- Python 3.10+
- OpenAI API key
- Monad testnet wallet with MON

## Disclaimer
This version only simulates the transaction. For actual broadcasting, Monad JSON-RPC integration and signature handling must be implemented.
