import json
import os
from dotenv import load_dotenv

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes, Application, CommandHandler

from app.schemas.word_model import WordModel
from app.services.rae.router import get_word

load_dotenv()
CHUNK_SIZE = 4096


async def get_definition(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    word: str = update.message.text.split(" ")[1]
    response: WordModel = get_word(word)

    json_str = json.dumps(response.model_dump(), indent=4, ensure_ascii=False)

    chunks = [json_str[i: i + CHUNK_SIZE] for i in range(0, len(json_str), CHUNK_SIZE)]
    for chunk in chunks:
        await update.message.reply_text(text=f"\n ```json\n{chunk}\n```",
                                        parse_mode=ParseMode.MARKDOWN_V2)


if __name__ == '__main__':
    application = Application.builder().token(os.getenv("TELEGRAM_TOKEN")).build()
    handler = CommandHandler("definition", get_definition)
    application.add_handler(handler, -1)
    application.run_polling(allowed_updates=Update.ALL_TYPES)
