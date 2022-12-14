import random

import numpy as np

import functools 
import operator  

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtGui, uic

 
qtCreatorFile = "ADFG(V)X.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

symboly = "ABCDEFGHIJKLMNOPQRSTUVXYZ"

symboly1 =  "ABCDEFGHIJKLMNOPQRSTUWVXYZ0123456789"

symboly2 = "ABCDEFGHIKLMNOPQRSTUVWXYZ"


   


def ADFGVX_generator():
    rand = random.sample(symboly1 , 36)
    
    rand = functools.reduce(operator.add , (rand))
  
    return ''.join(rand)


def ADFGX_generator_CZ():
    rand = random.sample(symboly,25)
    
    rand = functools.reduce(operator.add , (rand))
  
    return ''.join(rand)

def ADFGX_generator_EN():
    rand = random.sample(symboly2,25)
    
    rand = functools.reduce(operator.add , (rand))
  
    return ''.join(rand)
                
def ADFGX_matrix_CZ(sym):
     

    matrix = []
    for char in sym:
        if char not in matrix and char in sym:
            matrix.append(char)       
    
    return matrix   

def ADFGX_matrix_EN(sym1):
     
    matrix = []
    for char in sym1:
        if char not in matrix and char in sym1:
            matrix.append(char)       
    
    return matrix                     

def ADFGVX_matrix(sym2):
    

    matrix = []
    for char in sym2:
        if char not in matrix and char in sym2:
            matrix.append(char)
    return matrix    
  

def SifrujADFGX_CZ(text,sym):
    
    matica = ADFGX_matrix_CZ(sym)
    indexy = 'ADFGX'
    sifra_text = ''
    cislo = ''
              
    for char in text.upper():
        row, col = divmod(matica.index(char), 5) 
        cislo += str(row) + str(col)
        
    for i in range(len(cislo)):
        znak = int(cislo[i])
        sifra_text += indexy[znak]
        
    return sifra_text


def SifrujADFGX_EN(textEN,sym1):
    matica = ADFGX_matrix_EN(sym1)
    indexy = 'ADFGX'
    sifra_text = ''
    cislo = ''
              
    for char in textEN.upper():
        row, col = divmod(matica.index(char), 5) 
        cislo += str(row) + str(col)
        
    for i in range(len(cislo)):
        znak = int(cislo[i])
        sifra_text += indexy[znak]
        
    return sifra_text




def SifrujADFGVX(text1,sym2):
    
    matica = ADFGVX_matrix(sym2)
    indexy = 'ADFGVX'
    sifra_text = ''
    cislo = ''
              
    for char in text1.upper():
        row, col = divmod(matica.index(char), 6) 
        cislo += str(row) + str(col)
        
    for i in range(len(cislo)):
        znak = int(cislo[i])
        sifra_text += indexy[znak] 
        
    return sifra_text    

def matrix_ADFGX_EN(kluc1,textEN,sym1):
    
    matrix = []
    
    rows = len(kluc1)
    sifra = SifrujADFGX_EN(textEN,sym1) 
    
    l = [list(sifra[i:i+rows]) for i in range(0,len(sifra), rows)]
    matrix = [s if len(s) == rows else s+[' ']*(rows-len(s)) for s in l]


    matrix = np.array(matrix)    
    
    return matrix 

def matrix_ADFGX_CZ(kluc,text,sym):
    
    matrix = []
    
    rows = len(kluc)
    
    sifra = SifrujADFGX_CZ(text,sym) 
    
    l = [list(sifra[i:i+rows]) for i in range(0,len(sifra), rows)]
    matrix = [s if len(s) == rows else s+[' ']*(rows-len(s)) for s in l]


    matrix = np.array(matrix)    
    
    return matrix   


def matrix_ADFGVX(kluc0,text1,sym2):
    
    matrix = []
    
    rows = len(kluc0)
    
    sifra = SifrujADFGVX(text1,sym2) 
    
    l = [list(sifra[i:i+rows]) for i in range(0, len(sifra), rows)]
    matrix = [s if len(s) == rows else s+[' ']*(rows-len(s)) for s in l]

    matrix = np.array(matrix)    
    
    return matrix
    
    
 
