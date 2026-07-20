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

print("\nall diagrams written ->", OUT)
