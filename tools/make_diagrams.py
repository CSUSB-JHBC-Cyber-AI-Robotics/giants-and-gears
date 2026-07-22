"""Generate the site's diagrams in the DaVinci Ink style (ultrapc.diagrams
ink_flow / ink_network) and the 'artifact formula' SVGs (matplotlib mathtext).

Run:  py -3.11 make_diagrams.py
"""
import sys
from pathlib import Path

ULTRA = Path(r"C:\Users\desmo\AI Programs\Ultra-PC")
sys.path.insert(0, str(ULTRA))

from ultrapc import diagrams  # noqa: E402

OUT = Path(__file__).resolve().parent.parent / "assets" / "img" / "diagrams"
OUT.mkdir(parents=True, exist_ok=True)

GOLD = "#f2dc9b"        # for dark plates (legacy)
INK = "#3a2c1a"          # iron-gall ink, for formulas on parchment


def save(name: str, svg: str) -> None:
    (OUT / f"{name}.svg").write_text(svg, encoding="utf-8")
    print(f"  ok {name}.svg")


# ============ FOLIO 05 — Angles That Reach ============

save("ik-pipeline", diagrams.ink_flow(
    [("Target (x, y)", "where we WANT the hand", "blue"),
     ("Joint angles θ₁, θ₂", "inverse kinematics", "yellow"),
     ("Motor commands", "electricity, finally", "orange"),
     ("Hand at target", "forward kinematics agrees", "green")],
    arrows=["law of cosines + atan2", "controller", "physics"],
    return_label="encoders measure the REAL angles — feedback closes the loop",
    title="How a robot arm reaches",
    caption="Trigonometry is the translator between 'where' and 'how much to turn'."))

save("trig-history", diagrams.ink_network(
    [("hip", "Hipparchus\n~150 BC · chords", "orange"),
     ("pto", "Ptolemy\n~150 AD · chord tables", "yellow"),
     ("ary", "Aryabhata\n499 AD · half-chord = sine", "green"),
     ("alk", "al-Khwārizmī\n~820 · sine tables + algebra", "purple"),
     ("eul", "Euler\n1748 · sin as a FUNCTION", "blue"),
     ("rob", "Your robot arm\ntoday · atan2()", "red")],
    [("hip", "pto", "star catalogs"), ("pto", "ary", "via trade routes"),
     ("ary", "alk", "House of Wisdom"), ("alk", "eul", "translation era"),
     ("eul", "rob", "unchanged since 1748")],
    pos={"hip": (0, 0.75), "pto": (1, -0.65), "ary": (2, 0.75),
         "alk": (3, -0.65), "eul": (4, 0.75), "rob": (5, -0.65)},
    directed=True,
    title="Nineteen centuries to name a ratio",
    caption="Every arrow is a civilization handing the problem to the next one."))

# ============ FOLIO 01 — Gears & Ratios ============

save("gear-pipeline", diagrams.ink_flow(
    [("Motor turns", "what the robot commands", "orange"),
     ("Gear pair N₁ : N₂", "the ratio machine", "yellow"),
     ("Wheel turns", "slower, but stronger", "blue"),
     ("Distance rolled", "what the world measures", "green")],
    arrows=["× N₁/N₂", "each turn rolls 2πr", ""],
    title="How a motor turn becomes a metre",
    caption="Two multiplications stand between electricity and geography."))

save("gears-history", diagrams.ink_network(
    [("arch", "Archimedes\n~250 BC · the lever & the ratio", "orange"),
     ("anti", "Antikythera mechanism\n~100 BC · 30+ bronze gears", "yellow"),
     ("jaz", "al-Jazarī\n1206 · gears that DO things", "purple"),
     ("leo", "Leonardo's notebooks\n~1495 · gear trains drawn to be built", "red"),
     ("rob", "Your drivetrain\ntoday · N₁/N₂", "blue")],
    [("arch", "anti", "ratio as machine"), ("anti", "jaz", "lost, then found"),
     ("jaz", "leo", "translated westward"), ("leo", "rob", "unchanged idea")],
    pos={"arch": (0, 0.7), "anti": (1, -0.6), "jaz": (2, 0.7),
         "leo": (3, -0.6), "rob": (4, 0.7)},
    directed=True,
    title="The ratio, cast in bronze",
    caption="A gear pair is a fraction you can hold."))

