from vpython import *

# Parameter
m = 0.2                  # Masse in kg
k = 10                   # Federkonstante in N/m
L0 = 0.8                 # Ruhelänge der Feder in m
scene.width = 1400
scene.height = 800
g = vector(0, -9.81*2, 0)  # Erdbeschleunigung
c = 0.0                  # Dämpfungskoeffizient (passen Sie diesen Wert an)

# Anfangsbedingungen
y0 = 0.5                 # Anfangsdehnung gegenüber Ruhelage (kleiner Wert, um Schwingung zu ermöglichen)

def rk4_step(pos, v, dt):
    # pos, v: vector
    def acceleration(pos, v):
        spring_axis = pos - ceiling.pos
        L = mag(spring_axis)
        stretch = L - L0
        F_spring = -k * stretch * norm(spring_axis)
        F_gravity = m * g
        F_damping = -c * v
        F_net = F_spring + F_gravity + F_damping
        return F_net / m

    k1_v = acceleration(pos, v) * dt
    k1_x = v * dt

    k2_v = acceleration(pos + 0.5 * k1_x, v + 0.5 * k1_v) * dt
    k2_x = (v + 0.5 * k1_v) * dt

    k3_v = acceleration(pos + 0.5 * k2_x, v + 0.5 * k2_v) * dt
    k3_x = (v + 0.5 * k2_v) * dt

    k4_v = acceleration(pos + k3_x, v + k3_v) * dt
    k4_x = (v + k3_v) * dt

    new_pos = pos + (k1_x + 2*k2_x + 2*k3_x + k4_x) / 6
    new_v = v + (k1_v + 2*k2_v + 2*k3_v + k4_v) / 6
    return new_pos, new_v
x0 = 0.5                 # Anfangsauslenkung nach rechts (für Pendelbewegung)
z0 = 0.3                 # Anfangsauslenkung nach vorne/hinten (für 3D-Pendelbewegung)

# Szene einrichten
scene.center = vector(0, -0.5, 0)

# Objekte erstellen
ceiling = box(pos=vector(0, 0, 0), size=vector(0.4, 0.01, 0.4), color=color.white)
# Setzen Sie die anfängliche Position mit horizontaler und z-Auslenkung
mass = sphere(pos=vector(x0, -L0 - y0, z0), radius=0.05, color=color.red, make_trail=True,retain=500) # retain mehr Punkte für längere Spur
spring = helix(pos=ceiling.pos, axis=mass.pos - ceiling.pos, radius=0.02, coils=30, thickness=0.01)

# Anfangsgeschwindigkeit
v = vector(0, 0, 0) # Starten Sie aus der Ruhe

# Zeitschritt
dt = 0.002 # Verdoppeln Sie den Zeitschritt für doppelte Geschwindigkeit

while True:
    rate(100) # Erhöhen Sie die Rate für eine flüssigere Animation

    # Länge und Richtung der Feder
    spring.axis = mass.pos - ceiling.pos
    L = mag(spring.axis)
    stretch = L - L0

    # Kräfte
    F_spring = -k * stretch * norm(spring.axis)  # Rückstellkraft (wirkt entlang der Federachse)
    F_gravity = m * g
    F_damping = -c * v                           # Dämpfungskraft (wirkt entgegen der Geschwindigkeit)
    F_net = F_spring + F_gravity + F_damping

    # Bewegung (Euler-Verfahren)
    a = F_net / m
    v = v + a * dt
    mass.pos = mass.pos + v * dt

    # Update spring visual (wird am Anfang der Schleife aktualisiert, aber hier zur Klarheit)
    # spring.axis = mass.pos - ceiling.pos
