import numpy as np
from scipy.io import wavfile

RytmoylisDigmatolipsias, s = wavfile.read('dsbmix.wav')

s = s.astype(np.float32)
t = np.arange(len(s)) / RytmoylisDigmatolipsias

syxnotitoules = np.arange(10000, 14001, 10) 
fasoules = [0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]

MegistiEnergia = -1
HkalhHsyxnothta = 0
ToThitaToKalo = 0
ToIdanikoY = None

for syx in syxnotitoules:
    for thita in fasoules:
    
        y = s * np.cos(2 * np.pi * syx * t + thita)
       
        Energia = np.sum(y**2)

        if Energia > MegistiEnergia:
            MegistiEnergia = Energia
            HkalhHsyxnothta = syx
            ToThitaToKalo = thita
            ToIdanikoY = y
print(f"E megale na ta apotelesmata , eftiaja kai ena arxeio hxoy, etsi gia ta lolz")
print(f"Megisti Energia [E(y)]: {MegistiEnergia}")
print(f"Syxnothta Mixis (fc): {HkalhHsyxnothta} Hz")
print(f"Wraia Fash Mpro mou (thita): {ToThitaToKalo} rad")

KanonikopoiimenoY = np.int16((ToIdanikoY / np.max(np.abs(ToIdanikoY))) * 32767)
wavfile.write('XaxaVrikaThnLexiXixixi.wav', RytmoylisDigmatolipsias, KanonikopoiimenoY)