class ParametrosGP(object):

    p = [
    300,                # tamPoblacion -> 0
    30,                 # numGenomas -> 1
    0.1,                # proMutacion -> 2 
    2,                  # canMutacion -> 3
    1,                  # numElitismo -> 4
    4,                  # knumeros -> 5
    4,                  # tamTorneo -> 6
    500,                # numRestos -> 7
    .6,                 # proCruce -> 8
    [1/3, 1/3, 1/3],    # w -> 9
    ['G', 'T', 'G', 'L', 'G', 'L', 'A', 'I', 'V', 'K', 'H', 'I', 'L', 'E', 'R', 'H', 'G', 'G', 'R', 'L', 'E', 'V', 'E', 'S', 'E', 'V', 'E', 'G', 'C', 'G']                  # secuenciaSintetica  -> 10
    ]

    nGeneraciones = 1000
    nRepeticiones = 30 
    

    def parametros(self):
        return self.p,self.nGeneraciones,self.nRepeticiones
        
    pass