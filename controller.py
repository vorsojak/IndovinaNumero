from view import View
from model import Model
import flet as ft


class Controller(object):
    def __init__(self, view: View):
        self._view = view
        self._model = Model()

    def get_numero_massimo(self):
        return self._model._n_max

    def get_numero_massimo_tentativi(self):
        return self._model._t_max

    def get_t_rimanenti(self):
        return self._model._t_corrente

    def reset(self):
        self._model.reset_gioco()
        self._view._t_rimasti.value = self._model._t_corrente
        self._view._lvOut.controls.clear()
        self._view._btn_gioca.disabled = False
        self._view._txt_input.disabled = False
        self._view._lvOut.controls.append(ft.Text("Indovina a quale numero sto pendando!"))
        self._view._pb.value = self._model._t_corrente / self._model._t_max
        self._view._txt_n_max.value = self._model._t_max
        self._view.update()

    def play(self, e):
        tentativoStr = self._view._txt_input.value
        self._view._txt_input.value = ""

        if tentativoStr == "":
            self._view._lvOut.controls.append(
                ft.Text("Attenzione! Inserisci un valore numerico da testate.", color="red")
                )
            self._view.update()

        try:
            tentativoInt = int(tentativoStr)
        except ValueError:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, valore inserito non è un intero.",
                        color="red")
            )
            self._view.update()
            return

        if tentativoInt < 0 or tentativoInt > self._model._n_max:
            self._view._lvOut.controls.append(
                ft.Text("Attenzione, valore inserito non è compreso tra 0 e "
                        f"{self._model._n_max}.",
                        color="red")
            )
            self._view.update()
            return

        self._view._t_rimasti.value = self._model._t_corrente - 1
        self._view._pb.value = (self._model._t_corrente - 1) / self._model._t_max

        res = self._model.play(tentativoInt)

        if res == 0:  # ho vinto
            self._view._lvOut.controls.append(
                ft.Text(f"Fantastico! hai vinto, il "
                        f"segreto era {tentativoInt}",
                        color="green"))
            self._view._btn_gioca.disabled = True
            self._view._txt_input.disabled = True
            self._view.update()
            return
        elif res == 2:  # ho finito tutte le vite
            self._view._lvOut.controls.append(
                ft.Text(f"Mi dispiace, hai finito le vite. "
                        f"Il segreto era: {self._model._segreto}")
            )
            self._view._btn_gioca.disabled = True
            self._view._txt_input.disabled = True
            self._view.update()
            return
        elif res == -1:  # il mio segreto è più piccolo
            self._view._lvOut.controls.append(
                ft.Text(f"Il segreto è più piccolo di {tentativoInt}.")
            )
            self._view.update()
        else:  # il segreto è più grande
            self._view._lvOut.controls.append(ft.Text(
                f"Il segreto è più grande di {tentativoInt}"
            ))
            self._view.update()
















