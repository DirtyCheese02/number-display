s=int(input("""(Recomendado ingresar una escala entre 1 y 5)
Ingrese la escala: """))
loop = True
while loop is True:
    
    #--Imprime los numeros linea por linea--#
    def printing():
        for b_1 in range(0,len(A[0])):
            B = []
            for b_2 in range(0,len(A)):
                B.append(A[b_2][b_1])
            P_B = " "
            for b_3 in range(0,len(B)):
                P_B += ("".join(B[b_3]) + "  ")
            
            print(P_B)

    #--Opciones y Dibujo de numeros--#
    def op():
        if n == 0:
            D[int(len(D)/2)][1] = " "

        elif n == 1:
            for n1_0 in range(0,len(D)):
                D[n1_0][0] = " "
            for n1_1 in range(0,len(D),s+1):
                D[n1_1][1] = s*" "

        elif n == 2:
            for n2_0 in range(1,int(len(D)/2)):
                D[n2_0][0] = " "
            for n2_3 in range(int(len(D)/2),len(D)-1):
                D[n2_3][2] = " "

        elif n == 3:
            for n3_0 in range(0,len(D)):
                D[n3_0][0] = " "

        elif n == 4:
            for n4_0 in range(int(len(D)/2),len(D)-1):
                D[n4_0][0] = " "
            for n4_1 in range(0,len(D),len(D)-1):
                D[n4_1][1] = s*" "

        elif n == 5:
            for n5_0 in range(int(len(D)/2),len(D)-1):
                D[n5_0][0] = " "
            for n5_2 in range(1,int(len(D)/2)):
                D[n5_2][2] = " "

        elif n == 6:
            for n6_2 in range(1,int(len(D)/2)):
                D[n6_2][2] = " "

        elif n == 7:
            for n7_0 in range(0,len(D)):
                D[n7_0][0] = " "
            for n7_1 in range(int(len(D)/2),len(D),s+1):
                D[n7_1][1] = s*" "

        elif n == 9:
            for n9_0 in range(int(len(D)/2),len(D)-1):
                D[n9_0][0] = " "

        else:
            loop = False


    #--Codigo base--#
    k = str(input("""(Escriba "end" para salir del loop)
Ingrese cualquier numero: """))
    if k == "end":
        break
    A = []
    for n in k:
        n=int(n)
        D =   [[" ",s*"-"," "],
       ["|",s*" ","|"],
       [" ",s*"-"," "],
       ["|",s*" ","|"],
       [" ",s*"-"," "]]

        for i in range(1,s):
            D.insert(1,["|",s*" ","|"])
            D.insert(-1,["|",s*" ","|"])

        op()
        A.append(D)
    printing()