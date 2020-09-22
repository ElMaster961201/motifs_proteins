class ParametrosGM(object):

    p = [
    300, # tamPoblacion -> 0
    10, # numGenomas -> 1
    0.1, # proMutacion -> 2 
    2, # canMutacion -> 3
    1, # numElitismo -> 4
    4, # eunumero -> 5
    3, # tamTorneo -> 6
    500, # numRestos -> 7
    .6, # proCruce -> 8
    [2/10, 4/10, 4/10], # w -> 9
    ['G','T','G','L','G','L','A','I','V','K'] # secuencia  -> 10
    ]

    n_generaciones = 1000
    n_repeticiones = 30
    
    def parametros(self):
        return self.p,self.n_generaciones,self.n_repeticiones
        