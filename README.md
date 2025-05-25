# Masse-Feder-Simulation

Dieses Projekt simuliert die Bewegung einer Masse, die an einer Feder befestigt ist, unter Berücksichtigung von Gravitation und Dämpfung. Die Simulation verwendet die VPython-Bibliothek zur 3D-Visualisierung.

## Projektstruktur

- `pendel.py`: Enthält den gesamten Code für die Masse-Feder-Simulation. Hier werden die physikalischen Parameter definiert, die Szene erstellt und die Bewegung der Masse berechnet und visualisiert.

## Anforderungen

Um diese Simulation auszuführen, benötigen Sie Python sowie die VPython-Bibliothek. Sie können VPython mit pip installieren:

```
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