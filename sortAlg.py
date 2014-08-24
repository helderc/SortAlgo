#-------------------------------------------------------------------------------
# Name:        softAlog
# Purpose:
#
# Author:      Helder
#
# Created:     27/04/2012
# Copyright:   (c) Helder 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-
#!/usr/bin/python


import sys, os, time

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.uic import *
from datetime import *
from copy import *
import random

class Main(QMainWindow):

    listaOriginal = [] #<--- usar isso para deixar armazenado a lista embaralhada
    lista = [] # <---- Essa lista será a que vai receber os valores ordenados
    tI = None
    tF = None
    tl = 0

    # Janela principal
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        loadUi('janela.ui', self)

        # Tabela
        self.configTabela()

        #Sinais -> Slots
        self.connect(self.actionSair, SIGNAL('triggered()'), self, SLOT('sair()'))
        self.connect(self.btnGera, SIGNAL('clicked()'), self, SLOT('gerarNum()'))
        self.connect(self.btnOrdenar, SIGNAL('clicked()'), self, SLOT('ordenar()'))
        self.connect(self.btnLimpar, SIGNAL('clicked()'), self, SLOT('limparTempo()'))

    @pyqtSlot()
    def limparTempo(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tl = 0
        self.configTabela()

    @pyqtSlot()
    def sair(self):
        self.close()

    def configTabela(self):
        self.tableWidget.setHorizontalHeaderLabels(QString("Algoritmo;Qtd. de Valores;Tempo Gasto (s)").split(";"))
        self.tableWidget.horizontalHeader().setResizeMode(2, QHeaderView.Stretch)

    def addTabela(self, alg, qtd, temp):
        self.tableWidget.setRowCount(self.tl+1)
        self.tableWidget.setItem(self.tl, 0, QTableWidgetItem(alg))
        self.tableWidget.setItem(self.tl, 1, QTableWidgetItem(qtd))
        self.tableWidget.setItem(self.tl, 2, QTableWidgetItem(temp))
        self.tl = self.tl + 1
        self.tableWidget.repaint()


    # Marca o tempo de execucao do Algoritmo
    def tempo(self):
        if (self.tI == None):
            self.tI = datetime.now()
        else:
            self.tF = datetime.now()
            # dif: a diferenca de tempo entre o inicio e fim
            dif = self.tF - self.tI
            # limpa as variaveis de inicio e fim
            self.tI = None
            self.tF = None
            return str(dif.total_seconds())

    def msgStatus(self, msg):
        self.statusbar.showMessage(msg)
        self.statusbar.repaint()

    @pyqtSlot()
    def ordenar(self):
        # Backup da lista embaralhada
        self.listaOriginal = copy(self.lista)

        # BUBBLE SORT
        if ((self.rdbBubble.isChecked()) or (self.rdbTodos.isChecked())):
            self.msgStatus(">> Bubble Sort")
            # Marca o Tempo Inicial
            self.tempo()
            # Ordena
            self.lista = self.bubbleSort(copy(self.listaOriginal))
            # Mostra a lista Ordenada
            self.mostraOrdenado()
            # Calcula o tempo Final
            tGasto = self.tempo()
            # Mostra o tempo gasto
            self.addTabela("Bubble Sort", str(self.spbQtdValor.value()), tGasto)
            self.msgStatus("")

        # HEAP SORT
        if ((self.rdbHeap.isChecked()) or (self.rdbTodos.isChecked())):
            self.msgStatus(">> Heap Sort")
            # Marca o Tempo Inicial
            self.tempo()
            # Ordena
            self.lista = self.heapSort(copy(self.listaOriginal))
            # Mostra a lista Ordenada
            self.mostraOrdenado()
            # Calcula o tempo Final
            tGasto = self.tempo()
            # Mostra o tempo gasto
            self.addTabela("Heap Sort", str(self.spbQtdValor.value()), tGasto)
            self.msgStatus("")

        # INSERTION SORT
        if ((self.rdbInsertion.isChecked()) or (self.rdbTodos.isChecked())):
            self.msgStatus(">> Insertion Sort")
            # Marca o Tempo Inicial
            self.tempo()
            # Ordena
            self.lista = self.insertionSort(copy(self.listaOriginal))
            # Mostra a lista Ordenada
            self.mostraOrdenado()
            # Calcula o tempo Final
            tGasto = self.tempo()
            # Mostra o tempo gasto
            self.addTabela("Insertion Sort", str(self.spbQtdValor.value()), tGasto)
            self.msgStatus("")


        # MERGE SORT
        if ((self.rdbMerge.isChecked()) or (self.rdbTodos.isChecked())):
            self.msgStatus(">> Merge Sort")
            # Marca o Tempo Inicial
            self.tempo()
            # Ordena
            self.lista = self.mergeSort(copy(self.listaOriginal))
            # Mostra a lista Ordenada
            self.mostraOrdenado()
            # Calcula o tempo Final
            tGasto = self.tempo()
            # Mostra o tempo gasto
            self.addTabela("Merge Sort", str(self.spbQtdValor.value()), tGasto)
            self.msgStatus("")

        # QUICK SORT
        if ((self.rdbQuick.isChecked()) or (self.rdbTodos.isChecked())):
            self.msgStatus(">> Quick Sort")
            # Marca o Tempo Inicial
            self.tempo()
            # Ordena
            self.lista = self.qsort1(copy(self.listaOriginal))
            #self.lista = self.quickSort(copy(self.listaOriginal), 0, len(self.listaOriginal)-1)
            # Mostra a lista Ordenada
            self.mostraOrdenado()
            # Calcula o tempo Final
            tGasto = self.tempo()
            # Mostra o tempo gasto
            self.addTabela("Quick Sort", str(self.spbQtdValor.value()), tGasto)
            self.msgStatus("")
        
        # SELECTION SORT
        if ((self.rdbSelection.isChecked()) or (self.rdbTodos.isChecked())):
            self.msgStatus(">> Selection Sort")
            # Marca o Tempo Inicial
            self.tempo()
            # Ordena
            self.lista = self.selectionSort(copy(self.listaOriginal))
            # Mostra a lista Ordenada
            self.mostraOrdenado()
            # Calcula o tempo Final
            tGasto = self.tempo()
            # Mostra o tempo gasto
            self.addTabela("Selection Sort", str(self.spbQtdValor.value()), tGasto)
            self.msgStatus("")

        # SHELL SORT
        if ((self.rdbShell.isChecked()) or (self.rdbTodos.isChecked())):
            self.msgStatus(">> Shell Sort")
            # Marca o Tempo Inicial
            self.tempo()
            # Ordena
            self.lista = self.shellSort(copy(self.listaOriginal))
            # Mostra a lista Ordenada
            self.mostraOrdenado()
            # Calcula o tempo Final
            tGasto = self.tempo()
            # Mostra o tempo gasto
            self.addTabela("Shell Sort", str(self.spbQtdValor.value()), tGasto)
            self.msgStatus("")

    @pyqtSlot()
    def gerarNum(self):
        del self.lista[0:len(self.lista)]
        self.lstEmb.clear()

        for i in range(0, self.spbQtdValor.value()):
            self.lista.append(i)
        
        # Embaralha a lista
        #random.shuffle(self.lista)
        
        # Inverte a lista
        #self.lista.reverse()

        for i in range(0, self.spbQtdValor.value()):
            self.lstEmb.addItem(QString(str(self.lista[i])))


    def mostraOrdenado(self):
        # limpa a lista de ordenados
        self.lstOrd.clear()

        # coloca a Lista na tela
        for i in range(0, self.spbQtdValor.value()):
            self.lstOrd.addItem(QString(str(self.lista[i])))

    '''
    #######################################################
    # SHELL SORT - http://pt.wikipedia.org/wiki/Shell_sort
    #######################################################
    '''
    def shellSort (self, lst):
        n = len(lst)
        h = int(n / 2)
        while (h > 0):
            for i in range(h, n):
                c = lst[i]
                j = i
                while ((j >= h) and (c < lst[j - h])):
                    lst[j] = lst[j - h]
                    j = j - h
                    lst[j] = c
            h = int(h / 2.2)
        return (lst)

    '''
    #######################################################
    # SELECTION SORT - http://pt.wikipedia.org/wiki/Selection_sort
    #######################################################
    '''
    def selectionSort (self, lst):
        n = len(lst)
        for i in range(0, n-1):
            mini = i
            for j in range(i+1,n):
                if (lst[j] < lst[mini]):
                    mini = j
            lst[i], lst[mini] = lst[mini], lst[i]
        return lst


    '''
    ####################################################### 
    # QUICK SORT - http://c2.com/cgi/wiki?QuickSortInPython
    #######################################################
    '''
    
    def qsort1(self, L):
        if len(L) < 2: 
            return L
        
        pivot_element = random.choice(L)
        small = [i for i in L if i < pivot_element]
        medium = [i for i in L if i == pivot_element]
        large = [i for i in L if i > pivot_element]
        return self.qsort1(small) + medium + self.qsort1(large)


    '''
    #######################################################
    # MERGE SORT - http://pt.wikipedia.org/wiki/Merge_sort
    #######################################################
    '''
    def merge(self, left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result += left[i:]
        result += right[j:]
        return result


    def mergeSort(self, list):
        if len(list) < 2:
            return list
        middle = len(list) / 2
        left = self.mergeSort(list[:middle])
        right = self.mergeSort(list[middle:])
        return self.merge(left, right)


    '''
    #######################################################
    # INSERTION SORT - http://pt.wikipedia.org/wiki/Insertion_sort
    #######################################################
    '''
    def insertionSort(self, lst):
        for i in range(0, len(lst)-1):
            key = lst[i]
            j = i
            while ((j > 0) and (lst[j - 1] > key)):
                lst[j] = lst[j - 1]
                j -= 1
            lst[j] = key
        return lst

    '''
    #######################################################
    # HEAP SORT - http://pt.wikipedia.org/wiki/Heapsort
    #######################################################
    '''
    def heapSort(self, lst):
        for start in range((len(lst)-2)/2, -1, -1):
            self.siftdown(lst, start, len(lst)-1)

        for end in range(len(lst)-1, 0, -1):
            lst[end], lst[0] = lst[0], lst[end]
            self.siftdown(lst, 0, end - 1)
        return lst

    def siftdown(self, lst, start, end):
        root = start
        while True:
            child = root * 2 + 1
            if (child > end):
                break
            if ((child + 1 <= end) and (lst[child] < lst[child + 1])):
                child += 1
            if (lst[root] < lst[child]):
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break


    '''
    #######################################################
    # BUBBLE SORT - http://pt.wikipedia.org/wiki/Bubble_sort
    #######################################################
    '''
    def bubbleSort(self, lst):
		# verifica se ja esta ordenado
        flag = True
        while flag:
            flag = False
            for i in range(0, len(lst)-1):
                if (lst[i] > lst[i+1]):
                    lst[i], lst[i+1] = lst[i+1], lst[i]
                    flag = True
        return lst



if __name__ == '__main__':
    app = QApplication(sys.argv)
    sortAlg = Main()
    sortAlg.setWindowTitle('Sort')
    sortAlg.show()
    sys.exit(app.exec_())