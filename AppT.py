
import yfinance as yf
import streamlit as st

st.write("""
# APP herramienta para obtener circuito equivalente **por unidad**

[Para más ejemplos ejemplos sobre el tema de por unidad puede hacer click aqui](http://web.mit.edu/6.061/www/notes3.pdf)


Esta herramienta le permite encontrar el circuito equivalente por unidad del sistema mostrado en la Figura 1.
Además, usted podra modificar los parámetros a su disposición del sistema por medio la barra lateral(izq). En la parte inferior
encontrara los resultados.

""")
L1 = add_selectbox = st.sidebar.number_input("Ingrese el valor de la reactancia de la linea 1 en ohms ej j2ohms -> ingrese 2 ", 1, 1000, 50)
L2 = add_selectbox = st.sidebar.number_input("Ingrese el valor de la reactancia de la linea 2 en ohms  ", 1, 1000, 25)
L3 = add_selectbox = st.sidebar.number_input("Ingrese el valor de la reactancia de la linea 3 en ohms  ", 1, 1000, 2)


SG1= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia del generador 1 en MVA ", 1, 10000, 1000)  # (#que se ingresa,comienza,termina, determindo)
VG1= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la tension del generador 1 en kV ", 1, 100, 18)
XG1= add_selectbox = 0.01*st.sidebar.number_input("Ingrese el valor de la reactancia del generador 1 en p.u. en porcentaje ej Xg1=6% -> ingrese 6 ", 1, 100, 20)

SG2= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia del generador 2 en MVA ", 1, 10000, 1000)
VG2= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la tension del generador 2 en kV ", 1, 100, 18)
XG2= add_selectbox = 0.01*st.sidebar.number_input("Ingrese el valor de la reactancia del generador 2 en p.u. ", 1, 100, 20)

SM3= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia del MOTOR  en MVA ", 1, 10000, 1500)
VM3= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la tension del MOTOR en kV ", 1, 100, 20)
XM3= add_selectbox = 0.01*st.sidebar.number_input("Ingrese el valor de la reactancia del MOTOR en p.u.", 1, 100, 20)

ST1= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia del Transformador 1 en MVA, Tenga en cuenta que por simetria de sistema T1a=T3a y T2b=T4b ", 1, 10000, 1000)
VT1a= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la relacion tension del Transformador 1 en kV, T1a-Ver Figura 1 ", 1, 1000, 500)
VT1b= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la relacion tension del Transformador 1 en kV, T1b-Ver Figura 1 ", 1, 1000, 20)
XT1= add_selectbox = 0.01*st.sidebar.number_input("Ingrese el valor de la reactancia del Transformador 1 en p.u.", 1, 100, 10)

ST2= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia del Transformador 2 en MVA ", 1, 10000, 1000)
VT2a= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la relacion tension del Transformador 2 en kV, T2a ", 1, 1000, 500)
VT2b= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la relacion tension del Transformacdor 2 en kV, T2b ", 1, 1000, 20)
XT2= add_selectbox = 0.01*st.sidebar.number_input("Ingrese el valor de la reactancia del Transformador 2 en p.u.", 1, 100, 10)

ST3= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia del Transformador 3 en MVA ", 1, 10000, 1000)
VT3a=VT1a
VT3b= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la relacion tension del Transformador 3 en kV, T2b ", 1, 1000, 20)
XT3= add_selectbox = 0.01*st.sidebar.number_input("Ingrese el valor de la reactancia del Transformador 3 en p.u.", 1, 100, 10)

ST4= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia del Transformador 4 en MVA ", 1, 10000, 1000)
VT4a= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la relacion tension del Transformador 4 en kV, T2a ", 1, 1000, 500)
VT4b=VT2b
XT4= add_selectbox = 0.01*st.sidebar.number_input("Ingrese el valor de la reactancia del Transformador 4 en p.u.", 1, 100, 10)

ST5= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia del Transformador 5 en MVA ", 1, 10000, 1500)
VT5a= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la relacion tension del Transformador 5 en kV, T2a ", 1, 1000, 500)
VT5b= add_selectbox = 1e3*st.sidebar.number_input("Ingrese la relacion tension del Transformador 5 en kV, T2b ", 1, 1000, 20)
XT5= add_selectbox = 0.01*st.sidebar.number_input("Ingrese el valor de la reactancia del Transformador 5 en p.u.", 1, 100, 10)

Sbase= add_selectbox = 1e6*st.sidebar.number_input("Ingrese la potencia de base del sistema ", 1, 10000, 100)
VbaseZ2=VT2a

st.header('Figura 1. Circuito a Desarrollar')
st.image("https://user-images.githubusercontent.com/65580822/95666491-c318b480-0b1f-11eb-95af-d7647d956df5.png", use_column_width=True)

#ZONA 2

ZT2pu=(((XT2*(VT2a**2))/(ST2))/((VbaseZ2**2)/(Sbase)))
st.write('La impedancia ZT2pu es:', ZT2pu)
st.write('La impedancia ZT2pu es:', ZT2pu) #Coloco el mismo ya que ZT2pu=ZT1pu

ZL1pu=L1/((VbaseZ2**2)/(Sbase))
st.write('La impedancia ZL1pu es:', ZL1pu)

#ZONA1

Vnew=(VT1a*VT2b)/VbaseZ2
ZG1pu=(((XG1*(VG1**2))/(SG1))/((Vnew**2)/(Sbase)))
st.write('La impedancia ZG1pu es:', ZG1pu)

#ZONA4

ZL2pu=L2/((VT4a**2)/(Sbase))
st.write('La impedancia ZL2pu es:', ZL2pu)

ZL3pu=L3/((VT4a**2)/(Sbase))
st.write('La impedancia ZL3pu es:', ZL3pu)


ZT4pu=(((XT4*(VT4a**2))/(ST4))/((VT4a**2)/(Sbase)))
st.write('La impedancia ZT2pu es:', ZT4pu)
st.write('La impedancia ZT4pu es:', ZT4pu) #Coloco el mismo ya que ZT2pu=ZT4pu

#ZONA3
ZG2pu=(((XG2*(VG2**2))/(SG2))/((VT2b**2)/(Sbase)))
st.write('La impedancia ZG2pu es:', ZG2pu)

#ZONA5

ZM3pu=(((XM3*(VT5b**2))/(SM3))/((VT5b**2)/(Sbase)))
st.write('La impedancia ZM3pu es:', ZM3pu)

ZT5pu=(((XT5*(VT5b**2))/(ST5))/((VT5b**2)/(Sbase)))
st.write('La impedancia ZT5pu es:', ZT5pu)

st.header('Figura 2. Circuito equivalente Desarrollado')
st.image("https://user-images.githubusercontent.com/65580822/95670408-f83cfb00-0b4f-11eb-88a9-faa0777de2ae.png", use_column_width=True)


st.write("""
# ¿Necesita ver la continuacion del ejercicio?¿Necesita otra app para su empresa?

[Para comprar esta App u otras ingrese aqui](https://www.experionglobal.com/?utm_source=Clutch&utm_medium=Clutch&utm_campaign=WebDev)

Desarrollado por estudiantes Ingeniería eléctrica: 
![alt text](https://user-images.githubusercontent.com/65580822/95415721-aea5a380-08f6-11eb-8746-dcf17c2e56d6.png)

Para mayor informacion puede comunicarse al email: _efsanchezr@unal.edu.co_
         
""")
st.video('https://www.youtube.com/watch?v=OqPAoS8dt4E&ab_channel=Facultaddeingenier%C3%ADa-UniversidadNacionaldeColombia')