# ============ FOLIO 02 — The Robot's Map ============

save("coords-history", diagrams.ink_network(
    [("bra", "Brahmagupta\n628 · debts BELOW zero", "orange"),
     ("kwa", "House of Wisdom\n~820 · negatives travel west", "purple"),
     ("des", "Descartes\n1637 · the fly on the ceiling", "yellow"),
     ("rob", "Your rover\ntoday · goto(x, y)", "blue")],
    [("bra", "kwa", "trade + translation"), ("kwa", "des", "algebra meets geometry"),
     ("des", "rob", "every map since")],
    pos={"bra": (0, 0.7), "kwa": (1, -0.6), "des": (2, 0.7), "rob": (3, -0.6)},
    directed=True,
    title="How places became pairs of numbers",
    caption="A negative number is not less than nothing — it is the other direction."))

# ============ FOLIO 03 — The Unknown (al-jabr) ============

save("aljabr-pipeline", diagrams.ink_flow(
    [("The unknown t", "hidden inside the machine", "orange"),
     ("al-jabr", "restore: undo + and −", "yellow"),
     ("al-muqābala", "balance: undo ×", "purple"),
     ("t, known", "exact — no guessing", "green")],
    arrows=["− b from both sides", "÷ s on both sides", ""],
    title="The two moves that solve everything linear",
    caption="Whatever you do to one side of the balance, you owe the other."))

# ============ FOLIO 04 — Rigid Triangles ============

save("triangle-history", diagrams.ink_network(
    [("rope", "Egyptian rope-stretchers\n~2000 BC · 3-4-5 knots", "orange"),
     ("pyt", "Pythagoras\n~530 BC · WHY it works", "yellow"),
     ("euc", "Euclid\n~300 BC · Elements I.47, proved forever", "purple"),
     ("rob", "Your rover\ntoday · hypot(a, b)", "blue")],
    [("rope", "pyt", "recipe becomes question"), ("pyt", "euc", "question becomes proof"),
     ("euc", "rob", "proof becomes code")],
    pos={"rope": (0, 0.7), "pyt": (1, -0.6), "euc": (2, 0.7), "rob": (3, -0.6)},
    directed=True,
    title="Four thousand years of the same triangle",
    caption="The rope-stretchers knew THAT it works; Pythagoras asked WHY; Euclid closed the case."))

# ============ Artifact formulas (matplotlib mathtext -> transparent SVG) ====

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

matplotlib.rcParams["mathtext.fontset"] = "cm"
matplotlib.rcParams["svg.fonttype"] = "path"   # glyphs as paths: no font needed


def formula(name: str, tex: str, size: int = 30, color: str = INK) -> None:
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, f"${tex}$", fontsize=size, color=color)
    fig.savefig(OUT / f"{name}.svg", format="svg", transparent=True,
                bbox_inches="tight", pad_inches=0.06)
    plt.close(fig)
    print(f"  ok {name}.svg")


# Folio 05
formula("f-forward-kinematics",
        r"x = L_1\cos\theta_1 + L_2\cos(\theta_1{+}\theta_2)\qquad "
        r"y = L_1\sin\theta_1 + L_2\sin(\theta_1{+}\theta_2)")
formula("f-law-of-cosines",
        r"c^2 = a^2 + b^2 - 2ab\cos C")
formula("f-ik-elbow",
        r"\cos\theta_2 \;=\; \frac{x^2 + y^2 - L_1^2 - L_2^2}{2\,L_1 L_2}")
formula("f-atan2",
        r"\theta_1 = \mathrm{atan2}(y,\,x)\;-\; "
        r"\mathrm{atan2}\left(L_2\sin\theta_2,\; L_1{+}L_2\cos\theta_2\right)")
formula("f-unit-circle",
        r"\sin^2\theta + \cos^2\theta = 1")
formula("f-euler",
        r"e^{i\theta} = \cos\theta + i\,\sin\theta")

