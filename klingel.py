#!/usr/bin/env python
# pylint: disable=unused-argument
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import vlc

def create_instance(device: str) -> vlc.Instance:
    """Erzeugt eine VLC-Instanz für das angegebene ALSA-Gerät"""
    instance = vlc.Instance('--aout=alsa', f'--alsa-audio-device={device}', '--no-video')
    if instance is None:
        raise RuntimeError(f"VLC konnte für {device} nicht initialisiert werden (ALSA-Gerät vorhanden?)")
    return instance

instance0 = create_instance('plughw:0,0')
instance1 = create_instance('plughw:1,0')
player0 = instance0.media_player_new()
vlc.libvlc_audio_set_volume(player0, 100)
player1 = instance1.media_player_new()
vlc.libvlc_audio_set_volume(player1, 100)

with open('token.txt', 'r') as file:
    TOKEN = file.read().strip()

soundfiles = ["Audio/Klingel01.mp3",
              "Audio/Klingel02.mp3",
              "Audio/Klingel03.mp3",
              "Audio/Klingel04.mp3",
              "Audio/Klingel05.mp3",
              "Audio/Klingel06.mp3",
              "Audio/Klingel07.mp3",
              "Audio/Klingel08.mp3",
              "Audio/Klingel09.mp3",
              "Audio/Klingel10.mp3",
              "Audio/Klingel11.mp3",
              "Audio/Klingel12.mp3",
              "Audio/Klingel13.mp3",
              "Audio/Klingel14.mp3"]

startup_sounds = ["Audio/Boot01.mp3",
                  "Audio/Boot02.mp3",
                  "Audio/Boot03.mp3",
                  "Audio/Boot04.mp3",
                  "Audio/Boot05.mp3",
                  "Audio/Boot06.mp3",
                  "Audio/Boot07.mp3",
                  "Audio/Boot08.mp3",
                  "Audio/Boot09.mp3",
                  "Audio/Boot10.mp3",
                  "Audio/Boot11.mp3"]

def play(audiofile: str) -> None:
    """Spielt eine Audiodatei auf beiden Ausgängen ab"""
    media0 = instance0.media_new(audiofile)
    player0.set_media(media0)
    player0.play()
    media1 = instance1.media_new(audiofile)
    player1.set_media(media1)
    player1.play()

async def post_init(application: Application) -> None:
    """Wird nach erfolgreicher Verbindung mit der Telegram API aufgerufen"""
    print(f"Verbunden als @{application.bot.username}")
    play(random.choice(startup_sounds))

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Erklärt die Funktion des Bots"""
    if update.message is None:
        return
    await update.message.reply_text("Mit /klingel klingelt es im Saal")

async def klingel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Wählt eine Zufällige Klingel aus und spielt diese ab, nach dem Klingeln wird der Befehl gelöscht"""
    if update.message is None:
        return
    play(random.choice(soundfiles))
    await update.message.delete()

def main() -> None:
    # Anwendung mit API-Token starten
    application = Application.builder().token(TOKEN).post_init(post_init).build()
    # Telegrambefehle auf Funktionen Mappen
    application.add_handler(CommandHandler(["start", "help"], start))
    application.add_handler(CommandHandler("klingel", klingel))
    # Der Bot läuft unendlich weiter
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()