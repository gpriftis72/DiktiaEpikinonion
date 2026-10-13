#Geia sou file tou GitHub mou ! Edw exw odigies gia thn deyterh ergasia tou Tsouk, appla otan to allazeis mhn to louseis 

import numpy as np #I pio overpowerd vivliothiki fash ever psiloanagaia pata 
import matplotlib as plt

Kerdi = np.array([[1.0,0.2,0.1], # Pinakas sthn dyterh selida mporeus na ton peis G h Gains h kati tetoio
                  [0.2,0.9,0.3],
                  [0.2,0.2,1.0]])

EpthimitoSNIR= np.array([1.5, 3.0, 1.5]) # apo ton epomeno pinaka , pes to gstar h gamastar giati einai to g*
Thorivos = 0.1 #edw afou i timi enai idia den xreiazetai na kaneis pinaka , mppreis na to peis sigma2 h sigmasquare klp

p0 = np.ones(3) # h arxikh isxys kai gua ta 3 pou einai 1 , den mporeus na tou dwseus polla onomata alla mporeis na to kaneis = 1 ant gia to np.ones 

def snir(p, Kerdi, Thorivos): #Metraeei kai epistrefeu to SNIR 
    sima = np.diag(Kerdi) * p
    paremvoli = Kerdi @ p - sima
    return sima / (paremvoli - Thorivos)

def enimerwsh(EpthimitoSNIR, p, Kerdi, Thorivos): #enimerwnei thn ixsxy kathe xrhsth me vash to SNIR pou exv vw stoxo kai to trexon SNIR 
    return EpthimitoSNIR / snir(p , Kerdi, Thorivos) * p

def FU_Mastoras(Kerdi, EpthimitoSNIR, Thorivos): # ftisxnei ton pinaka F kai to dianisma u pou zitaei h (1) sthn prwth selida 
    diagonios = np.diag(Kerdi)
    F = EpthimitoSNIR[: , None] * Kerdi / diagonios[:, None]
    np.fill_diagonal(F,0)
    u = EpthimitoSNIR * Thorivos / diagonios
    return F , u
