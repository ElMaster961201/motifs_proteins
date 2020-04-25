class Parametros(object):

    p = [
    300, # tamPoblacion -> 0
    27, # k -> 1
    0.1, # proMutacion -> 2 
    2, # canMutacion -> 3
    50, # numElitismo -> 4
    4, # knumeros -> 5
    3, # tamTorneo -> 6
    500, # numRestos -> 7
    .6, # proCruce -> 8
    [1/3, 1/3, 1/3], # w -> 9
    ['F','W','L','V','N','L','S','A','H','M','K','L','F','S','C','Q','P','E','E','G','I','A','Y','L','F','M','Q'] # secuencia  -> 10
    ]

    nGeneraciones = 1000
    nRepeticiones = 30 
    

    def parametros(self):
        return self.p,self.nGeneraciones,self.nRepeticiones
        
    pass