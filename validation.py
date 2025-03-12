import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import pandas as pd



NIST_V = np.array([1.4138,-3.6467,10.965,339.76])
NIST_L = np.array([1.8667,-1.3421,8.1825,339.77])

NRTL_V = np.array([-2.3614,2.3724,7.8881,340.11])
NRTL_L = np.array([-2.209,5.2926,4.7949,340.18])

pts = 100
x_vals = np.linspace(0, 1, pts)

nist_vap_t=np.zeros(pts) #temps
nist_liq_t=np.zeros(pts) 

nrtl_vap_t = np.zeros(pts) 
nrtl_liq_t = np.zeros(pts) 

def txy(x):
    #x is an array
    #vapor pressure
    
    for i in range(pts):
        nist_vap_t[i] = NIST_V[0]*(x[i]**3)+NIST_V[1]*(x[i]**2)+NIST_V[2]*x[i]+NIST_V[3]
        nist_liq_t[i] = NIST_L[0]*(x[i]**3)+NIST_L[1]*(x[i]**2)+NIST_L[2]*x[i]+NIST_L[3]
        nrtl_vap_t[i] = NRTL_V[0]*(x[i]**3)+NRTL_V[1]*(x[i]**2)+NRTL_V[2]*x[i]+NRTL_V[3]
        nrtl_liq_t[i] = NRTL_L[0]*(x[i]**3)+NRTL_L[1]*(x[i]**2)+NRTL_L[2]*x[i]+NRTL_L[3]

txy(x_vals)

plt.rcParams['figure.dpi'] = 500
plt.rcParams['font.family'] = "Arial"
#nist
plt.figure()
plt.plot(x_vals, nist_vap_t, color='#84A1D6') #NIST VAP
plt.plot(x_vals, nist_liq_t, color='#E9AFA3') #NIST LIQ
plt.xlabel('Styrene Mole Fraction (Vapor/Liquid)') 
plt.ylabel('Temperature (°K)')
plt.title('Styrene-Ethylbenzene Binary System (NIST), P=0.1 bar') 
plt.legend(['Vapour','Liquid'])
plt.yticks(np.arange(np.round(min(nist_vap_t)),np.round(max(nist_vap_t))+1,1))
#plt.savefig('NIST.png')

#nrtl
plt.figure()
plt.plot(x_vals, nrtl_vap_t, color='#84A1D6') #NIST VAP
plt.plot(x_vals, nrtl_liq_t, color='#E9AFA3') #NIST LIQ
plt.xlabel('Styrene Mole Fraction (Vapor/Liquid)') 
plt.ylabel('Temperature (°K)')
plt.title('Styrene-Ethylbenzene Binary System (NRTL), P=0.1 bar') 
plt.legend(['Vapour','Liquid'])
plt.yticks(np.arange(np.round(min(nrtl_vap_t)),np.round(max(nrtl_vap_t))+1,1))
#plt.savefig('NRTL.png')
plt.show()
#compute relative error
error_vap = abs(((nist_vap_t - nrtl_vap_t)/(nist_vap_t))*100)
error_liq = abs(((nist_liq_t - nrtl_liq_t)/(nist_liq_t))*100)
max_error_vap = np.max(error_vap)
max_error_liq = np.max(error_liq)

#export to pandas
df = pd.DataFrame(
    {'xval': x_vals, 
    'NIST_VAP_T': nist_vap_t,
    'NIST_LIQ_T': nist_liq_t,
    'NRTL_VAP_T': nrtl_vap_t,
    'NRTL_LIQ_T': nrtl_liq_t,
    'Error Vapor': error_vap,
    'Error Liq': error_liq,
    'max error vapor': max_error_vap,
    'max_error liq': max_error_liq}
    ) 
#df.to_excel('validation.xlsx', index=False) 

