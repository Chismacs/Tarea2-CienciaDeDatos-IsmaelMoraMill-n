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
    
    valores= []
    for v in lista:
        if math.isfinite(v):
            valores.append(v)
        
    promedio=sum(valores)/len(valores)
    return promedio





def mediana(valsIn):
    """
    Calcula la mediana de una lista de números
    Detecta y elimina valores NaN
    -----------------------------------------------
    Recibe:
    valsIn: Lista con los números
        
    Retorna:
    mediana: Float con la mediana de los números (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valores=[]
    for v in valsIn:
        if math.isfinite(v):
            vals.append(v)
    
    #ordenar la lista
    valores.sort()
    if len(valores)%2!=0:
        k=len(valores)//2
        mediana=valores[k]
    else:
        k=len(valores)//2
        mediana=(valores[k-1]+valores[k])/2
    return mediana




def moda(valores):
    """
    Calcula la moda de una lista 
    ----------------------------------
    Recibe:
    valores: Lista de categorias
    
    Retorna:
    moda: str con la moda de la muestra
    """
    #encontrar el conjunto de elementos unicos
    categorias=[]
    for v in valores:
        if v not in categorias:
            categorias.append(v)
    #obtener el numero de cuentas en la muestra
    #para cada una de las categorias
    cuentas=[]
    for c in categorias:
        n=0
        for val in valores:
            if val==c:
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
    moda=[]
    for i in range(len(cuentas)):
        if cuentas[i]==valoresMax:
            modas.append(categorias[i])
  
    #retorno la moda
    #moda= categorias[i_max]
    return moda



def rango(valsIn):
    """
    Calcula el rango de una lista de números
    Detecta y elimina valores NaN
    ------------------------------------------
    Recibe:
    valsIn: Lista con los números
    
    Retorna:
    rango: Float con el rango de los números (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valores=[]
    for v in valsIn:
        if math.isfinite(v):
            valores.append(v)

    return max(valores)-min(valores)


def varianza(valsIn):
    """
    Calcula la varianza de una lista de números
    Detecta y elimina valores NaN
    ----------------------------------------------
    Recibe:
    valsIn: Lista con los números
        
    Retorna:
    varianza: Float con la varianza de los números (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valores=[]
    for v in valsIn:
        if math.isfinite(v):
            valores.append(v)
            
    #estimar el promedio
    promVal=promedio(valores)
    
    #Estimamos las desviaciones cuadraticas medias
    dcm=[]
    for i in valores:
        dcm.append((v-promVal)**2)
    varianza=sum(dcm)/len(valores)
    
    return varianza


def desviacionEstandar(valsIn):
    """
    Calcula la desviacion estandar de una lista de números
    Detecta y elimina valores NaN
    ---------------------------------------------------------
    Recibe:
    valsIn: Lista con los números
        
    Retorna:
    desviacion estandar: Float con la desviacion estandar de los números (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valores=[]
    for v in valsIn:
        if math.isfinite(v):
            valores.append(v)
        #estimar el promedio
    promVal=promedio(valores)
    
    #Estimamos las desviaciones cuadraticas medias
    dcm=[]
    for i in vals:
        dcm.append((i-promVal)**2)
    varianza=sum(dcm)/len(valores)
    
    return varianza**(1/2)


def percentil(valsIn,q,interpolacion="lineal"):
    """
    Calcula el percentil de una lista de números
    Detecta y elimina valores NaN
    -------------------------------------------------
    Recibe:
    valsIn: Lista con los números
    q: Int con el percentil que se desea 
    interpolacion: string con la cadena "lineal"
        
    Retorna
    percentil: Float con el percentil de los números (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valores=[]
    for v in valsIn:
        if math.isfinite(v):
            valores.append(v)

    # Ordenar la lista dada como input in-place
    valores.sort()

    if interpolacion=="lineal":
        ieff=(len(valores)-1)*(q/100)
        i=int(ieff)
        j=min(i+1,len(valores)-1)
        fraccion=ieff-i
        #interpolacion lineal
        percentil=valores[i]+(valores[j]-valores[i])*fraccion

        return percentil
    
def rangoIntercuartilico(valsIn):
    """
    Calcula el rango intercuartilico de una lista de números
    Detecta y elimina valores NaN
    -----------------------------------------------------------
    Recibe:
    valsIn: Lista con los números
        
    Retorna:
    rango intercuartilico: Float con el rango intercuartilico de los números (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valores=[]
    for v in valsIn:
        if math.isfinite(v):
            valores.append(v)
    rangoIntercuartilico=percentil(valores,75)-percentil(valores,25)
    return rangoIntercuartilico
def mad(valsIn):
    """
    Calcula el MAD de una lista de números
    Detecta y elimina valores NaN
    ----------------------------------------
    Recibe:
    valsIn: Lista con los numeros
        
    Retorna:
    MAD: Float con el MAD de los numeros (excluyendo NaNs)
    """
    
    
    #eliminamos los valores que sean NaNs
    valores=[]
    for v in valsIn:
        if math.isfinite(v):
            valores.append(v)
    #calculamos la mediana de los datos orginales
    mediana1=mediana(valores)
    #creamos una lista vacia para ingresar cada dato restado con la mediana1 y su valor absoluto
    desviacionesMedias=[]
    for i in valores:
        desviacionesMedias.append(abs(i-mediana1))
    #por ultimo se calcula la mediana de la lista el cual sera el MAD
    mad=mediana(desviacionesMedias)
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
        if math.isfinite(valoresX[i]) and math.isfinite(valoresY[i]): 
            x.append(valoresX[i])
            y.append(valoresY[i])
  

    promedioX=promedio(x)
    promedioY=promedio(y)
    
    total=[]
    
    for xv,yv in zip(x,y):
        total.append( (xv-promedioX)*(yv-promedioY))
        
    covarianza=sum(total)/len(total)
    return covarianza
    
def correlacion(x, y):
    """
    Calcula la coeficiente de correlación de una lista de números
    Detecta y elimina valores NaN
    ---------------------------------------------------------------
    Recibe:
    x: Lista con los números correspondientes a la coordenada x del par ordenado
    y: Lista con los números correspondientes a la coordenada y del par ordenado
        
    Retorna:
    correlacion: Float con la correlacion de los números (excluyendo NaNs)
    """
    valoresX, valoresY = [], []
    for xi, yi in zip(x, y):
        if math.isfinite(xi) and math.isfinite(yi):
            valoresX.append(xi)
            valoresY.append(yi)
    
    covarianzaXY = covarianza(valoresX, valoresY)
    stdX = desviacion_estandar(valoresX)
    stdY = desviacion_estandar(valoresY)
    
    return covarianzaXY / (stdX * stdY)
