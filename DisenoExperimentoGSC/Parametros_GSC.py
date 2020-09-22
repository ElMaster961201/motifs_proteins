class ParametrosGSC(object):

    p = [
    500, # tamPoblacion -> 0
    10, # numGenomas -> 1
    20, # numSecuenciasConservadas -> 2
    0.1, # proMutacion -> 3 
    2, # canMutacion -> 4
    1, # numElitismo -> 5
    4, # eunumero -> 6
    4, # tamTorneo -> 7
    500, # numRestos -> 8
    0.6, # proCruce -> 9
    ]

    n_generaciones = 1000
    n_repeticiones = 30

    def parametros(self):
        return self.p,self.n_generaciones,self.n_repeticiones
        