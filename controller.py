from math import log2

from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def get_numero_massimo(self):
        return self._model.get_n_max

    def get_numero_massimo_tentativi(self):
        return self._model.get_t_max

    def get_t_rimanenti(self):
        return self._model.get_t_rimanenti

    def reset(self, e):
        self._model.reset_gioco()
        self._view.sl.disabled = True
        self._view.t_rimasti.value = self._model.get_t_rimanenti
        self._view.lvOut.controls.clear()
        self._view.btn_gioca.disabled = False
        self._view.txt_input.disabled = False
        self._view.lvOut.controls.append(ft.Text("Indovina a quale numero sto pensando!"))
        self._view.pb.value = self._model.get_t_rimanenti / self._model.get_t_max
        self._view.txt_n_max.value = self._model.get_n_max
        self._view.update()

    def play(self, e):
        tentativoStr = self._view.txt_input.value
        self._view.txt_input.value = ""

        if tentativoStr == "":
            self._view.lvOut.controls.append(
                ft.Text("Attenzione! Inserisci un valore numerico da testare.", color="red")
                )
            self._view.update()

        try:
            tentativoInt = int(tentativoStr)
        except ValueError:
            self._view.lvOut.controls.append(
                ft.Text("Attenzione, valore inserito non è un intero.",
                        color="red")
            )
            self._view.update()
            return

        if tentativoInt < 0 or tentativoInt > self._model.get_n_max:
            self._view.lvOut.controls.append(
                ft.Text("Attenzione, valore inserito non è compreso tra 0 e "
                        f"{self._model.get_n_max}.",
                        color="red")
            )
            self._view.update()
            return

        self._view.t_rimasti.value = self._model.get_t_rimanenti - 1
        self._view.pb.value = (self._model.get_t_rimanenti - 1) / self._model.get_t_max

        res = self._model.play(tentativoInt)

        if res == 0:  # ho vinto
            self._view.lvOut.controls.append(
                ft.Text(f"Fantastico! hai vinto, il "
                        f"segreto era {tentativoInt}",
                        color="green"))
            self._view.btn_gioca.disabled = True
            self._view.txt_input.disabled = True
            self._view.sl.disabled = False
            self._view.update()
            return
        elif res == 2:  # ho finito tutte le vite
            self._view.lvOut.controls.append(
                ft.Text(f"Mi dispiace, hai finito le vite. "
                        f"Il segreto era: {self._model.get_segreto}", color="red")
            )
            self._view.btn_gioca.disabled = True
            self._view.txt_input.disabled = True
            self._view.sl.disabled = False
            self._view.update()
            return
        elif res == -1:  # il mio segreto è più piccolo
            self._view.lvOut.controls.append(
                ft.Text(f"Il segreto è più piccolo di {tentativoInt}.")
            )
            self._view.update()
        else:  # il segreto è più grande
            self._view.lvOut.controls.append(ft.Text(
                f"Il segreto è più grande di {tentativoInt}."
            ))
            self._view.update()


    def setDifficulty(self, e):
        self._model._n_max = int(self._view.sl.value)
        self._model._t_max = int(log2(self._model.get_n_max))
        self._view.txt_n_max.value = self._model.get_n_max
        self._view.txt_T_max.value = self._model.get_t_max
        self._view.t_rimasti.value = self._model.get_t_max
        self._view.update()
        print(self._model.get_n_max, "Nmax")
















