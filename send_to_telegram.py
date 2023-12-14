import asyncio
from telegram import Bot
import subprocess

bot = Bot(token='token_replace')
chat_id = 'chat_id_replace'

async def send_to_telegram(content):
    await bot.send_message(chat_id=chat_id, text=content)

def capture_tmux_session():
    return subprocess.check_output(["tmux", "capture-pane", "-p"]).decode('utf-8')

async def main():
    tmux_content = capture_tmux_session()
    await send_to_telegram(tmux_content)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
