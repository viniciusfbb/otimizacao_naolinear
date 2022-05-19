#OTIMIZAÇÃO NÃO LINEAR - MÉTODOS DOS GRADIENTES
import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

sy.init_printing()

#Condições Iniciais
x = 1/3
y = 5/2

x1 = sy.Symbol('x1')
x2 = sy.Symbol('x2')
alfa = sy.Symbol('alfa')

funcao = ((x1 + 2*x2 - 7)**2 + (2*x1 + x2 - 5)**2)

resultado1 = 0
resultado2 = 0
controlex = 1
controley = 1
i = 0

while (abs(controlex) > 0.000001) or (abs(controlex) > 0.000001):
#while i < 5:

    print('\nINTERAÇÃO ',i+1," :")

    grad1 = sy.diff(funcao, x1)         #Gradiente da Função
    grad2 = sy.diff(funcao, x2)
    
    a = grad1.subs(x1, x)               #Valor de X no gradiente
    a2 = a.subs(x2, y)

    b = grad2.subs(x1, x)               #Valor de Y no gradiente
    b2 = b.subs(x2, y)
   
    y1 = (x - alfa*a2)                  #Expressão do alfa
    y2 = (y - alfa*b2)

    funcao1 = funcao.subs(x1, y1)       #Substituição de de y1 e y2 na função 
    funcao2 = funcao1.subs(x2, y2)
    
    d1 = sy.diff(funcao2, alfa)         #Derivada da função em relação a alfa

    raiz = (sy.solve(d1))               #Raiz da derivada da função
    raiz = raiz[0]
  
    resultado1 = y1.subs(alfa, raiz)    #Substitui o valor da raiz de alfa na expressão de alfa
    resultado2 = y2.subs(alfa, raiz)
    print('Ponto X1:',float((resultado1)),'\nPonto X2:',float(resultado2))
   
    controlex = resultado1 - x          #Calcula a variação dos valores dos pontos encontrados
    controley = resultado2 - y
    
    i= i + 1                            #Atualiza os valores de x e y
    x = resultado1
    y = resultado2

#Plot do Gráfico da Função
def f(x1, x2):  
    z = ((x1 + 2*x2 - 7)**2 + (2*x1 + x2 - 5)**2)   
    return z

x = np.linspace(-6, 6, 30)
y = np.linspace(-6, 6, 30)
X, Y = np.meshgrid(x, y)

Z = f(X, Y)

fig = plt.figure(figsize=(10, 10))

ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1,cmap='winter', edgecolor='none')
ax.set_title('Gráfico de superfície no Espaço 3D', fontsize=18);
ax.set_xlabel('Eixo X', fontsize=15)
ax.set_ylabel('Eixo Y', fontsize=15)
ax.set_zlabel('Eixo Z', fontsize=15)
ax.view_init(60, 45)

# Exibindo o gráfico criado
plt.show()