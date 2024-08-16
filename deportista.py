class Deportista:
    def __init__(self, deporte, añosPracticando):
        if (deporte == None):
            self._deporte = "Futbol"
        else:
            self._deporte = deporte
        self._añosPracticando = añosPracticando

    def getDeporte(self):
        return self._deporte

    def setDeporte(self, deporte):
        self._deporte = deporte
    
    def getAñosPracticando(self):
        return self._añosPracticando

    def setAñosPractiando(self, añosPracticando):
        self._añosPracticando = añosPracticando