def transpoz_ADFGX_CZ(kluc,text,sym):
    
    matica = matrix_ADFGX_CZ(kluc,text,sym)

    stlpce = list(zip(*matica))
    stlpce_kluc = list(zip(kluc,stlpce))
    transpoz = sorted(stlpce_kluc)
    transpoz = np.array(transpoz)
    
    return transpoz


def transpoz_ADFGX_EN(kluc1,textEN,sym1):
    
    matica = matrix_ADFGX_EN(kluc1,textEN,sym1)

    stlpce = list(zip(*matica))
    stlpce_kluc = list(zip(kluc1,stlpce))
    transpoz = sorted(stlpce_kluc)
    transpoz = np.array(transpoz)
    
    return transpoz
    

def transpoz_ADFGVX(kluc0,text1,sym2):
    
    matica = matrix_ADFGVX(kluc0,text1,sym2)
    
    stlpce = list(zip(*matica))
    
    stlpce_kluc = list(zip(kluc0,stlpce))
    transpoz = sorted(stlpce_kluc)
    transpoz = np.array(transpoz)
    
    return transpoz


def des_matrix_ADFGX(text2,kluc2):
    
  length = len(text2) // len(kluc2)
  sifra = text2
  
  l = [list(sifra[i:i+length]) for i in range(0, len(sifra), length)]
  matrix = [s if len(s) == length else s+[' ']*(length-len(s)) for s in l]
  
  matrix = list(zip(*matrix))
  
  #matrix = np.array(matrix)

  matrix = functools.reduce(operator.add , (matrix))
  
  return ''.join(matrix)

  
  #return matrix

  

def des_matrix_ADFGVX(text4,kluc2):
    
  length = len(text4) // len(kluc2)
  sifra = text4
  
  l = [list(sifra[i:i+length]) for i in range(0, len(sifra), length)]
  matrix = [s if len(s) == length else s+[' ']*(length-len(s)) for s in l]
  
  matrix = list(zip(*matrix))
  
  #matrix = np.array(matrix)

  matrix = functools.reduce(operator.add , (matrix))
  
  return ''.join(matrix)

 
