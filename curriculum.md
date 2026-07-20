# Giants & Gears — a robotics-first mathematics curriculum

**Thesis.** Mathematics is taught as answer-checking: compute, verify, forget.
This curriculum inverts that. Every unit opens with a real robot that cannot do
something — drive straight, reach a target, know where it is — and the
mathematics is *discovered* as the tool that fixes it, the same way humanity
discovered it. The people who found each idea appear as characters with faces,
stakes, and rivalries, because al-Khwarizmi's inheritance problems and Euler's
Königsberg stroll ARE robotics problems in period costume. Correctness is the
floor, not the ceiling: the goal is that a student can *re-derive* an idea
because they know why it had to exist.

**Format.** Offline interactive site (golden-archive museum style). Each unit =
one exhibit hall: a robotics hook → a history thread with portraits → the
mathematics built up interactively → a live simulator lab → a "so the robot
can…" payoff. Every claim runs offline: portraits from the local Wikipedia
archive, diagrams from `ultrapc/diagrams.py`, simulations in vanilla JS.

---

## Stage I — Making a Machine Move at All *(middle school)*

| # | Unit | Robotics hook | Mathematics | Giants | Artifact formula | Interactive lab |
|---|------|---------------|-------------|--------|------------------|-----------------|
| 1 | Gears & Ratios | Two robots, same motor: the one with bigger wheels goes farther per turn. Why? | ratio, rate, proportion, π and circumference, unit conversion | Archimedes | d = 2πr · turns | gear-train playground: mesh gears, watch speed/torque trade |
| 2 | The Robot's Map | A robot told "go to (−3, 2)" — what does a negative place even mean? | integers, signed arithmetic, the coordinate plane | Brahmagupta, Descartes | P = (x, y) | drive a rover on a grid by typing coordinates |
| 3 | The Unknown (al-jabr) | How many motor turns until the wall? You know speed and distance — solve for the missing piece. | linear equations, balancing, slope as speed | al-Khwarizmi | ax + b = c | equation balance scale driving a real countdown-to-wall sim |
| 4 | Rigid Triangles | The diagonal shortcut: drive 3 m east, 4 m north — how far are you from home? | Pythagorean theorem, similar triangles, square roots | Pythagoras, Euclid | a² + b² = c² | stretch a right triangle; watch the squares literally tile |

## Stage II — Sensing and Turning *(early high school)*

| # | Unit | Robotics hook | Mathematics | Giants | Artifact formula | Interactive lab |
|---|------|---------------|-------------|--------|------------------|-----------------|
| 5 | **Angles That Reach (PILOT)** | A 2-link robot arm must touch a target. Which two joint angles? | sine, cosine, tangent, unit circle, atan2, law of cosines → inverse kinematics | Hipparchus, Ptolemy, Aryabhata, Euler | x = L₁cosθ₁ + L₂cos(θ₁+θ₂) | drag a live robot arm; forward & inverse kinematics solve in real time |
| 6 | Machines as Functions | A distance sensor turns echo-time into millimetres. Every robot part is an input→output rule. | functions, domain/range, transformations, composition | Euler (f(x) notation), Dirichlet | y = f(x) | wire sensor→function→motor blocks; compose them |
| 7 | Curves of Decay | Your drone's battery doesn't die linearly. Neither does a signal, or a capacitor. | exponentials, logarithms, half-life, log scales | Napier, Euler (e) | V(t) = V₀e^(−t/τ) | discharge a battery; find τ by sliding a curve onto data |
| 8 | Trusting a Noisy Sensor | Ten ultrasonic pings, ten different answers. Which is true? | mean, variance, distributions, the bell curve | Gauss, Pascal & Fermat | σ² = Σ(x−μ)²/n | live noisy sensor; average n pings, watch the bell emerge |

## Stage III — Describing Motion Exactly *(late high school)*

| # | Unit | Robotics hook | Mathematics | Giants | Artifact formula | Interactive lab |
|---|------|---------------|-------------|--------|------------------|-----------------|
| 9 | Arrows of Motion | Wind pushes the drone one way, its rotors another. What actually happens? | vectors, components, dot product, heading | Hamilton, Grassmann | v = v₁ + v₂ | vector-add forces on a hovering drone |
| 10 | The Rotation Machine | The camera sees "left"; the world says "north-west." Convert. | matrices, rotation matrices, composition of transforms | Cayley, Gauss | R(θ) = [cosθ −sinθ; sinθ cosθ] | rotate frames; stack transforms; see order matter |
| 11 | The Speed of Speed | The encoder gives position ticks. The controller needs velocity — *right now*. | limits, derivatives, tangent lines | Newton vs Leibniz (the war) | v = dx/dt | zoom into a position curve until it turns straight |
| 12 | Adding Up Motion | No GPS indoors: integrate wheel speed to know where you are (and watch error grow). | integrals, accumulation, fundamental theorem | Leibniz, Riemann | x(t) = ∫v dt | dead-reckon a rover; drift accumulates live |
| 13 | Numbers That Rotate | Multiplying by i turns you 90°. Rotation is arithmetic. | complex plane, e^iθ, Euler's identity | Euler, Argand, Hamilton | e^iθ = cosθ + i·sinθ | multiply complex numbers; watch the arm spin |

## Stage IV — The Robot's Bloodstream *(undergraduate core)*

