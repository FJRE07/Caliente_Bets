

from bs4 import BeautifulSoup
import urllib,re
from lxml import etree
import pandas as pd
import numpy as np
from math import floor
from statistics import stdev,mean as sd,mean


def transform(data):
    datatrans=[]
    for item in data:
        auxiliar=[]
        for value in item:
            auxiliar.append(float(value))
        datatrans.append(auxiliar)
    return(datatrans)

def bet(bets):
    sim=100000
    n=np.random.random_sample(size = sim*3)  
    allnumbers=[]
    allpartialgains=[]
    for item in range(sim):
        randomnumbers=n[(item*3):((item+1)*3)]
        randomnumbers=list(randomnumbers/sum(randomnumbers))
        partialgains=[]
        for i in range(3):
            if bets[i]<0:
                partialgains.append(100*randomnumbers[i]/abs(bets[i])+randomnumbers[i])
            else: 
                partialgains.append(bets[i]*randomnumbers[i]/100 + randomnumbers[i])
        partialgains+=-sum(randomnumbers)
        allnumbers.append(randomnumbers)
        allpartialgains.append(partialgains)
        allnumbers[0]
        allpartialgains[0]
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