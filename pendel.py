from vpython import vector, box, sphere, helix, color, scene, wtext, slider, button, rate, norm, mag

# --- UI Widgets ---
scene.width = 1400
scene.height = 800
scene.title = "Federpendel mit einstellbaren Parrametern und Anstupsen"

# Standardwerte
m = 0.2
k = 10
L0 = 0.8
c = 0.0
g = vector(0, -9.81*2, 0)

# UI-Elemente
wtext(text="Masse (kg): ")
m_slider = slider(min=0.05, max=2, value=m, length=200, bind=lambda s: None, step=0.01)
m_val = wtext(text=f"{m_slider.value:.2f}\n")

wtext(text="Federkonstante (N/m): ")
k_slider = slider(min=1, max=50, value=k, length=200, bind=lambda s: None, step=0.1)
k_val = wtext(text=f"{k_slider.value:.1f}\n")

wtext(text="Ruhelänge (m): ")
L0_slider = slider(min=0.1, max=2, value=L0, length=200, bind=lambda s: None, step=0.01)
L0_val = wtext(text=f"{L0_slider.value:.2f}\n")

wtext(text="Dämpfung: ")
c_slider = slider(min=0, max=2, value=c, length=200, bind=lambda s: None, step=0.01)
c_val = wtext(text=f"{c_slider.value:.2f}\n")

scene.append_to_caption("\n")

def nudge_xp(): nudge(vector(2,0,0))
def nudge_xn(): nudge(vector(-2,0,0))
def nudge_yp(): nudge(vector(0,2,0))
def nudge_yn(): nudge(vector(0,-2,0))
def nudge_zp(): nudge(vector(0,0,2))
def nudge_zn(): nudge(vector(0,0,-2))

button(text="Anstupsen +x", bind=lambda _: nudge_xp())
button(text="Anstupsen -x", bind=lambda _: nudge_xn())
button(text="Anstupsen +y", bind=lambda _: nudge_yp())
button(text="Anstupsen -y", bind=lambda _: nudge_yn())
button(text="Anstupsen +z", bind=lambda _: nudge_zp())
button(text="Anstupsen -z", bind=lambda _: nudge_zn())

scene.append_to_caption("\n\n")

# --- Anfangsbedingungen ---
y0 = 0.5
x0 = 0.5
z0 = 0.3

scene.center = vector(0, -0.5, 0)
ceiling = box(pos=vector(0, 0, 0), size=vector(0.4, 0.01, 0.4), color=color.white)
mass = sphere(pos=vector(x0, -L0 - y0, z0), radius=0.05, color=color.red, make_trail=True, retain=500)
spring = helix(pos=ceiling.pos, axis=mass.pos - ceiling.pos, radius=0.02, coils=30, thickness=0.01)

v = vector(0, 0, 0)
dt = 0.004

def rk4_step(pos, v, dt):
    def acceleration(pos, v):
        spring_axis = pos - ceiling.pos
        L = mag(spring_axis)
        stretch = L - L0_slider.value
        F_spring = -k_slider.value * stretch * norm(spring_axis)
        F_gravity = m_slider.value * g
        F_damping = -c_slider.value * v
        F_net = F_spring + F_gravity + F_damping
        return F_net / m_slider.value

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

def nudge(impulse=vector(2,0,0)):
    global v
    v += impulse

# --- Pfeiltasten-Steuerung ---
def keydown(evt):
    key = evt.key
    if key == 'left':
        nudge(vector(-2,0,0))
    elif key == 'right':
        nudge(vector(2,0,0))
    elif key == 'up':
        nudge(vector(0,0,-2))
    elif key == 'down':
        nudge(vector(0,0,2))
    elif key == 'w':
        nudge(vector(0,2,0))
    elif key == 's':
        nudge(vector(0,-2,0))

scene.bind('keydown', keydown)

# --- Maus-Anstupsen ---
dragging = False
drag_start = None

def mousedown(evt):
    global dragging, drag_start
    obj = evt.pick
    if obj is mass:
        dragging = True
        drag_start = evt.pos

def mouseup(evt):
    global dragging, drag_start
    if dragging and drag_start is not None:
        drag_end = evt.pos
        impulse = drag_end - drag_start
        if mag(impulse) > 0.01:
            nudge(norm(impulse)*2)
    dragging = False
    drag_start = None

scene.bind('mousedown', mousedown)
scene.bind('mouseup', mouseup)

while True:
    rate(100)

    # Update UI-Anzeigen
    m_val.text = f"{m_slider.value:.2f}\n"
    k_val.text = f"{k_slider.value:.1f}\n"
    L0_val.text = f"{L0_slider.value:.2f}\n"
    c_val.text = f"{c_slider.value:.2f}\n"

    # Update Feder und Bewegung
    spring.axis = mass.pos - ceiling.pos
    mass.pos, v = rk4_step(mass.pos, v, dt)
