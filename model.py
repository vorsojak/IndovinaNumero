import random as r


class Model(object):
    def __init__(self):
        self._n_max = 100
        self._t_max = 5
        self._segreto = None
        self._t_corrente = self._t_max

    def reset_gioco(self):
        self._segreto = r.randint(1, self._n_max)
        self._t_corrente = self._t_max
        print(self._segreto)

    def play(self, tentativo):
        self._t_corrente -= 1
        if tentativo == self._segreto:
            return 0
        if self._t_corrente == 0:
            return 2
        if tentativo > self._segreto:
            return 1
        return -1  # tentativo < self._segreto

    @property
    def get_n_max(self):
        return self._n_max

    @property
    def get_t_max(self):
        return self._t_max

    @property
    def get_t_rimanenti(self):
        return self._t_corrente


if __name__ == "__main__":
    m = Model()
    m.reset_gioco()
    print(m.play(12))
