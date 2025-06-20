import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.anno_selected = None

    def fillDDYear(self):
        anni = self._model.get_year_model()  # Recupera lista di anni, es. [2001, 2002, 2003]

        # Converte ciascun anno in una Option (occhio: map() da un iteratore, meglio usare list)
        listOfOptions = [
            ft.dropdown.Option(text=str(anno), data=anno)
            for anno in anni
        ]

        self._view._ddAnno.options = listOfOptions  # Assegna le opzioni al dropdown
        self._view._ddAnno.on_change = self.readDDValue  # Imposta il metodo da chiamare al cambio selezione
        self._view.update_page()

    def readDDValue(self, e):
        selected = e.control.value  # Prende il valore selezionato dal dropdown (es. "2003")
        try:
            self.anno_selected = int(selected)
            print(f"Hai selezionato l'anno: {anno_selected}")
            # Puoi ora salvare o usare questo valore per altre operazioni, es. analisi
            self._annoScelto = anno_selected
        except:
            print("Errore nella conversione dell'anno selezionato")



    def handleDDYearSelection(self, e):
        pass

    def handleCreaGrafo(self,e):
        if self.anno_selected is None:
            self._view.controls.clear()
            self._view.txt_result.controls.append(ft.Text("inserire prima un opzione nel dropdown", color="red"))
            self._view.update()
        self._model.build_graph(int(self.anno_selected))
        dettagli = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(dettagli))
        self._view.update_page()

    def handleCerca(self, e):
        valoresoglia = self._view._txtIntK.value
        if valoresoglia is None:
            self._view.txt_result.controls.append(ft.Text("scegli soglia"))
            self._view.update_page()
        try:
            soglia = int(valoresoglia)
        except ValueError:
            self._view.controls.clear()
            self._view.txt_result.controls.append(ft.Text("non è numero"))

        risultati = self._model.getDreamTeam(soglia)
        self._view.controls.clear()
        for r in risultati:
            self._view.txt_result.controls.append(ft.Text(r))
            self._view.update_page()

