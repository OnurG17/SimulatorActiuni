import numpy
import math

class Actiuni:
    DictionarFluctuatiiActiuni={} #cheile sunt nume de actiuni si valorile asociate sunt liste cu fluctuatii.

    luni=0
    buget_initial=0
    buget_lunar=0

    @classmethod
    def timp_actiuni(cls,ani):
        if cls.luni==0:
            cls.luni=int(ani*12)

    @classmethod
    def date_actiune(cls,nume,performanta,volatilitate):
        performanta=performanta/100
        volatilitate=volatilitate/100

        Generator_random=numpy.random.default_rng()
        fluctuatii=[1]
        
        for i in range(1,cls.luni):
            random=Generator_random.normal(loc=0.0, scale=1.0, size=None)
            fluctuatii.append(1+((1+performanta)**(1/12) - 1 - volatilitate**2/2/12 + volatilitate*random*math.sqrt(1/12)))

            #fluctuatii[i]=fluctuatii[i-1]*(1+(1+performanta)**1/12 - 1 - volatilitate**2/2/12 + volatilitate*random*math.sqrt(1/12))
            #fluctuatii[i]=max(0,fluctuatii[i]) #pentru memorie prealocata

        cls.DictionarFluctuatiiActiuni[nume]=fluctuatii

    @classmethod
    def valori_actiune(cls,nume,suma_start,suma_lunar):
        cls.buget_initial=suma_start
        cls.buget_lunar=suma_lunar

        valori=[suma_start] #se poate prealoca memoria listei valori=[0]*cls.luni,astfel nu ar mai fi nevoie de append()
        
        for i in range(1,cls.luni):
            valori.append(valori[i-1]*(cls.DictionarFluctuatiiActiuni[nume][i])+suma_lunar)
            valori[i]=max(valori[i],0)
            
        return valori

    @classmethod
    def rebalansare(cls):
        valori_portofoliu=[0]*cls.luni
        valori_portofoliu[0]=cls.buget_initial
        
        buget_actiune=cls.buget_initial/len(cls.DictionarFluctuatiiActiuni)
        DictionarPortofoliu={}
        
        for actiune in cls.DictionarFluctuatiiActiuni:
            DictionarPortofoliu[actiune]=buget_actiune
        
        for i in range(1,cls.luni):
            minim=100 #o valoare mai mare decat orice fluctuatie din portofoliu.
            actiune_minim=""
            for fluctuatie_luna in cls.DictionarFluctuatiiActiuni:
                if cls.DictionarFluctuatiiActiuni[fluctuatie_luna][i]<minim:
                    minim=cls.DictionarFluctuatiiActiuni[fluctuatie_luna][i]
                    actiune_minim=fluctuatie_luna
                    
            for actiune in DictionarPortofoliu:
                DictionarPortofoliu[actiune] *= cls.DictionarFluctuatiiActiuni[actiune][i]
                valori_portofoliu[i] += DictionarPortofoliu[actiune]
                
            DictionarPortofoliu[actiune_minim] += cls.buget_lunar
            valori_portofoliu[i] +=cls.buget_lunar
            
        return valori_portofoliu
    
    @classmethod
    def resetare(cls):
        cls.DictionarFluctuatiiActiuni={}
        cls.luni=0
        cls.buget_initial=0
        cls.buget_lunar=0
        
    @classmethod
    def convertire_valori(cls,valori): #primeste o lista de valori si da o lista de fluctuatii
        fluctuatii=[0]*len(valori)
        fluctuatii[0]=1
        
        for i in range(1,len(valori)):
            fluctuatii[i]=valori[i]/valori[i-1]
            
        return fluctuatii
        