| # | Unit | Robotics hook | Mathematics | Giants | Artifact formula | Interactive lab |
|---|------|---------------|-------------|--------|------------------|-----------------|
| 14 | The Language of Space | Camera calibration, point clouds, least squares: how Gauss found a lost dwarf planet with pen and paper. | linear algebra: Ax=b, eigenvectors, least squares, SVD | Gauss (Ceres!), Cayley, Sylvester | min‖Ax−b‖² | fit a plane to a noisy 3-D point cloud |
| 15 | Many Knobs at Once | Move joint 1 a hair — the hand moves *how much, which way*? The Jacobian is the arm's exchange rate. | partial derivatives, gradients, Jacobians, config space | Lagrange, Jacobi | J = ∂x/∂θ | heat-map an arm's configuration space; singularities glow |
| 16 | Equations of Change | The inverted pendulum (every walking robot is one) obeys an equation about its own rate of change. | ODEs, phase portraits, numerical solvers | Newton, Euler (method), Kovalevskaya (the top) | ẍ = −(g/L)sin x | balance a live inverted pendulum; phase portrait draws itself |
| 17 | Bridges & Routes | Euler's 1736 Königsberg stroll is your robot vacuum's route problem — unchanged. | graphs, trees, Dijkstra/A*, state machines | Euler (Königsberg), Turing | V − E + F = 2 | draw a floor plan; watch A* flood toward the goal |
| 18 | Where Am I, Probably | A lost robot with a map and bad sensors: belief as a probability cloud. | Bayes' rule, conditional probability, estimation | Bayes, Laplace | P(H\|E) ∝ P(E\|H)P(H) | Monte-Carlo localization: particles converge as the robot senses |

## Stage V — Control and Intelligence *(advanced undergrad / early graduate)*

| # | Unit | Robotics hook | Mathematics | Giants | Artifact formula | Interactive lab |
|---|------|---------------|-------------|--------|------------------|-----------------|
| 19 | Taming the Machine | Maxwell wrote "On Governors" (1868) because Victorian engines shook themselves apart — the first feedback mathematics. | feedback, PID, Laplace transforms, poles & stability | Maxwell, Nyquist, Bode, Wiener | G(s) = 1/(s²+2ζωs+ω²) | tune PID gains live; poles migrate across the s-plane |
| 20 | The Best Possible Move | Apollo flew to the Moon on Kalman's filter and Bellman's principle. | state space, LQR, dynamic programming, Kalman filter | Kalman, Bellman, Pontryagin | x̂ₖ = x̂ₖ⁻ + K(zₖ − Hx̂ₖ⁻) | Kalman-filter a tumbling sensor stream; crank the noise |
| 21 | The Shape of Rotation | Hamilton carved i²=j²=k²=ijk=−1 into Broom Bridge in 1843; it now runs inside every drone IMU. | quaternions, SO(3), Rodrigues' formula, screw motion | Hamilton, Rodrigues, Chasles | q = cos(θ/2) + û sin(θ/2) | rotate a 3-D frame with quaternions; gimbal lock demo |
| 22 | Waves Inside Signals | Every sensor stream is a chord of frequencies; filtering is choosing which notes to keep. | Fourier series & transform, sampling theorem | Fourier (Egypt, heat), Shannon | f(t) = Σ cₙe^(inωt) | build a square wave from sines; alias a signal live |

## Stage VI — The Frontier *(graduate)*

| # | Unit | Robotics hook | Mathematics | Giants | Artifact formula | Interactive lab |
|---|------|---------------|-------------|--------|------------------|-----------------|
| 23 | Motion From Energy | Simulators don't push objects around — they minimize action. Lagrange wrote a mechanics book with *no diagrams* and it runs your physics engine. | Euler–Lagrange equations, Hamiltonians, Noether's theorem | Lagrange, Hamilton, **Noether** | d/dt(∂L/∂q̇) − ∂L/∂q = 0 | double pendulum: energy method vs force method, side by side |
| 24 | Curved Configuration Space | A robot's poses form a curved space (SE(3)); planning a motion is drawing a geodesic on it. | manifolds, Lie groups & algebras, geodesics | Riemann, Lie, Cartan | X ∈ 𝔰𝔢(3), exp: 𝔰𝔢(3)→SE(3) | walk a tangent vector around a sphere; holonomy appears |
| 25 | Learning as Descent | Backpropagation is the chain rule; reinforcement learning is Bellman with unknowns. Cauchy invented gradient descent in 1847. | convexity, gradient flows, backprop, RL ↔ optimal control | Cauchy, Kantorovich, Bellman | θ ← θ − α∇L(θ) | descend a loss landscape; get stuck, add momentum |
| 26 | The Mathematics of Not Knowing | SLAM: build the map and find yourself in it, simultaneously, forever uncertain. | stochastic processes, Markov chains, particle filters, Wiener processes | Markov, Wiener, Itô | dX = μdt + σdW | full mini-SLAM: watch map and pose co-converge |

---

## Design invariants (every unit obeys these)

1. **The robot fails first.** No unit opens with a definition. It opens with a
   machine that cannot do something, and the failure is demonstrable in the lab.
2. **History is load-bearing.** The mathematician appears at the moment their
   problem matches the robot's problem — never as a sidebar box.
3. **One artifact formula per unit,** framed in gold like a museum piece, and
   by the end the student can read every symbol in it as a physical statement.
4. **The lab is the assessment.** Success = making the robot work, not marking
   a worksheet. Numerical correctness is checked *by the simulation itself*.
5. **Fully offline.** Portraits from the local Wikipedia archive, diagrams
   generated locally, no CDN, no accounts.
