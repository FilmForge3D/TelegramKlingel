#!/usr/bin/env python
# pylint: disable=unused-argument
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from pydub import AudioSegment
from pydub.playback import play
import random

with open('token.txt', 'r') as file:
    TOKEN = file.read()

soundfiles = ["Audio/Klingel1.mp3",
              "Audio/Klingel2.mp3",
              "Audio/Klingel3.mp3",
              "Audio/Klingel4.mp3",
              "Audio/Klingel5.mp3",
              "Audio/Klingel6.mp3",
              "Audio/Klingel7.mp3",
              "Audio/Klingel8.mp3",
              "Audio/Klingel9.mp3",
              "Audio/Klingel10.mp3"]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Erklärt die Funktion des Bots"""
    random.seed(update.effective_message.chat_id)
    await update.message.reply_text("Mit /klingel klingelt es im Saal")

async def klingel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Wählt eine Zufällige Klingel aus und spielt diese ab, nach dem Klingeln wird der Befehl gelöscht"""
    audiofile = random.choice(soundfiles)
    sound = AudioSegment.from_mp3(audiofile)
    play(sound)
    await context.bot.delete_message(chat_id=update.message.chat_id,message_id=update.message.message_id)

def main() -> None:
    # Anwendung mit API-Token starten
    application = Application.builder().token(TOKEN).build()
    # Telegrambefehle auf Funktionen Mappen
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("klingel", klingel))
    # Der Bot läuft unendlich weiter
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()