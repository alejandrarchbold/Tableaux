# -*- coding: utf-8 -*-

# Implementación de los tableros semánticos (tableaux)
# Input: cadena de la formula en notacion inorder
# Output: lista de listas de literales

# Importando la libreria tableaux
import tableaux as T

# Fórmula (en notación polaca inversa)
# para obtener uno de sus tableaux

formula = "qpOq-p-YY"

# Se crea el tableau
ta = T.Tableaux(formula)

# Imprime el resultado en consola
if len(ta) == 0:
    print('La fórmula es insatisfacible')
else:
    print('La fórmula es satisfacible.')
    print('Las hojas abiertas del tableaux son:')
    for l in ta:
        print(T.imprime_hoja(l))


'''
t1 = T.par_complementario([T.Tree('1',None,None), T.Tree('2',None,None), T.Tree('-',None,T.Tree('3',None,None)), T.Tree('1',None,None)])
print(t1)

print('\n')

t2 = T.par_complementario([T.Tree('b',None,None), T.Tree('-',None,T.Tree('a',None,None)), T.Tree('-',None,T.Tree('c',None,None)), T.Tree('a',None,None), T.Tree('d',None,None)])
print(t2)

print('\n')

t3 = T.par_complementario([T.Tree('-',None,T.Tree('Z1',None,None)), T.Tree('S1',None,None), T.Tree('-',None,T.Tree('S10',None,None)), T.Tree('Z10',None,None)])
print(t3)

print('\n')

t4 = T.par_complementario([T.Tree('-',None,T.Tree('q',None,None)), T.Tree('-',None,T.Tree('p',None,None)), T.Tree('q',None,None), T.Tree('-',None,T.Tree('r',None,None))])
print(t4)

print('\n')


t5 = T.es_literal(T.Tree('-',None,T.Tree('p',None,None)))
print(t5)

print('\n')

t6 = T.es_literal(T.Tree('p',None,None))
print(t6)

print('\n')

t7 = T.es_literal(T.Tree('O',T.Tree('k',None,None),T.Tree('Y',T.Tree('i',None,None),T.Tree('j',None,None))))
print(t7)

print('\n')

t8 = T.es_literal(T.Tree('-',None,T.Tree('Y',T.Tree('p',None,None),T.Tree('q',None,None))))
print(t8)

print('\n')


t9 = T.no_literales([T.Tree('-',None,T.Tree('p',None,None)),T.Tree('p',None,None),T.Tree('-',None,T.Tree('q',None,None)),T.Tree('q',None,None)])
print(t9)

print('\n')

t10 = T.no_literales([T.Tree('p',None,None),T.Tree('q',None,None),T.Tree('O',T.Tree('p',None,None),T.Tree('q',None,None)),T.Tree('-',None,T.Tree('q',None,None)),T.Tree('-',None,T.Tree('p',None,None))])
print(t10)

print('\n')

t11 = T.no_literales([T.Tree('q',None,None),T.Tree('-',None,T.Tree('p',None,None)),T.Tree('-',None,T.Tree('-',None,T.Tree('p',None,None))),T.Tree('-',None,T.Tree('q',None,None))])
print(t11)

print('\n')

t12 = T.no_literales([T.Tree('-',None,T.Tree('p',None,None)),T.Tree('q',None,None),T.Tree('-',None,T.Tree('p',None,None)),T.Tree('r',None,None),T.Tree('-',None,T.Tree('q',None,None)),T.Tree('p',None,None)])
print(t12)

print('\n')


print("Clasificacion de formulas:")

print('\n')

c1 = T.clasificacion(T.Tree('-',None,T.Tree('>',T.Tree('-',None,T.Tree('1',None,None)),T.Tree('Y',T.Tree('-',None,T.Tree('3',None,None)),T.Tree('2',None,None)))))
print(c1)

print('\n')

c2 = T.clasificacion(T.Tree('-',None,T.Tree('-',None,T.Tree('-',None,T.Tree('O',T.Tree('p',None,None),T.Tree('q',None,None))))))
print(c2)

print('\n')

c3 = T.clasificacion(T.Tree('-',None,T.Tree('O',T.Tree('>',T.Tree('m',None,None),T.Tree('n',None,None)),T.Tree('-',None,T.Tree('l',None,None)))))
print(c3)

print('\n')

c4 = T.clasificacion(T.Tree('Y',T.Tree('>',T.Tree('x',None,None),T.Tree('z',None,None)),T.Tree('O',T.Tree('-',None,T.Tree('w',None,None)),T.Tree('-',None,T.Tree('y',None,None)))))
print(c4)

print('\n')

c5 = T.clasificacion(T.Tree('-',None,T.Tree('pq>',None,None)))
print(c5)

print('\n')

c6 = T.clasificacion(T.Tree('-',None,T.Tree('Y',T.Tree('-',None,T.Tree('a',None,None)),T.Tree('-',None,T.Tree('b',None,None)))))
print(c6)

print('\n')

c7 = T.clasificacion(T.Tree('>',T.Tree('Y',T.Tree('p',None,None),T.Tree('>',T.Tree('p',None,None),T.Tree('q',None,None))),T.Tree('q',None,None)))
print(c7)

print('\n')

c8 = T.clasificacion(T.Tree('O',T.Tree('-',None,T.Tree('s',None,None)),T.Tree('Y',T.Tree('t',None,None),T.Tree('>',T.Tree('u',None,None),T.Tree('v',None,None)))))
print(c8)

print('\n')


f1 = T.Inorder2Tree('(pYq)')

h1 = [f1, T.Inorder2Tree('-q')]

listaHojas1 = [h1]

T.imprime_listaHojas(T.clasifica_y_extiende(f1, h1))


print('\n')

f2 = T.Inorder2Tree('-(pO(rYs))')

h2 = [f2, T.Inorder2Tree('q'), T.Inorder2Tree('p')]

listaHojas2 = [h2]

T.imprime_listaHojas(T.clasifica_y_extiende(f2, h2))

print('\n')

f3 = T.Inorder2Tree('-(rYs)')

h3 = [f3, T.Inorder2Tree('-p')] 

listaHojas3 = [h3]

T.imprime_listaHojas(T.clasifica_y_extiende(f3, h3))

print('\n')

f4 = T.Inorder2Tree('-(-(r>s)Oq)')

h4 = [f4, T.Inorder2Tree('-p')]

listaHojas4 = [h4]

T.Inorder(T.clasifica_y_extiende(f4, h4))

'''

