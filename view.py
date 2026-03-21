import flet as ft


class View(object):
    def __init__(self, page):
        self._page = page
        self._page.title = "TdP 2026 - Indovina il Numero"
        self._page.horizontal_alignment = 'CENTER'
        self._titolo = None
        self._controller = None
        self._lvOut = ft.ListView(expand=True)

    def carica_interfaccia(self):
        self._titolo = ft.Text("Indovina il numero",
                               color="blue", size=24)

        self._txt_n_max = ft.TextField(label="NumeroMassimo", disabled=True, width=200, value=self._controller.get_numero_massimo())
        self._txt_T_max = ft.TextField(label="Tentativi Max", disabled=True, width=200, value=self._controller.get_numero_massimo_tentativi())
        self._t_rimasti = ft.TextField(label="Tentativi rimanenti", disabled=True, width=200)
        self._txt_input = ft.TextField(label="Valore", disabled=True, width=200)
        self._btn_reset = ft.ElevatedButton(text="Nuova Partita", width=200, on_click=self._controller.reset)
        self._btn_gioca = ft.ElevatedButton(text="Indovina", width=200, on_click=self._controller.play, disabled=True)


        self.row1 = ft.Row(controls=[self._txt_n_max, self._btn_reset], alignment=ft.MainAxisAlignment.CENTER)
        self.row2 = ft.Row(controls=[self._t_rimasti, self._txt_T_max], alignment=ft.MainAxisAlignment.CENTER)
        self.row3 = ft.Row(controls=[self._txt_input, self._btn_gioca], alignment=ft.MainAxisAlignment.CENTER)

        self._sl = ft.Slider(label="Difficoltà",
                             min=50, max=500,
                             value=100, width=600, divisions=10, on_change=self._controller.setDifficulty, disabled=False)

        self._pb = ft.ProgressBar(width=600, color="amber")
        
        self._page.add(self.row1, self.row2, self.row3, self._sl, self._pb, self._lvOut)
        self._page.update()

    def setController(self, controller):
        self._controller = controller

    def update(self):
        self._page.update()


    @property
    def lvOut(self):
        return self._lvOut

    @property
    def txt_n_max(self):
        return self._txt_n_max

    @property
    def txt_T_max(self):
        return self._txt_T_max

    @property
    def t_rimasti(self):
        return self._t_rimasti

    @property
    def txt_input(self):
        return self._txt_input

    @property
    def btn_gioca(self):
        return self._btn_gioca

    @property
    def sl(self):
        return self._sl

    @property
    def pb(self):
        return self._pb








if __name__ == "__main__":
    v = View(ft.Page)
    