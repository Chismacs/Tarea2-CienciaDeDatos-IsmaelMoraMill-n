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
    -----------------------------------------------
    Recibe:
    valoress: Lista con los números
        
    Retorna:
    mediana: Float con la mediana de los números (excluyendo NaNs)
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
    Calcula la moda de una lista 
    ----------------------------------
    Recibe:
    valoress: Lista de categotias
    
    Retorna:
    moda: str con la moda de la muestra
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
    Calcula el rango de una lista de números
    Detecta y elimina valores NaN
    ------------------------------------------
    Recibe:
    valores: Lista con los números
    
    Retorna:
    rango: Float con el rango de los números (excluyendo NaNs)
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
    Calcula la varianza de una lista de números
    Detecta y elimina valores NaN
    ----------------------------------------------
    Recibe:
    valores: Lista con los números
        
    Retorna:
    varianza: Float con la varianza de los números (excluyendo NaNs)
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
    Calcula la desviacion estandar de una lista de números
    Detecta y elimina valores NaN
    ---------------------------------------------------------
    Recibe:
    valoress: Lista con los números
        
    Retorna:
    desviacion estandar: Float con la desviacion estandar de los números (excluyendo NaNs)
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
    Calcula el percentil de una lista de números
    Detecta y elimina valores NaN
    -------------------------------------------------
    Recibe:
    valores: Lista con los números
    q: Int con el percentil que se desea 
    interpolacion: string con la cadena "lineal"
        
    Retorna
    percentil: Float con el percentil de los números (excluyendo NaNs)
    """
    
    #eliminamos los valores que sean NaNs
    valoresFinal=[]
    for v in valores:
        if math.isfinite(v):
            valoresFinal.append(v)

    # Ordenar la lista dada como input in-place
    valoresFinal.sort()

    if interpolacion=="lineal":
        #Distancia entre el primer y ultimo elemento
        distancia=len(valoresFinal)-1

        #calcular el indice efectivo del percentil
        indiceEfectivo=(distancia)*(q/100)
        
        #parte fraccional
        parteDecimalIndice=indiceEfectivo-int(indiceEfectivo)
        
        #indice inferior
        i=int(indiceEfectivo)
        j=min(i+1,len(valoresFinal)-1)

        #La interoplacion lineal se implementa con
        # val_inf + (val_sup)- val_inf)*fraction,
        percentiles=valoresFinal[i]+(valoresFinal[j]-valoresFinal[i])*parteDecimalIndice
        return percentiles
        
        percentiles=valoresFinal
    
def rangoIntercuartilico(valores):
    """
    Calcula el rango intercuartilico de una lista de números
    Detecta y elimina valores NaN
    -----------------------------------------------------------
    Recibe:
    valores: Lista con los números
        
    Retorna:
    rango intercuartilico: Float con el rango intercuartilico de los números (excluyendo NaNs)
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
    Calcula el MAD de una lista de números
    Detecta y elimina valores NaN
    ----------------------------------------
    Recibe:
    valores: Lista con los numeros
        
    Retorna:
    MAD: Float con el MAD de los numeros (excluyendo NaNs)
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
    Calcula la covarianza de una lista de números
    Detecta y elimina valores NaN
    -----------------------------------------------
    Recibe:
    valoresX: Lista con los números correspondientes a la coordenada x del par ordenado
    valoresY: Lista con los números correspondientes a la coordenada y del par ordenado
        
    Retorna:
    covarianza: Float con la covarianza de los números (excluyendo NaNs)
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
    Calcula la coeficiente de correlación de una lista de números
    Detecta y elimina valores NaN
    ---------------------------------------------------------------
    Recibe:
    valoresX: Lista con los números correspondientes a la coordenada x del par ordenado
    valoresY: Lista con los números correspondientes a la coordenada y del par ordenado
        
    Retorna:
    correlacion: Float con la correlacion de los números (excluyendo NaNs)
    """  
    #eliminamos los valores que sean NaNs
    x=[]
    y=[]
    
    for i in range(len(valoresX)):
        if math.isfinite(valoresX[i]) & math.isfinite(valoresY[i]): 
            x.append(valoresX[i])
            y.append(valoresY[i])

    rxy=covarianza(x,y)/(desviacionEstandar(x)*desviacionEstandar(y))
    return rxy
