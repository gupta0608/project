# -*- coding: utf-8 -*-
"""
Created on Wed Feb 03 10:22:28 2016

@author: A.K.GUPTA
"""

"""
An industrialist needs to setup a water purification plat for his industrial
unit to treat the wastewater flow before discharging it into the water bodies
owing to ISO14000. 
We need to design a plant and establish the capital and running costs such 
that it fulfills his needs in the most economic way possible.
"""

class purification:
    #design parametres(fixed)
    Y=0.5
    "yield coefficient ie. mass of cells formed/mass of substrate utilized" 
    k=5.0 #1/day
    "maximum specific substrate utilization rate"
    Kd=0.06 #1/day
    "endogenous decay coefficient"
    Ks=100.0 #mg/l
    "saturation constant"
    f=0.675 
    "conversion factor for converting BOD5 to ultimate BOD"
    e=0.1
    "oxygen transfer effeciency"
    
    #adsjustable parameters
    X=2000.0 #mg/l
    "concentration of microbial mass"
    
    #user defined parametres
    So = 250.0 #mg/l
    "initial BOD5"
    Se = 10.0 #mg/l
    "final BOD5"
    Q = 500.0 #m3/hr
    "Wastewater flow rate"
    
    def variation(self):
        So=self.So
        Se=self.Se
        Q=self.Q
        
        Kd=0.06
        Y=0.5
        k=5.0
        Ks=100.0
        X=2000.0
        f=0.675
        e=0.1
        
        "Calculation of mean cell residence time (tc)"
        a=((Y*k*Se)/(Ks+Se))-Kd
        tc=1/a
        "Calculation of hydraulic retention time or period of aeration (t)"
        t=((tc*Y*(So-Se))/(X*(1+tc*Kd)))*24
        "Volume of aeration tank"
        V=Q*t 
        "Treatment effeciency"
        n=((So-Se)/So)*100
        "Observed Yield"
        Yobs=(Y/(1+tc*Kd))
        "Mass of sludge wasted each day"
        P= (Yobs*Q*(So-Se))/1000 #kg/day
        "Mass of oxygen required per day"
        m=((Q*(So-Se))/(f*1000))-1.42*P #kg/day
        "Volume of air required"
        Va=(m/(1.185*0.232*e)) #m3/day
        
               
        print "Voulme of aeration tank required=",V,"m3"
        print "Time required for aeration of 1 unit=",t,"hrs"
        print "Mass of sludge wasted eash day=",P,"kg/day"
        print "Mass of oxygen required=",m,"kg/day"
        print "Voulme of air required=",Va,"m3/day"
        print "Treatment effeciency=",n,"%"
        
        
        
        
        
        
        
        
    

        
        
        
        
        
        
        
        
        
        
        
        
        