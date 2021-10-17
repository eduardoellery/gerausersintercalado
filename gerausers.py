#!/usr/bin/python3

def geraUsersTxt():
    arquivo = open("intercalado.txt", "w+")

    for x in range(1,11):
        arquivo.write("primeiro\r\n")
        arquivo.write("segundo\r\n")

    arquivo.close()

geraUsersTxt()