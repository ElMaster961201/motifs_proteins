class Parametros(object):

    p = [
    500, # tamPoblacion -> 0
    27, # k -> 1
    0.1, # proMutacion -> 2 
    2, # canMutacion -> 3
    1, # numElitismo -> 4
    3, # tamTorneo -> 5
    500, # numRestos -> 6
    .6, # proCruce -> 7
    [1/3, 1/3, 1/3], # w -> 8
    ['F', 'W', 'L', 'V', 'N', 'L','S','A','H','M','K','L','F','S','C','Q','P','E','E','G','I','A','Y','L','F','M','Q'] # secuencia  -> 9
    ]

    nGeneraciones = 500
    nRepeticiones = 10 
    

    def parametros(self):
        return self.p,self.nGeneraciones,self.nRepeticiones
    pass