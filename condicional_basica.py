# -*- coding: utf-8 -*-
"""condicional.basica

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13tESCt95f7dIpx7uhw4YYVS7IIxmCnYa
"""

salario = float(input("informe seu salario:"))

if salario <=3000:
  print("programador junior")

elif salario >3000 and salario <=6000:
        print("programador pleno")

elif salario >6000 and salario <=15000:
        print("programador senior")

else:
  print("gerentes de projetos")