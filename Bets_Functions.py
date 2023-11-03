import urllib,re
import pandas as pd
import numpy as np
from math import floor
from statistics import stdev,mean as sd,mean
from itertools import permutations
from time import ctime
import os

archivo = "Bets_Functions.py"
print("Último cambio en las funciones "+ str(ctime(os.path.getmtime(archivo))))

def transform(data):
    datatrans=[]
    for item in data:
        auxiliar=[]
        for value in item:
            auxiliar.append(float(value))
        datatrans.append(auxiliar)
    return(datatrans)

percentage_vector=[(x+1)/100 for x in range(100)]
percentage_bets=list(permutations(percentage_vector,3))
selected_percentage=[]

for element in percentage_bets:
    if sum(element)==1:
        selected_percentage.append(element)


def bet(bets):
    allnumbers=[]
    allpartialgains=[]
    for item in range(len(selected_percentage)):
        
        randomnumbers=selected_percentage[item]
        
        partialgains=[]
        for i in range(3):
            if bets[i]<0:
                partialgains.append(100*randomnumbers[i]/abs(bets[i])+randomnumbers[i])
            else: 
                partialgains.append(bets[i]*randomnumbers[i]/100 + randomnumbers[i])
        
        partialgains=np.array(partialgains)-sum(randomnumbers)
        allnumbers.append(randomnumbers)
        allpartialgains.append(partialgains)

    result={"Numbers":allnumbers,"Gains":allpartialgains}
    return(result)


def select(dicbet):
    selection=dicbet
    selection=pd.DataFrame(selection)
    selection=selection.where(selection<0,1,inplace=False)        
    selection=selection.where(selection>0,0,inplace=False)  
    auxiliar=[]
    for row in range(len(selection)):
        auxiliar.append(sum(selection.iloc[row]))
    pdauxiliar=pd.DataFrame(auxiliar)
    desired=pd.DataFrame(pdauxiliar[pdauxiliar>1])
    desired=desired.dropna()
    index=list(desired.index)
    return(index)

def addmaxmin(betlist,names):
    dfgains=[]
    for gain in betlist:
        item=list(gain)
        item.append(min(gain))
        item.append(max(gain))
        dfgains.append(item)
    dfgains=pd.DataFrame(dfgains)
    names.extend(["Min","Max"])
    dfgains.columns=names
    return(dfgains)

def minsort(pdfinal):
    aux=pdfinal.sort_values("Min",ascending=False)[0:]
    minimum=abs(aux["Min"])
    maximum=abs(aux["Max"])
    max_min=maximum-minimum
    aux["Max_Min"]=max_min
    aux=pd.DataFrame(aux.sort_values("Max_Min",ascending=False))
    return(aux)
    
def maxsort(pdfinal):
    aux=pdfinal.sort_values("Max",ascending=False)[0:]
    minimum=abs(aux["Min"])
    maximum=abs(aux["Max"])
    max_min=maximum-minimum
    aux["Max_Min"]=max_min
    aux=pd.DataFrame(aux.sort_values("Max_Min",ascending=False))
    return(aux)
    
    
def midpointsort(pdfinal):
    minimum=abs(pdfinal["Min"])
    maximum=abs(pdfinal["Max"])
    max_min=maximum-minimum
    pdfinal["Max_Min"]=max_min
    aux=pdfinal.sort_values("Max_Min",ascending=False)[0:]
    aux=pd.DataFrame(aux.sort_values("Max_Min",ascending=False))
    return(aux)

def absolute_value_selection(simulation):
    positive_numbers = [num for num in simulation if num > 0]
    negative_numbers=[num for num in simulation if num > 0]
    if len(positive_numbers)==2 and all(num > abs(negative_numbers[0]) for num in positive_numbers):
        print("Both positive numbers are greater than the absolute value of the negative number.")
        print(simulation)


def greater_than_abs_minimum(simulation):
    positive_numbers = [num for num in simulation if num > 0]
    negative_numbers=[num for num in simulation if num < 0]
    if any(num > abs(negative_numbers[0]) for num in positive_numbers):
        return(simulation)