import math 
def promedio(lista):
    """
    Calcula el promedio de una lista.
    ----------------------------------
    Recibe:
    lista: Lista de variables aleatorias
    
    Retorna:
    promedio: Float con el promedio de la lista ingresada
    """
    
    valores=[]
    for i in lista:
        if math.isfinite(i):
            valores.append(i)
        
    promedio=sum(valores)/len(valores)
    return promedio

def mediana(valores):
    """
    Calcula la mediana de una lista de números
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    mediana:float
        la mediana de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valoresFinal=[]
    for i in valores:
        if math.isfinite(i):
            valoresFinal.append(i)
    
    #ordenar la lista
    valoresFinal.sort()
    if len(valoresFinal)%2!=0:
        k=len(valoresFinal)//2
        mediana=valoresFinal[k]
    else:
        k=len(valoresFinal)//2
        mediana=(valoresFinal[k-1]+valoresFinal[k])/2
    return mediana

def moda(valores):
    """
    calcula la moda de una lista conteniendo una
    variable categoriva nominal
    Parametros
    -----------
    vals: list
    lista de categotias
    Retorna
    -------
    moda: str
    la moda de la muestra
    """
    #encontrar el conjunto de elementos unicos
    categorias=[]
    for i in valores:
        if i not in categorias:
            categorias.append(i)
    #obtener el numero de cuentas en la muestra
    #para cada una de las categorias
    cuentas=[]
    for i in categorias:
        n=0
        for j in valores:
            if j==i:
                n=n+1
        cuentas.append(n)

    #guess and check
    iMax=0
    valoresMax=cuentas[0]
    for i in range(1,len(cuentas)):
        if cuentas[i]> valoresMax:  
            iMax=i
            valoresMax=cuentas[i]
    # determinar todas las categorias que tengan el numero
    # maximo de cuentas	
    modas=[]
    for i in range(len(cuentas)):
        if cuentas[i]==valoresMax:
            modas.append(categorias[i])
  
    #retorno la moda
    #moda= categorias[i_max]
    return modas

def rango(valores):
    """
    Calcula el rango de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    rango:float
        rango de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valoresFinal=[]
    for i in valores:
        if math.isfinite(i):
            valoresFinal.append(i)
    rango=max(valoresFinal)-min(valoresFinal)
    return rango

def varianza(valores):
    """
    Calcula la varianza de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    varianza:float
        varianza de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valoresFinal=[]
    for i in valores:
        if math.isfinite(i):
            valoresFinal.append(i)
            
    #estimar el promedio
    promedioEstimado=promedio(valoresFinal)
    
    #Estimamos las desviaciones cuadraticas medias
    desviacionCuadraticaMedia=[]
    for v in valoresFinal:
        desviacionCuadraticaMedia.append((i-promedioEstimado)**2)
    varianza=sum(desviacionCuadraticaMedia)/len(valoresFinal)    
    return varianza

def desviacionEstandar(valores):
    """
    Calcula la desviacion estandar de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    desviacion estandar:float
        desviacion estandar de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valoresFinal=[]
    for i in valores:
        if math.isfinite(i):
            valoresFinal.append(i)
        #estimar el promedio
    promedioEstimado=promedio(valoresFinal)
    
    #Estimamos las desviaciones cuadraticas medias
    desviacionCuadraticaMedia=[]
    for v in valoresFinal:
        desviacionCuadraticaMedia.append((i-promedioEstimado)**2)
    varianza=sum(desviacionCuadraticaMedia)/len(valoresFinal)
    desviacionEstandar=varianza**(1/2)
    return desviacionEstandar

def percentil(valores,q,interpolacion="lineal"):
    """
    Calcula el percentil de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    percentil:float
        percentil de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valoresFinal=[]
    for v in valores:
        if math.isfinite(v):
            valoresFinal.append(v)

    # Ordenar la lista dada como input in-place
    valoresFinal.sort()

    if interpolacion=="lineal":
        #Distancia entre el primer y ultimo elemtno,
        #a ki kargi del eje de indices
        distancia=len(valoresFinal)-1

        #calcular el indice efectio del percentil
        indiceEfectivo=distancia*q/100
        
        #parte fraccional
        parteDecimalIndice=indiceEfectivo-int(indiceEfectivo)
        
        #indice inferior
        i=int((indiceEfectivo)//1)
        j=i+1

        #La interoplacion lineal se implementa con
        # val_inf + (val_sup)- val_inf)*fraction,
        percentiles=valoresFinal[i]+valoresFinal[j]-valoresFinal[i]*parteDecimalIndice
        return percentiles
        
        percentiles=valoresFinal
    
def rangoIntercuartilico(valores):
    """
    Calcula el rango intercuartilico de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    rango intercuartilico:float
        rango intercuartilico de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valoresFinal=[]
    for i in valores:
        if math.isfinite(i):
            valoresFinal.append(i)
            
    rangoIntercuartilico=percentil(valores,75)-percentil(valores,25)
    return rangoIntercuartilico
    
def mad(valores):
    """
    Calcula el MAD de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    MAD:float
        MAD de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valoresFinal=[]
    for i in valores:
        if math.isfinite(i):
            valoresFinal.append(i)
    #calculamos la mediana de los datos orginales
    mediana1=mediana(valoresFinal)
    #creamos una lista vacia para ingresar cada dato restado con la mediana1 y su valor absoluto
    desviacionesMediana=[]
    for i in valoresFinal:
        desviacionesMediana.append(abs(i-mediana1))
    #por ultimo se calcula la mediana de la lista el cual sera el MAD
    mad=mediana(desviacionesMediana)
    return mad

def covarianza(valoresX,valoresY):
    """
    Calcula la covarianza de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    covarianza:float
        covarianza de los numeros (excluyendo NaNs)
    """
    
    
      #eliminamos los valores que sean NaNs
    x=[]
    y=[]
    
    for i in range(len(valoresX)):
        if math.isfinite(valoresX[i]) & math.isfinite(valoresY[i]): 
            x.append(valoresX[i])
            y.append(valoresY[i])
  

    promedioX=promedio(x)
    promedioY=promedio(y)
    
    total=[]
    
    for i,j in zip(x,y):
        total.append((i-promedioX)*(j-promedioY))
        
    covarianza=sum(total)/len(total)
    return covarianza

def correlacion(valoresX,valoresY):
    """
    Calcula la coeficiente de correlacion de una lista de numeros
    Detecta y elimina valores NaN
    
    Paràmetros
    ----------
    vals: lista
        lista con los numeros
        
    Retorna
    -------
    correlacion:float
        correlacion de los numeros (excluyendo NaNs)
    """  
    #eliminamos los valores que sean NaNs
    x=[]
    y=[]
    
    for i in range(len(valoresX)):
        if math.isfinite(valoresX[i]) & math.isfinite(valoresY[i]): 
            x.append(valoresX[i])
            y.append(valoresY[i])

    rxy=covarianza(x,y)/(varianza(x)*varianza(y))
    return rxy
