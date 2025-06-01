# Masse-Feder-Simulation

Dieses Projekt simuliert die Bewegung einer Masse, die an einer Feder befestigt ist, unter Berücksichtigung von Gravitation und Dämpfung. Die Simulation verwendet die VPython-Bibliothek zur 3D-Visualisierung.

<p align="right" style="float: right; margin-left: 20px;">
    <a href="https://www.youtube.com/shorts/MSY_UUy0_Ds">
        <img src="pendel.jpg" alt="Masse-Feder-Simulation" width="250">
    </a>
</p>
Online-Demo: [Online-demo](https://qualcuno.github.io/Pendel/)
Der Screenshot rechts zeigt die 3D-Visualisierung der Masse-Feder-Simulation. Klicken Sie auf das Bild, um eine kurze Video-Demonstration auf YouTube zu sehen.

## Projektstruktur

- `pendel.py`: Enthält den gesamten Code für die Masse-Feder-Simulation. Hier werden die physikalischen Parameter definiert,
-  die Szene erstellt und die Bewegung der Masse berechnet und visualisiert.
 
## Anforderungen

Um diese Simulation auszuführen, benötigen Sie Python sowie die VPython-Bibliothek. Sie können VPython mit pip installieren:

```shell
pip install vpython
```

## Ausführung der Simulation

Nachdem Sie die Anforderungen installiert haben, können Sie die Simulation ausführen, indem Sie das `pendel.py`-Skript starten:

```
python pendel.py
```

Dadurch wird ein Fenster gestartet, das die Masse-Feder-Simulation anzeigt. Sie können die Szene mit der Maus drehen und zoomen.

## Anpassung der Simulation

Im `pendel.py`-Skript können Sie verschiedene Parameter anpassen, um das Verhalten der Simulation zu ändern:

- `m`: Masse des Objekts
- `k`: Federkonstante
- `L0`: Ruhelänge der Feder
- `g`: Gravitationsvektor
- `c`: Dämpfungskoeffizient
- `y0`, `x0`, `z0`: Anfangsauslenkungen der Masse
- `v`: Anfangsgeschwindigkeit der Masse
- `dt`: Zeitschritt der Simulation
- `rate()`: Steuert die Geschwindigkeit der Animation
- `retain`: Anzahl der Punkte, die in der Spur der Masse beibehalten werden

Experimentieren Sie mit diesen Werten, um verschiedene Schwingungsarten und Dämpfungseffekte zu beobachten.

## Video-Demonstration

Eine Beispiel-Demonstration der Simulation finden Sie auf [YouTube](https://www.youtube.com/shorts/MSY_UUy0_Ds).

## Screenshot
<p align="right" style="float: right; margin-left: 20px;">
    <a href="https://www.youtube.com/shorts/MSY_UUy0_Ds">
        <img src="pendel.jpg" alt="Masse-Feder-Simulation" width="250">
    </a>
</p>
Der Screenshot rechts zeigt die 3D-Visualisierung der Masse-Feder-Simulation. Klicken Sie auf das Bild, um eine kurze Video-Demonstration auf YouTube zu sehen.

## HTML-Version

Neben der Python-Implementation ist auch eine eigenständige HTML/JavaScript-Version der Simulation verfügbar.

### pendel.html

Die HTML-Version verwendet Three.js zur 3D-Visualisierung und implementiert das gleiche physikalische Modell wie die Python-Version, jedoch mit diesen zusätzlichen Funktionen:

- Keine Installation erforderlich - läuft in jedem modernen Webbrowser
- Interaktive Steuerelemente für Dämpfung und Federkonstante
- Möglichkeit, die Masse anzuschupsen (durch Klicken oder Tasten)
- Einstellbare Schubstärke für dynamische Interaktionen

### Ausführung der HTML-Version

Um die HTML-Version auszuführen, öffnen Sie einfach die Datei `pendel.html` in einem Webbrowser:

```shell
# Unter macOS
open pendel.html

# Alternativ mit einem bestimmten Browser
firefox pendel.html
chrome pendel.html
```