# Folio 01
formula("f-circumference",
        r"d \;=\; 2\pi r \,\times\, \mathrm{turns}")
formula("f-gear-ratio",
        r"\mathrm{wheel\ turns} \;=\; \mathrm{motor\ turns}\times\frac{N_1}{N_2}")
formula("f-torque-trade",
        r"\tau_{\mathrm{wheel}} \;=\; \tau_{\mathrm{motor}}\times\frac{N_2}{N_1}")
formula("f-drive-distance",
        r"D \;=\; \mathrm{turns}\times\frac{N_1}{N_2}\times 2\pi r")

# Folio 02
formula("f-ordered-pair",
        r"P = (x,\; y)")
formula("f-displacement",
        r"\Delta x = x_2 - x_1 \qquad \Delta y = y_2 - y_1")

# Folio 03
formula("f-linear",
        r"s\,t + b \;=\; D")
formula("f-solve-t",
        r"t \;=\; \frac{D - b}{s}")

# Folio 04
formula("f-pythagoras",
        r"a^2 + b^2 = c^2")
formula("f-distance",
        r"d \;=\; \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}")

# ============ FOLIO 06 — Machines as Functions ============
save("function-machine", diagrams.ink_flow(
    [("Echo time  t", "the sensor's raw number", "blue"),
     ("f( t )", "halve it, times the speed of sound", "yellow"),
     ("Distance  d", "millimetres, at last", "green")],
    arrows=["the rule f", "read it off"],
    title="A sensor is a function",
    caption="Same input, same output — every time. That is what makes it a machine you can trust."))

formula("f-function", r"y \;=\; f(x)")
formula("f-sonar", r"d \;=\; \frac{v \cdot t}{2}")
formula("f-compose", r"(g \circ f)(x) \;=\; g(\,f(x)\,)")

# ============ FOLIO 07 — Curves of Decay ============
save("decay-history", diagrams.ink_network(
    [("nap", "Napier\n1614 · logarithms", "purple"),
     ("eul", "Euler\n1748 · the number e", "blue"),
     ("rc", "The RC circuit\nvoltage bleeds away", "green"),
     ("bat", "Your drone battery\ntoday · V₀e^(−t/τ)", "red")],
    [("nap", "eul", "e is log's natural base"),
     ("eul", "rc", "continuous decay"),
     ("rc", "bat", "the same curve")],
    pos={"nap": (0, 0.7), "eul": (1, -0.6), "rc": (2, 0.7), "bat": (3, -0.6)},
    directed=True,
    title="How nothing dies in a straight line",
    caption="Halving, and halving again — the signature of decay."))

formula("f-decay", r"V(t) \;=\; V_0\, e^{-t/\tau}")
formula("f-log", r"t \;=\; -\,\tau \ln\!\left(\frac{V}{V_0}\right)")
formula("f-halflife", r"t_{1/2} \;=\; \tau \ln 2")

# ============ FOLIO 08 — Trusting a Noisy Sensor ============
save("stats-history", diagrams.ink_network(
    [("pf", "Pascal & Fermat\n1654 · letters on chance", "purple"),
     ("gauss", "Gauss\n~1809 · the bell & least squares", "blue"),
     ("sensor", "Your ultrasonic sensor\ntoday · average of n pings", "red")],
    [("pf", "gauss", "chance becomes a curve"),
     ("gauss", "sensor", "noise has a shape")],
    pos={"pf": (0, 0.6), "gauss": (1, -0.5), "sensor": (2, 0.6)},
    directed=True,
    title="Noise is not chaos — it has a shape",
    caption="Average enough pings and the truth rises out of the scatter."))

formula("f-mean", r"\mu \;=\; \frac{1}{n}\sum_{i=1}^{n} x_i")
formula("f-variance", r"\sigma^2 \;=\; \frac{1}{n}\sum_{i=1}^{n}(x_i-\mu)^2")
formula("f-gaussian",
        r"p(x) \;=\; \frac{1}{\sigma\sqrt{2\pi}}\; e^{-(x-\mu)^2 / 2\sigma^2}")

print("\nall diagrams written ->", OUT)
