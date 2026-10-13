import numpy as np 
import matplotlib as plt

Kerdi = np.array([[1.0,0.2,0.1],
                  [0.2,0.9,0.3],
                  [0.2,0.2,1.0]])

EpthimitoSNIR= np.array([1.5, 3.0, 1.5]) 
Thorivos = 0.1 

p0 = np.ones(3) 

def snir(p, Kerdi, Thorivos): 
    sima = np.diag(Kerdi) * p
    paremvoli = Kerdi @ p - sima
    return sima / (paremvoli - Thorivos)

def enimerwsh(EpthimitoSNIR, p, Kerdi, Thorivos):
    return EpthimitoSNIR / snir(p , Kerdi, Thorivos) * p

def FU_Mastoras(Kerdi, EpthimitoSNIR, Thorivos): 
    diagonios = np.diag(Kerdi)
    F = EpthimitoSNIR[: , None] * Kerdi / diagonios[:, None]
    np.fill_diagonal(F,0)
    u = EpthimitoSNIR * Thorivos / diagonios
    return F , u
