## Programa que excluir arquivos 

* #### *Contexto da aplicação:*

*Programa excluir arquivos selecionando pela extensão exemplo EXE, PNG, TXT entre outros*

* #### *Mapa do código:*

2. **Bibliotecas Python/ Comandos**

```Python
from PyQt5 import uic, QtWidgets #Para criar a interface GUI
import os #Para far os comandos ao windowns
import glob #Para Excluir arquivos especificos

#Caso não tenha as bibliotecas intale digitando no terminal
#A biblioteca OS já vem instalada por padrão no Python
pip install PyQt5
pip install glob

#Comando para transfomar o arquivo .py em .exe(executável)
pyinstaller --onefile w main.py
```

2. **Função que exclui os arquivos ao clicar no botão excluir na tela**
```Python
def exclui_arquivos():
    usr = interface_piloto.line_user.text() #Variavel que armazena o usuário digitado
    ext = interface_piloto.line_ext.text() # Variavel que armazena a extensão digitada
    py_files = glob.glob(f'C:/Users/{usr}/Downloads/*.{ext}')

    for py_file in py_files:
        try:
            os.remove(py_file)
        except OSError as e:
            print(f"Error:{ e.strerror}") 
```
3. **Função que sair do programa ao clicar no botão sair na tela**
```Python
def sair():
    interface_piloto.close()
```

4. **Inicia o programa**
```Python
app = QtWidgets.QApplication([])
interface_piloto = uic.loadUi("interface_piloto.ui")
interface_piloto.excluir_label.clicked.connect(exclui_arquivos) 
interface_piloto.excluir_tudo_label.clicked.connect(exclui_tudo)
interface_piloto.sair_label.clicked.connect(sair)
interface_piloto.show()
app.exec_()
```

5. **Codigo da interface da tela(QtDesigner)**
````Python
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>313</width>
    <height>202</height>
   </rect>
  </property>
  <property name="contextMenuPolicy">
   <enum>Qt::DefaultContextMenu</enum>
  </property>
  <property name="windowTitle">
   <string>Exclui Arquivos</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: #89e3d4</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>90</x>
     <y>0</y>
     <width>131</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Calibri</family>
     <pointsize>14</pointsize>
     <weight>75</weight>
     <bold>true</bold>
    </font>
   </property>
   <property name="text">
    <string>Exclui Arquivos</string>
   </property>
  </widget>
  <widget class="QToolButton" name="excluir_label">
   <property name="geometry">
    <rect>
     <x>20</x>
     <y>160</y>
     <width>75</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Calibri</family>
     <pointsize>10</pointsize>
     <weight>75</weight>
     <bold>true</bold>
     <underline>false</underline>
     <strikeout>false</strikeout>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="mouseTracking">
    <bool>true</bool>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color:#faf786;
border-radius:10px;
cursor:pointer;
color:black;
text-decoration:none;
border:2px solid black;
	</string>
   </property>
   <property name="text">
    <string>Excluir</string>
   </property>
   <property name="checkable">
    <bool>false</bool>
   </property>
  </widget>
  <widget class="QToolButton" name="excluir_tudo_label">
   <property name="geometry">
    <rect>
     <x>110</x>
     <y>160</y>
     <width>91</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Calibri</family>
     <pointsize>10</pointsize>
     <weight>75</weight>
     <bold>true</bold>
     <underline>false</underline>
     <strikeout>false</strikeout>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color:#faf786;
	border-radius:10px;
	border:1.5px solid black;
	cursor:pointer;
	color:black;
	text-decoration:none;</string>
   </property>
   <property name="text">
    <string>Excluir Tudo</string>
   </property>
  </widget>
  <widget class="QToolButton" name="sair_label">
   <property name="geometry">
    <rect>
     <x>220</x>
     <y>160</y>
     <width>75</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Calibri</family>
     <pointsize>10</pointsize>
     <weight>75</weight>
     <bold>true</bold>
     <underline>false</underline>
     <strikeout>false</strikeout>
    </font>
   </property>
   <property name="cursor">
    <cursorShape>PointingHandCursor</cursorShape>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color:#faf786;
	border-radius:10px;
	border:1.5px solid black;
	cursor:pointer;
	color:black;
	text-decoration:none;</string>
   </property>
   <property name="text">
    <string>Sair</string>
   </property>
  </widget>
  <widget class="QLineEdit" name="line_ext">
   <property name="geometry">
    <rect>
     <x>80</x>
     <y>100</y>
     <width>151</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Calibri</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color : rgb(255, 255, 255);
border-radius: 10px ;
border-style: outset;
border-width: 2px</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
   <property name="placeholderText">
    <string>Informe a Extensão</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_3">
   <property name="geometry">
    <rect>
     <x>40</x>
     <y>80</y>
     <width>51</width>
     <height>71</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>14796741191530273515-32.png</pixmap>
   </property>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>50</x>
     <y>50</y>
     <width>47</width>
     <height>31</height>
    </rect>
   </property>
   <property name="text">
    <string/>
   </property>
   <property name="pixmap">
    <pixmap>8924699331558965375-24.png</pixmap>
   </property>
  </widget>
  <widget class="QLineEdit" name="line_user">
   <property name="geometry">
    <rect>
     <x>80</x>
     <y>50</y>
     <width>151</width>
     <height>31</height>
    </rect>
   </property>
   <property name="font">
    <font>
     <family>Calibri</family>
     <pointsize>10</pointsize>
    </font>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color : rgb(255, 255, 255);
border-radius: 10px ;
border-style: outset;
border-width: 2px</string>
   </property>
   <property name="alignment">
    <set>Qt::AlignCenter</set>
   </property>
   <property name="placeholderText">
    <string>Informe a Extensão</string>
   </property>
  </widget>
  <zorder>label_3</zorder>
  <zorder>label_2</zorder>
  <zorder>label</zorder>
  <zorder>excluir_label</zorder>
  <zorder>excluir_tudo_label</zorder>
  <zorder>sair_label</zorder>
  <zorder>line_ext</zorder>
  <zorder>line_user</zorder>
 </widget>
 <resources/>
 <connections/>
</ui>

```