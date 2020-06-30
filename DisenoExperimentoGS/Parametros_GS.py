class ParametrosGS(object):

    p = [
    300,                # tamPoblacion -> 0
    30,                 # numGenomas -> 1
    0.1,                # proMutacion -> 2 
    2,                  # canMutacion -> 3
    1,                  # numElitismo -> 4
    4,                  # eunumero -> 5
    4,                  # tamTorneo -> 6
    500,                # numRestos -> 7
    .6,                 # proCruce -> 8
    ['W', 'W', 'F', 'G', 'R', 'D', 'C', 'A', 'M', 'M', 'Y', 'A', 'F', 'K', 'M', 'Y', 'P', 'L', 'P', 'R', 'W', 'G', 'Y', 'L', 'N', 'I', 'Q', 'A', 'R', 'K']                  # secuenciaSintetica  -> 9
    ]

    nGeneraciones = 1000
    nRepeticiones = 30 
    

    def parametros(self):
        return self.p,self.nGeneraciones,self.nRepeticiones
        
    pass