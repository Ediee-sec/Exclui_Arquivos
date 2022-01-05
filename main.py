from PyQt5 import uic, QtWidgets
import os
import glob


def exclui_arquivos():
    usr = interface_piloto.line_user.text()
    ext = interface_piloto.line_ext.text()
    py_files = glob.glob(f'C:/Users/{usr}/Downloads/*.{ext}')

    for py_file in py_files:
        try:
            os.remove(py_file)
        except OSError as e:
            print(f"Error:{ e.strerror}") 

def exclui_tudo():
    usr = interface_piloto.line_user.text()
    py_files = glob.glob(f'C:/Users/{usr}/Downloads/*.*')

    for py_file in py_files:
        try:
            os.remove(py_file)
        except OSError as e:
            print(f"Error:{ e.strerror}") 

def sair():
    interface_piloto.close()

app = QtWidgets.QApplication([])
interface_piloto = uic.loadUi("interface_piloto.ui")
interface_piloto.excluir_label.clicked.connect(exclui_arquivos)
interface_piloto.excluir_tudo_label.clicked.connect(exclui_tudo)
interface_piloto.sair_label.clicked.connect(sair)
interface_piloto.show()
app.exec_()

    