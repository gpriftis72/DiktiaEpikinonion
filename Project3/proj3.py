import numpy as np
import matplotlib.pyplot as plt

a, b = 0.8, 1.2
p0 = 1e-3
SlotsHronou = 1000
Evros = np.random.default_rng(1)

def N_of(t):
    return 20 if t <= 500 else 40

p = np.zeros(SlotsHronou + 1)
X = np.zeros(SlotsHronou + 1, dtype=int)
p[0] = p0

for t in range(SlotsHronou + 1):

    X[t] = Evros.binomial(N_of(max(t, 1)), p[t])
    if t == SlotsHronou:
        break
    if X[t] == 1:
        p[t + 1] = p[t]
    elif X[t] > 1:
        p[t + 1] = a * p[t]
    else:
        p[t + 1] = min(b * p[t], 1.0)

ts = np.arange(1, SlotsHronou + 1)
epitixia = (X[1:] == 1).astype(float)
T = np.cumsum(epitixia) / ts

print(f"T(500)  = {T[499]:.3f}")
print(f"T(1000) = {T[-1]:.3f}")
print(f"Μέσο p για 300 ≤ t ≤ 500  = {p[300:501].mean():.4f}  (1/20 = 0.05)")
print(f"Μέσο p για 800 ≤ t ≤ 1000 = {p[800:1001].mean():.4f}  (1/40 = 0.025)")

plt.figure(figsize=(9, 4.5))
plt.plot(ts, T, label="T(t)")
plt.axhline(np.exp(-1), color="r", ls="--", label="1/e ≈ 0.368 (θεωρητικό μέγιστο)")
plt.axvline(500, color="purple", ls=":", label="Άυξηση χρηστών: N = 20 → 40")
plt.xlabel("Slot t"); plt.ylabel("Διεκπεραιωτικότητα T(t)")
plt.title("Διεκπεραιωτικότητα T(t)")
plt.ylim(0, 0.6); plt.grid(alpha=0.3); plt.legend()
plt.tight_layout(); plt.savefig("diekperaiotikotita.png", dpi=150)

plt.figure(figsize=(9, 4.5))
plt.plot(ts, p[1:], label="p(t)")
plt.hlines(1/20, 1, 500, colors="r", ls="--", label="Βέλτιστη τιμή p* = 1/N")
plt.hlines(1/40, 500, 1000, colors="r", ls="--")
plt.axvline(500, color="purple", ls=":", label="Αύξηση χρηστών: N = 20 → 40")
plt.xlabel("Slot t"); plt.ylabel("Πιθανότητα p(t)")
plt.title("Πιθανότητα p(t)")
plt.grid(alpha=0.3); plt.legend()
plt.tight_layout(); plt.savefig("pithanotita.png", dpi=150)
plt.show()