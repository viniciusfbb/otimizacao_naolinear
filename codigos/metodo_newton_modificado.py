#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DE NEWTON MODIFICADO   
import sympy as sy
import numpy as np
import math

def main(): 
  
    sy.init_printing()

    #Condições Iniciais
    x = 0.5
    y = 0.5
    e = 0

    x1 = sy.Symbol('x1')
    x2 = sy.Symbol('x2')
    alfa = sy.Symbol('alfa')

    funcao = 2*x1 - 1.05*x1**4 + x1**6/6 +  x1*x2 + x2**2

    resultado1 = 0
    resultado2 = 0
    controlex = 1
    controley = 1
    i = 0

    while (abs(controlex) > 0.000001) or (abs(controley) > 0.000001):
        
        i = i + 1
        print('\nINTERAÇÃO',i,":")

        grad1 = sy.diff(funcao, x1)         #Gradiente da Função
        grad2 = sy.diff(funcao, x2)
        
        a = grad1.subs(x1, x)               #Valor de X no gradiente
        a2 = a.subs(x2, y)

        b = grad2.subs(x1, x)               #Valor de Y no gradiente
        b2 = b.subs(x2, y)

        norma = math.sqrt(a2**2 + b2**2)    #Calcula e verifica se a norma é menor que o erro
        
        if norma <= e:
            print("Break")
            break

        h11 = sy.diff(grad1, x1)       #Calcula os elementos do hesiano
        h12 = sy.diff(grad1, x2)
        h21 = sy.diff(grad2, x1)
        h22 = sy.diff(grad2, x2)

        print(h11,'\n', h12,'\n', h21,'\n', h22,'\n') 
        
        #Passa as condições iniciais, elementos do hesiano e o gradiente no pontos iniciais para matrizes

        hessiana = sy.Matrix([[h11, h12],[h21, h22]]) 
        x0 = sy.Matrix([[x], [y]])

        print(hessiana)

        inv_hesiana = hessiana.inv()     #Inverte a matriz hessiana

        print('\n\n', inv_hesiana)

        print('\n\n', inv_hesiana * x0)

        break







main()