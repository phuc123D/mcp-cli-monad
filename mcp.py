
import typer
import openai
import requests
from rich import print
from getpass import getpass

app = typer.Typer()

openai.api_key = getpass("Nhập OpenAI API key: ")
WALLET_ADDRESS = typer.prompt("Nhập địa chỉ ví Monad")
PRIVATE_KEY = getpass("Nhập private key của ví Monad (không chia sẻ cho ai!)")

MONAD_RPC = "https://node.devnet.monad.xyz"

def create_transaction(to_address: str, amount: float):
    print(f"[bold green]Gửi {amount} MON tới {to_address} từ {WALLET_ADDRESS}[/bold green]")
    # Giao dịch thật sẽ cần xử lý JSON-RPC và ký giao dịch tại đây

@app.command()
def run():
    prompt = typer.prompt("Nhập lệnh (ví dụ: Gửi 0.01 MON đến 0xABC...)")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{
            "role": "system",
            "content": "Bạn là một trợ lý phân tích giao dịch Monad."
        }, {
            "role": "user",
            "content": prompt
        }]
    )

    content = response['choices'][0]['message']['content']
    print(f"[yellow]AI phân tích:[/yellow] {content}")

    import re
    match = re.search(r'(\d+\.\d+)\s*MON.*(0x[a-fA-F0-9]{40})', content)
    if match:
        amount = float(match.group(1))
        to_address = match.group(2)
        create_transaction(to_address, amount)
    else:
        print("[red]Không hiểu yêu cầu. Vui lòng nhập lại rõ ràng.[/red]")

if __name__ == "__main__":
    app()
