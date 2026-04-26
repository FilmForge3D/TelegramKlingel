# Über diesen Bot

Dieser Telegram Bot erlaubt eine Klingel auf einem Raspberry Pi aufzusetzen, welche auf den Telegram Befehl `/klingel` reagiert und über den Audioausgang des Pi ein Klingeln abspielt.

Der Bot kann Teil einer Gruppe sein und mit Adminrechten auch die `/klingel` Nachrichten löschen, sodass es kein Spam in der Gruppe gibt.

# Installation

1. `git pull` im Zielverzeichnis durchführen
1. `sudo cp telegram-klingel.service /etc/systemd/system`
1. mit `sudo nano /etc/systemd/system/telegram-klingel.service` den Service bearbeiten und den Pfad anpassen
1. mit `sudo systemctl enable telegram-klingel.service` den Service in den Autostart aufnehmen
1. Eine `token.txt` Datei im Zielverzeichnis anlegen und nur den Telegram-Bot Token in der Datei ablegen. Ein Beispiel hierfür findet sich in der `example.token.txt`

1. mit `sudo raspi-config` Option `4 Performance Options` und `P2 Overlay File System` das Overlay File System aktivieren und die Bootpartition schreibschützen.

# Updates Installieren

Updates installieren prinzipiell automatisch beim Boot, jedoch werden änderungen jedes Mal erneut heruntergeladen. Um ein Update als neue Basis zu installieren muss das Overlay File System für einen Bootvorgang deaktiviert werden.