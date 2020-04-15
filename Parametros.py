class Parametros(object):

    p = [
    500, # tamPoblacion -> 0
    27, # k -> 1
    0.1, # proMutacion -> 2 
    2, # canMutacion -> 3
    1, # numElitismo -> 4
    4, # knumeros -> 5
    3, # tamTorneo -> 6
    500, # numRestos -> 7
    .6, # proCruce -> 8
    [1/3, 1/3, 1/3], # w -> 9
    ['F', 'W', 'L', 'V', 'N', 'L','S','A','H','M','K','L','F','S','C','Q','P','E','E','G','I','A','Y','L','F','M','Q'] # secuencia  -> 10
    ]

    nGeneraciones = 1000
    nRepeticiones = 30 
    

    def parametros(self):
        return self.p,self.nGeneraciones,self.nRepeticiones
    pass

"""
###### Experimento 01 ######
Torneo 
    Con poblacion 500
        
        Elitismo 1
            puntofijo.
            mutacion estandar.
            Remplazo de padres.

        Elitismo 50
            puntofijo.
            mutacion estandar.
            Remplazo de padres.

    
    Con poblacion 300
        
        Elitismo 1
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
        
        Elitismo 50
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
            
###### Experimento 02 ######
Ruleta 
    Con poblacion 500

        Elitismo 1
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
        
        Elitismo 50
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
    
    Con poblacion 300
        
        Elitismo 1
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
        
        Elitismo 50
            puntofijo.
            mutacion estandar.
            Remplazo de padres.

###### Experimento 03 ######
estocastico universal.
    Con poblacion 500

        Elitismo 1
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
        
        Elitismo 50
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
    
    Con poblacion 300
        
        Elitismo 1
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
        
        Elitismo 50
            puntofijo.
            mutacion estandar.
            Remplazo de padres.

###### Experimento 04 ######
restos 
    Con poblacion 500

        Elitismo 1
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
        
        Elitismo 50
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
    
    Con poblacion 300
        
        Elitismo 1
            puntofijo.
            mutacion estandar.
            Remplazo de padres.
        
        Elitismo 50
            puntofijo.
            mutacion estandar.
            Remplazo de padres.


"""