def Desifruj_ADFGX_CZ(text3,sym):
    
    matica = ADFGX_matrix_CZ(sym)
    indexy = 'ADFGX'
    cislo = ''
    text = ''
        
    
    for i in text3.upper():
        cislo += str(indexy.index(i))
        
    for i in range(len(cislo)//2):
        a = (1 + i) * 2
        x = int(cislo[a-2])
        y = int(cislo[a-1])
        
        ch = x * 5 + y
        
        text += matica[ch]
        
    return text

def Desifruj_ADFGX_EN(text6,sym1):
    
    matica = ADFGX_matrix_EN(sym1)
    indexy = 'ADFGX'
    cislo = ''
    text = ''
        
    
    for i in text6.upper():
        cislo += str(indexy.index(i))
        
    for i in range(len(cislo)//2):
        a = (1 + i) * 2
        x = int(cislo[a-2])
        y = int(cislo[a-1])
        
        ch = x * 5 + y
        
        text += matica[ch]
        
    return text
    
def Desifruj_ADFGVX(text5,sym2):
    
    matica = ADFGVX_matrix(sym2)
    indexy = 'ADFGVX'
    cislo = ''
    text = ''
        
    
    for i in text5.upper():
        cislo += str(indexy.index(i))
        
    for i in range(len(cislo)//2):
        a = (1 + i) * 2
        x = int(cislo[a-2])
        y = int(cislo[a-1])
        
        ch = x * 6 + y
        
        text += matica[ch]
        
    return text   
 
def spaces (sifra, length):
    return ' '.join(sifra[i:i+length] for i in range(0,len(sifra),length))



if __name__ == "__main__":

 class ADFGVX(QMainWindow, Ui_MainWindow):
     
      
     def generuj_ADFGX(self):
          if self.gen_CZ_Button.isChecked():
              self.ADFGX_generator.setText(str(ADFGX_generator_CZ()))
          else:
              self.ADFGX_generator.setText(str(ADFGX_generator_EN()))
          
     def generuj_ADFGVX(self):
          self.ADFGVX_generator.setText(str(ADFGVX_generator()))
          
     
     def sifrujADFGX_CZ(self):
      
  
      text = self.text_edit.text()
      kluc = self.kluc_edit.text()
      sym = self.abeceda_edit.text()
      
      text = text.replace("w","v")
      text = text.replace("W","V")
      text = text.replace("??","R")
      text = text.replace("??","E")
      text = text.replace("??","S")
      text = text.replace("??","Z")
      text = text.replace("??","Y")
      text = text.replace("??","A")
      text = text.replace("??","C")
      text = text.replace("??","I")
      text = text.replace("??","E")
      text = text.replace("??","T")
      text = text.replace("??","D")
      text = text.replace("??","N")
      text = text.replace("??","U")
      text = text.replace("??","U")
      text = text.replace("??","r")
      text = text.replace("??","e")
      text = text.replace("??","s")
      text = text.replace("??","z")
      text = text.replace("??","y")
      text = text.replace("??","a")
      text = text.replace("??","c")
      text = text.replace("??","i")
      text = text.replace("??","e")
      text = text.replace("q","q")
      text = text.replace("??","t")
      text = text.replace("??","d")
      text = text.replace("??","n")
      text = text.replace("??","u")
      text = text.replace("??","u")
      text = text.replace(" ","OO")
      text = text.replace("0","CDAT")
      text = text.replace("1","BGKL")
      text = text.replace("2","ASVF")
      text = text.replace("3","FCYO")   
      text = text.replace("4","TRLC")
      text = text.replace("5","JPWN")
      text = text.replace("6","KYZJ")
      text = text.replace("7","IDBP")
      text = text.replace("8","ZHLS")
      text = text.replace("9","NCTG")
      text = text.replace("!","")
      text = text.replace("?","")
      text = text.replace(".","")
      text = text.replace(":","")
      text = text.replace(",","")
      text = text.replace("#","")
      text = text.replace("$","")
      text = text.replace("&","")
      text = text.replace("@","")
      text = text.replace("(","")
      text = text.replace(")","")
      
      kluc = kluc.replace("??","R")
      kluc = kluc.replace("??","E")
      kluc = kluc.replace("??","S")
      kluc = kluc.replace("??","Z")
      kluc = kluc.replace("??","Y")
      kluc = kluc.replace("??","A")
      kluc = kluc.replace("??","C")
      kluc = kluc.replace("??","I")
      kluc = kluc.replace("??","E")
      kluc = kluc.replace("??","T")
      kluc = kluc.replace("??","D")
      kluc = kluc.replace("??","N")
      kluc = kluc.replace("??","U")
      kluc = kluc.replace("??","U")
      kluc = kluc.replace("??","r")
      kluc = kluc.replace("??","e")
      kluc = kluc.replace("??","s")
      kluc = kluc.replace("??","z")
      kluc = kluc.replace("??","y")
      kluc = kluc.replace("??","a")
      kluc = kluc.replace("??","c")
      kluc = kluc.replace("??","i")
      kluc = kluc.replace("??","e")
      kluc = kluc.replace("q","q")
      kluc = kluc.replace("??","t")
      kluc = kluc.replace("??","d")
      kluc = kluc.replace("??","n")
      kluc = kluc.replace("??","u")
      kluc = kluc.replace("??","u")
      kluc = kluc.replace(" ","OO")
      kluc = kluc.replace("?","")
      kluc = kluc.replace(".","")
      kluc = kluc.replace(":","")
      kluc = kluc.replace(",","")
      kluc = kluc.replace("#","")
      kluc = kluc.replace("$","")
      kluc = kluc.replace("&","")
      kluc = kluc.replace("@","")
      kluc = kluc.replace("(","")
      kluc = kluc.replace(")","")
      
      sifra = SifrujADFGX_CZ(text,sym)
      

      self.sifra_text.setText(str(spaces(sifra,2)))
      self.matrixBrowser.setText(str(matrix_ADFGX_CZ(kluc,text,sym)))
      self.sifra_text_2.setText(str(transpoz_ADFGX_CZ(kluc,text,sym)))
      
      
    
     def sifruj_ADFGX_EN(self):
         
      textEN = self.text_edit.text()
      kluc1 = self.kluc_edit.text()
      sym1 = self.abeceda_edit.text()
      
      textEN = textEN.replace("J","I")
      textEN = textEN.replace("j","i")
      textEN = textEN.replace("??","R")
      textEN = textEN.replace("??","E")
      textEN = textEN.replace("??","S")
      textEN = textEN.replace("??","Z")
      textEN = textEN.replace("??","Y")
      textEN = textEN.replace("??","A")
      textEN = textEN.replace("??","C")
      textEN = textEN.replace("??","I")
      textEN = textEN.replace("??","E")
      textEN = textEN.replace("??","T")
      textEN = textEN.replace("??","D")
      textEN = textEN.replace("??","N")
      textEN = textEN.replace("??","U")
      textEN = textEN.replace("??","U")
      textEN = textEN.replace("??","r")
      textEN = textEN.replace("??","e")
      textEN = textEN.replace("??","s")
      textEN = textEN.replace("??","z")
      textEN = textEN.replace("??","y")
      textEN = textEN.replace("??","a")
      textEN = textEN.replace("??","c")
      textEN = textEN.replace("??","i")
      textEN = textEN.replace("??","e")
      textEN = textEN.replace("q","q")
      textEN = textEN.replace("??","t")
      textEN = textEN.replace("??","d")
      textEN = textEN.replace("??","n")
      textEN = textEN.replace("??","u")
      textEN = textEN.replace("??","u")
      textEN = textEN.replace(" ","OO")
      textEN = textEN.replace("0","CDAT")
      textEN = textEN.replace("1","BGKL")
      textEN = textEN.replace("2","ASVF")
      textEN = textEN.replace("3","FCYO")   
      textEN = textEN.replace("4","TRLC")
      textEN = textEN.replace("5","JPWN")
      textEN = textEN.replace("6","KYZJ")
      textEN = textEN.replace("7","IDBP")
      textEN = textEN.replace("8","ZHLS")
      textEN = textEN.replace("9","NCTG")
      textEN = textEN.replace("!","")
      textEN = textEN.replace("?","")
      textEN = textEN.replace(".","")
      textEN = textEN.replace(":","")
      textEN = textEN.replace(",","")
      textEN = textEN.replace("#","")
      textEN = textEN.replace("$","")
      textEN = textEN.replace("&","")
      textEN = textEN.replace("@","")
      textEN = textEN.replace("(","")
      textEN = textEN.replace(")","")
      
      kluc1 = kluc1.replace("??","R")
      kluc1 = kluc1.replace("??","E")
      kluc1 = kluc1.replace("??","S")
      kluc1 = kluc1.replace("??","Z")
      kluc1 = kluc1.replace("??","Y")
      kluc1 = kluc1.replace("??","A")
      kluc1 = kluc1.replace("??","C")
      kluc1 = kluc1.replace("??","I")
      kluc1 = kluc1.replace("??","E")
      kluc1 = kluc1.replace("??","T")
      kluc1 = kluc1.replace("??","D")
      kluc1 = kluc1.replace("??","N")
      kluc1 = kluc1.replace("??","U")
      kluc1 = kluc1.replace("??","U")
      kluc1 = kluc1.replace("??","r")
      kluc1 = kluc1.replace("??","e")
      kluc1 = kluc1.replace("??","s")
      kluc1 = kluc1.replace("??","z")
      kluc1 = kluc1.replace("??","y")
      kluc1 = kluc1.replace("??","a")
      kluc1 = kluc1.replace("??","c")
      kluc1 = kluc1.replace("??","i")
      kluc1 = kluc1.replace("??","e")
      kluc1 = kluc1.replace("q","q")
      kluc1 = kluc1.replace("??","t")
      kluc1 = kluc1.replace("??","d")
      kluc1 = kluc1.replace("??","n")
      kluc1 = kluc1.replace("??","u")
      kluc1 = kluc1.replace("??","u")
      kluc1 = kluc1.replace(" ","OO")
      kluc1 = kluc1.replace("!","")
      kluc1 = kluc1.replace("?","")
      kluc1 = kluc1.replace(".","")
      kluc1 = kluc1.replace(":","")
      kluc1 = kluc1.replace(",","")
      kluc1 = kluc1.replace("#","")
      kluc1 = kluc1.replace("$","")
      kluc1 = kluc1.replace("&","")
      kluc1 = kluc1.replace("@","")
      kluc1 = kluc1.replace("(","")
      kluc1 = kluc1.replace(")","")
     
      sifra1 = SifrujADFGX_CZ(textEN,sym1)
      

      self.sifra_text.setText(str(spaces(sifra1,2)))
      self.matrixBrowser.setText(str(matrix_ADFGX_EN(kluc1,textEN,sym1)))
      self.sifra_text_2.setText(str(transpoz_ADFGX_EN(kluc1,textEN,sym1)))
      
      
     def sifruj_ADFGVX(self):
      text1 = self.text_edit.text()
      kluc0 = self.kluc_edit.text()
      sym2 = self.abeceda_edit.text()
      
      
      text1 = text1.replace("??","R")
      text1 = text1.replace("??","E")
      text1 = text1.replace("??","S")
      text1 = text1.replace("??","Z")
      text1 = text1.replace("??","Y")
      text1 = text1.replace("??","A")
      text1 = text1.replace("??","C")
      text1 = text1.replace("??","I")
      text1 = text1.replace("??","E")
      text1 = text1.replace("??","T")
      text1 = text1.replace("??","D")
      text1 = text1.replace("??","N")
      text1 = text1.replace("??","U")
      text1 = text1.replace("??","U")
      text1 = text1.replace("??","r")
      text1 = text1.replace("??","e")
      text1 = text1.replace("??","s")
      text1 = text1.replace("??","z")
      text1 = text1.replace("??","y")
      text1 = text1.replace("??","a")
      text1 = text1.replace("??","c")
      text1 = text1.replace("??","i")
      text1 = text1.replace("??","e")
      text1 = text1.replace("q","q")
      text1 = text1.replace("??","t")
      text1 = text1.replace("??","d")
      text1 = text1.replace("??","n")
      text1 = text1.replace("??","u")
      text1 = text1.replace("??","u")
      text1 = text1.replace(" ","OO")
      text1 = text1.replace("!","")
      text1 = text1.replace("?","")
      text1 = text1.replace(".","")
      text1 = text1.replace(":","")
      text1 = text1.replace(",","")
      text1 = text1.replace("#","")
      text1 = text1.replace("$","")
      text1 = text1.replace("&","")
      text1 = text1.replace("@","")
      text1 = text1.replace("(","")
      text1 = text1.replace(")","")
      
      kluc0 = kluc0.replace("??","R")
      kluc0 = kluc0.replace("??","E")
      kluc0 = kluc0.replace("??","S")
      kluc0 = kluc0.replace("??","Z")
      kluc0 = kluc0.replace("??","Y")
      kluc0 = kluc0.replace("??","A")
      kluc0 = kluc0.replace("??","C")
      kluc0 = kluc0.replace("??","I")
      kluc0 = kluc0.replace("??","E")
      kluc0 = kluc0.replace("??","T")
      kluc0 = kluc0.replace("??","D")
      kluc0 = kluc0.replace("??","N")
      kluc0 = kluc0.replace("??","U")
      kluc0 = kluc0.replace("??","U")
      kluc0 = kluc0.replace("??","r")
      kluc0 = kluc0.replace("??","e")
      kluc0 = kluc0.replace("??","s")
      kluc0 = kluc0.replace("??","z")
      kluc0 = kluc0.replace("??","y")
      kluc0 = kluc0.replace("??","a")
      kluc0 = kluc0.replace("??","c")
      kluc0 = kluc0.replace("??","i")
      kluc0 = kluc0.replace("??","e")
      kluc0 = kluc0.replace("q","q")
      kluc0 = kluc0.replace("??","t")
      kluc0 = kluc0.replace("??","d")
      kluc0 = kluc0.replace("??","n")
      kluc0 = kluc0.replace("??","u")
      kluc0 = kluc0.replace("??","u")
      kluc0 = kluc0.replace(" ","OO")
      kluc0 = kluc0.replace("!","")
      kluc0 = kluc0.replace("?","")
      kluc0 = kluc0.replace(".","")
      kluc0 = kluc0.replace(":","")
      kluc0 = kluc0.replace(",","")
      kluc0 = kluc0.replace("#","")
      kluc0 = kluc0.replace("$","")
      kluc0 = kluc0.replace("&","")
      kluc0 = kluc0.replace("@","")
      kluc0 = kluc0.replace("(","")
      kluc0 = kluc0.replace(")","")
     
        
      sifra2 = SifrujADFGVX(text1,sym2)
      

      self.sifra_text.setText(str(spaces(sifra2,2)))
      self.matrixBrowser.setText(str(matrix_ADFGVX(kluc0,text1,sym2)))
      self.sifra_text_2.setText(str(transpoz_ADFGVX(kluc0,text1,sym2)))
      
      
     def desifrujADFGVX(self):
      text4 = self.Sifra_edit.text()
      kluc2 = self.kluc2_edit.text()
      sym2 = self.abeceda2_edit.text()
      
      self.desif_text_transp.setText(str(des_matrix_ADFGVX(text4,kluc2)))
    
      text5 = des_matrix_ADFGVX(text4,kluc2)
      
      desif_text = Desifruj_ADFGVX(text5,sym2)
      desif_text = desif_text.replace("OO"," ")
      
      self.desif_text.setText(desif_text)

           
     def desifruj_ADFGX_CZ(self):
       text2 = self.Sifra_edit.text()
       kluc2 = self.kluc2_edit.text()
       sym = self.abeceda2_edit.text()
       
       self.desif_text_transp.setText(str(des_matrix_ADFGX(text2,kluc2)))
       
       transpoz = des_matrix_ADFGX(text2,kluc2)
    
       text3 = transpoz
       
       desif_text1 = Desifruj_ADFGX_CZ(text3,sym)
       desif_text1 = desif_text1.replace("OO"," ")
       
       self.desif_text.setText(str(desif_text1))
        
     def desifruj_ADFGX_EN(self):
       text2 = self.Sifra_edit.text()
       kluc2 = self.kluc2_edit.text()
       sym1 = self.abeceda2_edit.text()
       
       self.desif_text_transp.setText(str(des_matrix_ADFGX(text2,kluc2)))
       
       transpoz = des_matrix_ADFGX(text2,kluc2)
    
       text6 = transpoz
       
       desif_text2 = Desifruj_ADFGX_EN(text6,sym1)
       desif_text2 = desif_text2.replace("OO"," ")
       
       self.desif_text.setText(str(desif_text2)) 
         
        
     def vymaz(self):
        self.text_edit.clear()
        self.kluc_edit.clear()
        self.ADFGX_generator.clear()
        self.ADFGVX_generator.clear()
        self.abeceda_edit.clear()
        self.sifra_text.clear()
        self.matrixBrowser.clear()
        self.sifra_text_2.clear()
        self.Sifra_edit.clear()
        self.kluc2_edit.clear()
        self.abeceda2_edit.clear()
        self.desif_text_transp.clear()
        self.desif_text.clear() 
          
     def __init__(self):
         QMainWindow.__init__(self)
         Ui_MainWindow.__init__(self)
         self.setupUi(self)
         self.Generuj_ADFGX.clicked.connect(self.generuj_ADFGX)
         self.Generuj_ADFGVX.clicked.connect(self.generuj_ADFGVX)
         self.SifrujButton_2.clicked.connect(self.sifrujADFGX_CZ)
         self.SifrujButton_3.clicked.connect(self.sifruj_ADFGX_EN)
         self.SifrujButton.clicked.connect(self.sifruj_ADFGVX)
         self.DesifrujButton.clicked.connect(self.desifrujADFGVX)
         self.DesifrujADFGX_CZ.clicked.connect(self.desifruj_ADFGX_CZ)
         self.DesifrujButtonEN.clicked.connect(self.desifruj_ADFGX_EN)
         
         self.ClearButton.clicked.connect(self.vymaz)
         
   

if __name__ == "__main__":

         app = QApplication(sys.argv)
         window = ADFGVX()
         window.show()
         sys.exit(app.exec_())


    

 

    


    


   
        