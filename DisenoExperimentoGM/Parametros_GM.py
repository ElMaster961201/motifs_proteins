class ParametrosGM(object):

    p = [
    300, # tamPoblacion -> 0
    30, # k -> 1
    0.1, # proMutacion -> 2 
    2, # canMutacion -> 3
    1, # numElitismo -> 4
    4, # knumeros -> 5
    3, # tamTorneo -> 6
    500, # numRestos -> 7
    .6, # proCruce -> 8
    [1/3, 1/3, 1/3], # w -> 9
    [] # secuencia  -> 10
    ]

    nGeneraciones = 1000
    nRepeticiones = 30 
    

    def parametros(self):
        return self.p,self.nGeneraciones,self.nRepeticiones
        
    pass