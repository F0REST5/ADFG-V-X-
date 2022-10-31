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
      text = text.replace("Ř","R")
      text = text.replace("Ě","E")
      text = text.replace("Š","S")
      text = text.replace("Ž","Z")
      text = text.replace("Ý","Y")
      text = text.replace("Á","A")
      text = text.replace("Č","C")
      text = text.replace("Í","I")
      text = text.replace("É","E")
      text = text.replace("Ť","T")
      text = text.replace("Ď","D")
      text = text.replace("Ň","N")
      text = text.replace("Ú","U")
      text = text.replace("Ů","U")
      text = text.replace("ř","r")
      text = text.replace("ě","e")
      text = text.replace("š","s")
      text = text.replace("ž","z")
      text = text.replace("ý","y")
      text = text.replace("á","a")
      text = text.replace("č","c")
      text = text.replace("í","i")
      text = text.replace("é","e")
      text = text.replace("q","q")
      text = text.replace("ť","t")
      text = text.replace("ď","d")
      text = text.replace("ň","n")
      text = text.replace("ú","u")
      text = text.replace("ů","u")
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
      
      kluc = kluc.replace("Ř","R")
      kluc = kluc.replace("Ě","E")
      kluc = kluc.replace("Š","S")
      kluc = kluc.replace("Ž","Z")
      kluc = kluc.replace("Ý","Y")
      kluc = kluc.replace("Á","A")
      kluc = kluc.replace("Č","C")
      kluc = kluc.replace("Í","I")
      kluc = kluc.replace("É","E")
      kluc = kluc.replace("Ť","T")
      kluc = kluc.replace("Ď","D")
      kluc = kluc.replace("Ň","N")
      kluc = kluc.replace("Ú","U")
      kluc = kluc.replace("Ů","U")
      kluc = kluc.replace("ř","r")
      kluc = kluc.replace("ě","e")
      kluc = kluc.replace("š","s")
      kluc = kluc.replace("ž","z")
      kluc = kluc.replace("ý","y")
      kluc = kluc.replace("á","a")
      kluc = kluc.replace("č","c")
      kluc = kluc.replace("í","i")
      kluc = kluc.replace("é","e")
      kluc = kluc.replace("q","q")
      kluc = kluc.replace("ť","t")
      kluc = kluc.replace("ď","d")
      kluc = kluc.replace("ň","n")
      kluc = kluc.replace("ú","u")
      kluc = kluc.replace("ů","u")
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
      textEN = textEN.replace("Ř","R")
      textEN = textEN.replace("Ě","E")
      textEN = textEN.replace("Š","S")
      textEN = textEN.replace("Ž","Z")
      textEN = textEN.replace("Ý","Y")
      textEN = textEN.replace("Á","A")
      textEN = textEN.replace("Č","C")
      textEN = textEN.replace("Í","I")
      textEN = textEN.replace("É","E")
      textEN = textEN.replace("Ť","T")
      textEN = textEN.replace("Ď","D")
      textEN = textEN.replace("Ň","N")
      textEN = textEN.replace("Ú","U")
      textEN = textEN.replace("Ů","U")
      textEN = textEN.replace("ř","r")
      textEN = textEN.replace("ě","e")
      textEN = textEN.replace("š","s")
      textEN = textEN.replace("ž","z")
      textEN = textEN.replace("ý","y")
      textEN = textEN.replace("á","a")
      textEN = textEN.replace("č","c")
      textEN = textEN.replace("í","i")
      textEN = textEN.replace("é","e")
      textEN = textEN.replace("q","q")
      textEN = textEN.replace("ť","t")
      textEN = textEN.replace("ď","d")
      textEN = textEN.replace("ň","n")
      textEN = textEN.replace("ú","u")
      textEN = textEN.replace("ů","u")
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
      
      kluc1 = kluc1.replace("Ř","R")
      kluc1 = kluc1.replace("Ě","E")
      kluc1 = kluc1.replace("Š","S")
      kluc1 = kluc1.replace("Ž","Z")
      kluc1 = kluc1.replace("Ý","Y")
      kluc1 = kluc1.replace("Á","A")
      kluc1 = kluc1.replace("Č","C")
      kluc1 = kluc1.replace("Í","I")
      kluc1 = kluc1.replace("É","E")
      kluc1 = kluc1.replace("Ť","T")
      kluc1 = kluc1.replace("Ď","D")
      kluc1 = kluc1.replace("Ň","N")
      kluc1 = kluc1.replace("Ú","U")
      kluc1 = kluc1.replace("Ů","U")
      kluc1 = kluc1.replace("ř","r")
      kluc1 = kluc1.replace("ě","e")
      kluc1 = kluc1.replace("š","s")
      kluc1 = kluc1.replace("ž","z")
      kluc1 = kluc1.replace("ý","y")
      kluc1 = kluc1.replace("á","a")
      kluc1 = kluc1.replace("č","c")
      kluc1 = kluc1.replace("í","i")
      kluc1 = kluc1.replace("é","e")
      kluc1 = kluc1.replace("q","q")
      kluc1 = kluc1.replace("ť","t")
      kluc1 = kluc1.replace("ď","d")
      kluc1 = kluc1.replace("ň","n")
      kluc1 = kluc1.replace("ú","u")
      kluc1 = kluc1.replace("ů","u")
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
      
      
      text1 = text1.replace("Ř","R")
      text1 = text1.replace("Ě","E")
      text1 = text1.replace("Š","S")
      text1 = text1.replace("Ž","Z")
      text1 = text1.replace("Ý","Y")
      text1 = text1.replace("Á","A")
      text1 = text1.replace("Č","C")
      text1 = text1.replace("Í","I")
      text1 = text1.replace("É","E")
      text1 = text1.replace("Ť","T")
      text1 = text1.replace("Ď","D")
      text1 = text1.replace("Ň","N")
      text1 = text1.replace("Ú","U")
      text1 = text1.replace("Ů","U")
      text1 = text1.replace("ř","r")
      text1 = text1.replace("ě","e")
      text1 = text1.replace("š","s")
      text1 = text1.replace("ž","z")
      text1 = text1.replace("ý","y")
      text1 = text1.replace("á","a")
      text1 = text1.replace("č","c")
      text1 = text1.replace("í","i")
      text1 = text1.replace("é","e")
      text1 = text1.replace("q","q")
      text1 = text1.replace("ť","t")
      text1 = text1.replace("ď","d")
      text1 = text1.replace("ň","n")
      text1 = text1.replace("ú","u")
      text1 = text1.replace("ů","u")
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
      
      kluc0 = kluc0.replace("Ř","R")
      kluc0 = kluc0.replace("Ě","E")
      kluc0 = kluc0.replace("Š","S")
      kluc0 = kluc0.replace("Ž","Z")
      kluc0 = kluc0.replace("Ý","Y")
      kluc0 = kluc0.replace("Á","A")
      kluc0 = kluc0.replace("Č","C")
      kluc0 = kluc0.replace("Í","I")
      kluc0 = kluc0.replace("É","E")
      kluc0 = kluc0.replace("Ť","T")
      kluc0 = kluc0.replace("Ď","D")
      kluc0 = kluc0.replace("Ň","N")
      kluc0 = kluc0.replace("Ú","U")
      kluc0 = kluc0.replace("Ů","U")
      kluc0 = kluc0.replace("ř","r")
      kluc0 = kluc0.replace("ě","e")
      kluc0 = kluc0.replace("š","s")
      kluc0 = kluc0.replace("ž","z")
      kluc0 = kluc0.replace("ý","y")
      kluc0 = kluc0.replace("á","a")
      kluc0 = kluc0.replace("č","c")
      kluc0 = kluc0.replace("í","i")
      kluc0 = kluc0.replace("é","e")
      kluc0 = kluc0.replace("q","q")
      kluc0 = kluc0.replace("ť","t")
      kluc0 = kluc0.replace("ď","d")
      kluc0 = kluc0.replace("ň","n")
      kluc0 = kluc0.replace("ú","u")
      kluc0 = kluc0.replace("ů","u")
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


    

 

    


    


   
        