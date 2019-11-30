from tkinter import *
import tkinter as tk
import webbrowser

global equation
global equation2
         

expression = "" 

expression2 = ""

def cred(): 

    creditos = Tk() 

    creditos.configure(background="light green") 

    creditos.title("Créditos") 

  

    creditos.Cria = Label(creditos, text="Criadores: Marlon Vinicius Gonçalves, Mauricio Adams, Lucas Scheffer, Gabriel Rost, Eduardo Stein") 

    creditos.Cria["background"]="light green" 

    creditos.Cria["font"] = ("Arial", "15") 

    creditos.Cria["height"]=1 

    creditos.Cria["width"]=97 

    creditos.Cria.grid(row = 1, column = 0) 

  

    creditos.prof = Label(creditos, text="Orientadora:  Bruna De Souza Goldani") 

    creditos.prof["background"]="light green" 

    creditos.prof["font"] = ("Arial", "15") 

    creditos.prof["height"]=1 

    creditos.prof["width"]=97 

    creditos.prof.grid(row = 2, column = 0) 


    creditos.prof = Label(creditos, text="Coorientador:  Frederico Schardong") 

    creditos.prof["background"]="light green" 

    creditos.prof["font"] = ("Arial", "15") 

    creditos.prof["height"]=1 

    creditos.prof["width"]=97 

    creditos.prof.grid(row = 3, column = 0)
  

    creditos.ifrs = Label(creditos, text=" Instituto Federal do Rio Grande do Sul") 

    creditos.ifrs["background"]="light green" 

    creditos.ifrs["font"] = ("Arial", "15") 

    creditos.ifrs["height"]=1 

    creditos.ifrs["width"]=97 

    creditos.ifrs.grid(row = 4, column = 0)

    creditos.mainloop() 





if __name__ == "__main__":  

        base = Tk()

        base.configure(background="white")  

        base.title("Distribuição Eletrônica da Tabela Periódica")

        lado, cima = (base.winfo_screenwidth()), (base.winfo_screenheight())
        base.geometry('%dx%d+0+0' % (lado,cima))
        

        wid = lado / 300
        hei = wid / 2
        hei = int(hei)
        wid = int(wid)
        if lado == 1920 and cima == 1080:
            wid = wid + 3
            hei = hei + 1
            widl = wid
        elif lado == 1280 and cima == 1024:
            widl = wid + 2
        else:
            widl = wid
  
        equation = StringVar() 

        equation2 = StringVar()

        equation.set("") 

        equation2.set("") 


        def conta(cor, escolha, di, elem, nome):
            
            def cores(aa, spdf, jan):
                cor1s = cor2s = cor3s = cor4s = cor5s = cor6s = cor7s = cor2p = cor3p = cor4p = cor5p = cor6p = cor3d = cor4d = cor5d = cor6d = cor4f = cor5f = cor7p = "gray"
                for i in range(len(spdf)):
                    if spdf[i] == "1s":
                        cor1s = "blue2"
                    elif spdf[i] == "2s":
                        cor2s = "blue2"
                    elif spdf[i] == "3s":
                        cor3s = "blue2"
                    elif spdf[i] == "4s":
                        cor4s = "blue2"
                    elif spdf[i] == "5s":
                        cor5s = "blue2"
                    elif spdf[i] == "6s":
                        cor6s = "blue2"
                    elif spdf[i] == "7s":
                        cor7s = "blue2"
                    elif spdf[i] == "2p":
                        cor2p = "blue2"
                    elif spdf[i] == "3p":
                        cor3p = "blue2"
                    elif spdf[i] == "4p":
                        cor4p = "blue2"
                    elif spdf[i] == "5p":
                        cor5p = "blue2"
                    elif spdf[i] == "6p":
                        cor6p = "blue2"
                    elif spdf[i] == "3d":
                        cor3d = "blue2"
                    elif spdf[i] == "4d":
                        cor4d = "blue2"
                    elif spdf[i] == "5d":
                        cor5d = "blue2"
                    elif spdf[i] == "6d":
                        cor6d = "blue2"
                    elif spdf[i] == "4f":
                        cor4f = "blue2"
                    elif spdf[i] == "5f":
                        cor5f = "blue2"
                    elif spdf[i] == "7p":
                        cor7p = "blue2"

                return (cor1s, cor2s, cor3s, cor4s, cor5s, cor6s, cor7s, cor2p, cor3p, cor4p, cor5p, cor6p, cor3d, cor4d, cor5d, cor6d, cor4f, cor5f, cor7p)
                        

            numeroatomic = 0
            global final
            conf=[2,2,6,2,6,2,10,6,2,10,6,2,14,10,6,2,14,10,6]
            name=['1s','2s','2p','3s','3p','4s','3d','4p','5s','4d','5p','6s','4f','5d','6p','7s','5f','6d','7p']
            lim=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
            index = 0
            while escolha>0:
                while lim[index]<conf[index]:
                    lim[index]=lim[index]+1
                    escolha=escolha-1
                    if escolha<=0:
                        break
                index=index+1
            final=''
            aa = len(lim)
            spdf = []
                            
            for i in range(0,aa,1):
                    if lim[i]>0:
                            spdf.append(name[i])
                            numeroatomic = numeroatomic + lim[i]
                            if lim[i] == 1:
                                sla = "¹"
                            elif lim[i] == 2:
                                sla = "²"
                            elif lim[i] == 3:
                                sla = "³"
                            elif lim[i] == 4:
                                sla = "⁴"
                            elif lim[i] == 5:
                                sla = "⁵"
                            elif lim[i] == 6:
                                sla = "⁶"
                            elif lim[i] == 7:
                                sla = "⁷"
                            elif lim[i] == 8:
                                sla = "⁸"
                            elif lim[i] == 9:
                                sla = "⁹"
                            elif lim[i] == 10:
                                sla = "¹⁰"
                            elif lim[i] == 11:
                                sla = "¹¹"
                            elif lim[i] == 12:
                                sla = "¹²"
                            elif lim[i] == 13:
                                sla = "¹³"
                            elif lim[i] == 14:
                                sla = "¹⁴"
                            final=final+name[i]+str(sla)+' '
                    else:
                        break
            

            global expression
            jan = tk.Toplevel(base)
            cor1s, cor2s, cor3s, cor4s, cor5s, cor6s, cor7s, cor2p, cor3p, cor4p, cor5p, cor6p, cor3d, cor4d, cor5d, cor6d, cor4f, cor5f, cor7p = cores(aa, spdf, jan)


            expression = "" 

            equation.set("") 

            expression = expression + str(final) 

            equation.set(expression)

            distri = Entry(jan)
            distri.grid(row = 0, column = 1, columnspan=25, ipadx=240)
            distri.insert(END,str(expression))
            distri["font"] = ("Arial", "15")

            distrisimpli = Entry(jan)
            distrisimpli.grid(row = 1, column = 1, columnspan=25, ipadx=230)
            distrisimpli.insert(END,str(di))
            distrisimpli["font"] = ("Arial", "15")
            
            
            
            lb1 = Label(jan, text = "Distribuição extensa:")
            lb1["font"] = ("Arial", "15", "bold")
            lb1.grid(row = 0, column = 0)

            lb12 = Label(jan, text = "Distribuição simplificada:")
            lb12["font"] = ("Arial", "15", "bold")
            lb12.grid(row = 1, column = 0)


            numato = Label(jan, text = "Número atômico:")
            numato["font"] = ("Arial", "15", "bold")
            numato.grid(row = 2, column = 0)

            ato = Label(jan, text = numeroatomic, bg = cor, fg = "black", height = 1, width = 3)
            ato["font"] = ("Arial", "20")
            ato.grid(row = 2, column = 1)

            elemento = Label(jan, text = elem, bg = cor, fg = "black", height = 2, width = 4)
            elemento["font"] = ("Arial", "25")
            elemento.grid(row = 3, column = 0)

            nomeel = Label(jan, text = nome)
            nomeel["font"] = ("Arial", "25")
            nomeel.grid(row = 4, column = 0)

            s1 = Label(jan, text = "1s", fg = cor1s)
            s1["font"] = ("Arial", "15","bold")
            s1.grid(row = 4, column = 4)

            s2 = Label(jan, text = "2s", fg = cor2s)
            s2["font"] = ("Arial", "15","bold")
            s2.grid(row = 5, column = 4)

            s3 = Label(jan, text = "3s", fg = cor3s)
            s3["font"] = ("Arial", "15","bold")
            s3.grid(row = 6, column = 4)

            s4 = Label(jan, text = "4s", fg = cor4s)
            s4["font"] = ("Arial", "15","bold")
            s4.grid(row = 7, column = 4)

            s5 = Label(jan, text = "5s", fg = cor5s)
            s5["font"] = ("Arial", "15","bold")
            s5.grid(row = 8, column = 4)

            s6 = Label(jan, text = "6s", fg = cor6s)
            s6["font"] = ("Arial", "15","bold")
            s6.grid(row = 9, column = 4)

            s7 = Label(jan, text = "7s", fg = cor7s)
            s7["font"] = ("Arial", "15","bold")
            s7.grid(row = 10, column = 4)

            p2 = Label(jan, text = "2p", fg = cor2p)
            p2["font"] = ("Arial", "15","bold")
            p2.grid(row = 5, column = 6)

            p3 = Label(jan, text = "3p", fg = cor3p)
            p3["font"] = ("Arial", "15","bold")
            p3.grid(row = 6, column = 6)

            p4 = Label(jan, text = "4p", fg = cor4p)
            p4["font"] = ("Arial", "15","bold")
            p4.grid(row = 7, column = 6)

            p5 = Label(jan, text = "5p", fg = cor5p)
            p5["font"] = ("Arial", "15","bold")
            p5.grid(row = 8, column = 6)

            p6 = Label(jan, text = "6p", fg = cor6p)
            p6["font"] = ("Arial", "15","bold")
            p6.grid(row = 9, column = 6)

            d3 = Label(jan, text = "3d", fg = cor3d)
            d3["font"] = ("Arial", "15","bold")
            d3.grid(row = 6, column = 8)

            d4 = Label(jan, text = "4d", fg = cor4d)
            d4["font"] = ("Arial", "15","bold")
            d4.grid(row = 7, column = 8)

            d5 = Label(jan, text = "5d", fg = cor5d)
            d5["font"] = ("Arial", "15","bold")
            d5.grid(row = 8, column = 8)

            d6 = Label(jan, text = "6d", fg = cor6d)
            d6["font"] = ("Arial", "15","bold")
            d6.grid(row = 9, column = 8)

            f4 = Label(jan, text = "4f", fg = cor4f)
            f4["font"] = ("Arial", "15","bold")
            f4.grid(row = 7, column = 10)

            f5 = Label(jan, text = "5f", fg = cor5f)
            f5["font"] = ("Arial", "15","bold")
            f5.grid(row = 8, column = 10)

            p7 = Label(jan, text = "7p", fg = cor7p)
            p7["font"] = ("Arial", "15","bold")
            p7.grid(row = 10, column = 6)


            

            K = Label(jan, text = "K")
            K["font"] = ("Arial", "15","bold")
            K.grid(row = 4, column = 3)

            L = Label(jan, text = "L")
            L["font"] = ("Arial", "15","bold")
            L.grid(row = 5, column = 3)

            M = Label(jan, text = "M")
            M["font"] = ("Arial", "15","bold")
            M.grid(row = 6, column = 3)

            N = Label(jan, text = "N")
            N["font"] = ("Arial", "15","bold")
            N.grid(row = 7, column = 3)

            O = Label(jan, text = "O")
            O["font"] = ("Arial", "15","bold")
            O.grid(row = 8, column = 3)

            P = Label(jan, text = "P")
            P["font"] = ("Arial", "15","bold")
            P.grid(row = 9, column = 3)

            Q = Label(jan, text = "Q")
            Q["font"] = ("Arial", "15","bold")
            Q.grid(row = 10, column = 3)


            jan.mainloop()
        invisible = Label(base)
        invisible.grid(row = 20, column = 0)
            
        nmetais = Label(base, text = "Não metais", fg = "black", bg = "green yellow",height = 3, width = 20)
        nmetais.grid(row = 21, column = 0, columnspan = 10)

        mataisa = Label(base, text = "Metais Alcalinos", fg = "black", bg = "orange",height = 3, width = 22)
        mataisa.grid(row = 21, column = 3, columnspan = 10)

        semimet = Label(base, text = "SemiMetais", fg = "black", bg = "medium aquamarine",height = 3, width = 20)
        semimet.grid(row = 21, column = 6, columnspan = 10)

        outrosmet = Label(base, text = "Outros Metais", fg = "black", bg = "light sky blue",height = 3, width = 22)
        outrosmet.grid(row = 21, column = 9, columnspan = 10)

        lanta = Label(base, text = "Lantanideos", fg = "black", bg = "cyan",height = 3, width = 20)
        lanta.grid(row = 21, column = 15, columnspan = 10)

        gases = Label(base, text = "Gases Nobres", fg = "black", bg = "steel blue",height = 3, width = 20)
        gases.grid(row = 22, column = 0, columnspan = 10)

        metalte = Label(base, text = "Metais Alcalinos-Terrosos", fg = "black", bg = "yellow",height = 3, width = 22)
        metalte.grid(row = 22, column = 3, columnspan = 10)

        halo = Label(base, text = "Halogênios", fg = "black", bg = "cadet blue",height = 3, width = 20)
        halo.grid(row = 22, column = 6, columnspan = 10)

        metran = Label(base, text = "Metais de transição", fg = "black", bg = "orange red",height = 3, width = 22)
        metran.grid(row = 22, column = 9, columnspan = 10)

        acti = Label(base, text = "Actinidios", fg = "black", bg = "pink",height = 3, width = 20)
        acti.grid(row = 22, column = 15, columnspan = 10) 

        credito = Button(base, text = "Créditos", fg = "white", bg = "gray25", command=cred, height = hei, width = wid) 

        credito.grid(row = 0, column = 0)

        photo = PhotoImage(file = "ifrs.png")

        def link():
            webbrowser.open("https://ifrs.edu.br/rolante/", new = 0, autoraise=True)

        invisible2 = Label(base)
        invisible.grid(row = 10, column = 19)

        ifrsim = Button(base, image = photo, command=lambda: link())

        ifrsim.grid(row = 10, column = 20, columnspan = 200, rowspan = 200)

            
        H = Button(base, text = "H", fg = "black", bg = "green yellow",command=lambda:[conta("green yellow",1, "Não possui", "H", "Hidrogênio")], height=hei, width=wid) 

        H.grid(row = 1, column = 1) 

  

        Li = Button(base, text = "Li", fg = "black", bg = "orange",command=lambda: [conta("orange",3, "Não possui", "Li", "Lítio")], height=hei, width=wid) 

        Li.grid(row = 2, column = 1) 

  

        Na = Button(base, text = "Na", fg = "black", bg = "orange",command=lambda: [conta("orange",11, "[Ne] 3s¹", "Na", "Sódio")], height=hei, width=wid)   

        Na.grid(row = 3, column = 1) 

  

        K = Button(base, text = "K", fg = "black", bg = "orange",command=lambda: [conta("orange",19, "[Ar] 4s¹", "K", "Potássio")], height=hei, width=wid)   

        K.grid(row = 4, column = 1) 

  

        Rb = Button(base, text = "Rb", fg = "black", bg = "orange",command=lambda: [conta("orange",37, "[Kr]5s¹", "Rb", "Rubídio")], height=hei, width=wid)  

        Rb.grid(row = 5, column = 1) 

  

        Cs = Button(base, text = "Cs", fg = "black", bg = "orange",command=lambda: [conta("orange",55, "[Xe] 6s¹", "Cs", "Césio")], height=hei, width=wid)  

        Cs.grid(row = 6, column = 1) 

  

        Fr = Button(base, text = "Fr", fg = "black", bg = "orange",command=lambda: [conta("orange",87, "[Rn] 7s²", "Fr", "Frâncio")], height=hei, width=wid)  

        Fr.grid(row = 7, column = 1) 

  

        Be = Button(base, text = "Be", fg = "black", bg = "yellow",command=lambda:[conta("yellow",4, "Não possui", "Be", "Berílio")], height=hei, width=wid)  

        Be.grid(row = 2, column = 2) 

  

        Mg = Button(base, text = "Mg", fg = "black", bg = "yellow",command=lambda:[conta("yellow",12, "[Ne] 3s²", "Mg", "Magnésio")], height=hei, width=wid)  

        Mg.grid(row = 3, column = 2) 

  

        Ca = Button(base, text = "Ca", fg = "black", bg = "yellow",command=lambda:[conta("yellow",20, "[Ar] 4s²", "Ca", "Cálcio")], height=hei, width=wid)  

        Ca.grid(row = 4, column = 2) 

  

        Sr = Button(base, text = "Sr", fg = "black", bg = "yellow",command=lambda:[conta("yellow",38, "[Kr] 5s²", "Sr", "Estrôncio")], height=hei, width=wid) 

        Sr.grid(row = 5, column = 2) 

  

        Ba = Button(base, text = "Ba", fg = "black", bg = "yellow",command=lambda:[conta("yellow",56, "[Xe] 6s²", "Ba", "Bário")], height=hei, width=wid)  

        Ba.grid(row = 6, column = 2) 

  

        Ra = Button(base, text = "Ra", fg = "black", bg = "yellow",command=lambda:[conta("yellow",88, "[Rn] 7s²", "Ra", "Rádio")], height=hei, width=wid)  

        Ra.grid(row = 7, column = 2) 

  

        Sc = Button(base, text = "Sc", fg = "black", bg = "orange red",command=lambda:[conta("orange red",21, "[Ar] 3d¹ 4s²", "Sc", "Escândio")], height=hei, width=wid)  

        Sc.grid(row = 4, column = 3) 

  

        Y = Button(base, text = "Y", fg = "black", bg = "orange red",command=lambda:[conta("orange red",39, "[Kr] 4d¹ 5s²", "Y", "Ítrio")], height=hei, width=wid)  

        Y.grid(row = 5, column = 3) 

  

        La = Button(base, text = "La", fg = "black", bg = "cyan",command=lambda:[conta("cyan",57, "[Xe] 4f¹", "La", "Lantânio")], height=hei, width=wid) 

        La.grid(row = 10, column = 4) 

  

        Ac = Button(base, text = "Ac", fg = "black", bg = "pink",command=lambda:[conta("pink",89, "[Rn] 5f¹ 7s²", "Ac", "Actínio")], height=hei, width=wid) 

        Ac.grid(row = 11, column = 4) 

  

        Ti = Button(base, text = "Ti", fg = "black", bg = "orange red",command=lambda:[conta("orange red",22, "[Ar] 3d² 4s²", "Ti", "Titânio")], height=hei, width=wid) 

        Ti.grid(row = 4, column = 4) 

  

        Zr = Button(base, text = "Zr", fg = "black", bg = "orange red",command=lambda:[conta("orange red",40, "[Kr] 4d² 5s²", "Zr", "Zircônio")], height=hei, width=wid) 

        Zr.grid(row = 5, column = 4) 

  

        Hf = Button(base, text = "Hf", fg = "black", bg = "orange red",command=lambda:[conta("orange red",72, "[Xe] 4f¹⁴ 5d² 6s²", "Hf", "Háfnio")], height=hei, width=wid) 

        Hf.grid(row = 6, column = 4) 

  

        Rf = Button(base, text = "Rf", fg = "black", bg = "orange red",command=lambda:[conta("orange red",104, "Não possui", "Rf", "Rutherfórdio")], height=hei, width=wid) 

        Rf.grid(row = 7, column = 4) 

  

        Ce = Button(base, text = "Ce", fg = "black", bg = "cyan",command=lambda:[conta("cyan",58, "[Xe] 4f² 6s²", "Ce", "Cério")], height=hei, width=wid) 

        Ce.grid(row = 10, column = 5) 

  

        Th = Button(base, text = "Th", fg = "black", bg = "pink",command=lambda:[conta("pink",90, "[Rn] 5f² 7s²", "Th", "Tório")], height=hei, width=wid) 

        Th.grid(row = 11, column = 5) 

  

        V = Button(base, text = "V", fg = "black", bg = "orange red",command=lambda:[conta("orange red",23, "[Ar] 3d³ 4s²", "V", "Vanádio")], height=hei, width=wid) 

        V.grid(row = 4, column = 5) 

  

        Nb = Button(base, text = "Nb", fg = "black", bg = "orange red",command=lambda:[conta("orange red",41, "[Kr] 4d³ 5s²", "Nb", "Nióbio")], height=hei, width=wid) 

        Nb.grid(row = 5, column = 5) 

  

        ent1 = Label(base, text = "La - Lu ", fg = "black", bg = "cyan", height=hei, width=widl)  

        ent1.grid(row = 6, column = 3) 

  

        ent2 = Label(base, text = "Ac - Lr", fg = "black", bg = "pink", height=hei, width=widl)   

        ent2.grid(row = 7, column = 3) 

  

        Ta = Button(base, text = "Ta", fg = "black", bg = "orange red",command=lambda:[conta("orange red",73, "[Xe] 4¹⁴ 5d³ 6s²", "Ta", "Tântalo")], height=hei, width=wid) 

        Ta.grid(row = 6, column = 5) 

  

        Db = Button(base, text = "Db", fg = "black", bg = "orange red",command=lambda:[conta("orange red",105, "Não possui", "Db", "Dúbnio")], height=hei, width=wid) 

        Db.grid(row = 7, column = 5) 

  

        Pr = Button(base, text = "Pr", fg = "black", bg = "cyan",command=lambda:[conta("cyan",59, "[Xe] 4f³ 6s²", "Pr", "Praseodímio")], height=hei, width=wid) 

        Pr.grid(row = 10, column = 6) 

  

        Pa = Button(base, text = "Pa", fg = "black", bg = "pink",command=lambda:[conta("pink",91, "[Rn] 5f³ 7s²", "Pa", "Protactínio")], height=hei, width=wid) 

        Pa.grid(row = 11, column = 6) 

  

        Cr = Button(base, text = "Cr", fg = "black", bg = "orange red",command=lambda:[conta("orange red",24, "[Ar] 3d⁴ 4s²", "Cr", "Cromo")], height=hei, width=wid) 

        Cr.grid(row = 4, column = 6) 

  

        Mo = Button(base, text = "Mo", fg = "black", bg = "orange red",command=lambda:[conta("orange red",42, "[Kr] 4d⁴ 5s²", "Mo", "Molibdênio")], height=hei, width=wid) 

        Mo.grid(row = 5, column = 6) 

  

        W = Button(base, text = "W", fg = "black", bg = "orange red",command=lambda:[conta("orange red",74, "[Xe] 4f¹⁴ 5d⁴ 6s²", "W", "Tungstênio")], height=hei, width=wid) 

        W.grid(row = 6, column = 6) 

  

        Sg = Button(base, text = "Sg", fg = "black", bg = "orange red",command=lambda:[conta("orange red",106, "Não possui", "Sg", "Seabórgio")], height=hei, width=wid) 

        Sg.grid(row = 7, column = 6) 

  

        Nd = Button(base, text = "Nd", fg = "black", bg = "cyan",command=lambda:[conta("cyan",60, "[Xe] 4⁴ 6s²", "Nd", "Neodímio")], height=hei, width=wid) 

        Nd.grid(row = 10, column = 7) 

  

        U = Button(base, text = "U", fg = "black", bg = "pink",command=lambda:[conta("pink",92, "[Rn] 5f⁴ 7s²", "U", "Urânio")], height=hei, width=wid) 

        U.grid(row = 11, column = 7) 

  

        Mn = Button(base, text = "Mn", fg = "black", bg = "orange red",command=lambda:[conta("orange red",25, "[Ar] 3d⁵ 4s²", "Mn", "Manganês")], height=hei, width=wid) 

        Mn.grid(row = 4, column = 7) 

  

        Tc = Button(base, text = "Tc", fg = "black", bg = "orange red",command=lambda:[conta("orange red",43, "[Kr] 4d⁵ 5s²", "Tc", "Tecnécio")], height=hei, width=wid) 

        Tc.grid(row = 5, column = 7) 

  

        Re = Button(base, text = "Re", fg = "black", bg = "orange red",command=lambda:[conta("orange red",75, "[Xe] 4f¹⁴ 5d⁵ 6s²", "Re", "Rênio")], height=hei, width=wid) 

        Re.grid(row = 6, column = 7) 

  

        Bh = Button(base, text = "Bh", fg = "black", bg = "orange red",command=lambda:[conta("orange red",107, "Não possui", "Bh", "Bóhrio")], height=hei, width=wid) 

        Bh.grid(row = 7, column = 7) 

  

        Pm = Button(base, text = "Pm", fg = "black", bg = "cyan",command=lambda:[conta("cyan",61, "[Xe] 4f⁵ 6s²", "Pm", "Promécio")], height=hei, width=wid) 

        Pm.grid(row = 10, column = 8) 

  

        Np = Button(base, text = "Np", fg = "black", bg = "pink",command=lambda:[conta("pink",93, "[Rn] 5f⁵ 7s²", "Np", "Neptúnio")], height=hei, width=wid) 

        Np.grid(row = 11, column = 8) 

  

        Fe = Button(base, text = "Fe", fg = "black", bg = "orange red",command=lambda:[conta("orange red",26, "[Ar] 3d⁶ 4s²", "Fe", "Ferro")], height=hei, width=wid) 

        Fe.grid(row = 4, column = 8) 

  

        Ru = Button(base, text = "Ru", fg = "black", bg = "orange red",command=lambda:[conta("orange red",44, "[Kr] 4d⁶ 5s²", "Ru", "Rutênio")], height=hei, width=wid) 

        Ru.grid(row = 5, column = 8) 

  

        Os = Button(base, text = "Os", fg = "black", bg = "orange red",command=lambda:[conta("orange red",76, "[Xe] 4¹⁴ 5d⁶ 6s²", "Os", "Ósmio")], height=hei, width=wid) 

        Os.grid(row = 6, column = 8) 

  

        Hs = Button(base, text = "Hs", fg = "black", bg = "orange red",command=lambda:[conta("orange red",108, "Não possui", "Hs", "Hássio")], height=hei, width=wid) 

        Hs.grid(row = 7, column = 8) 

  

        Co = Button(base, text = "Co", fg = "black", bg = "orange red",command=lambda:[conta("orange red",27, "[Ar] 3d⁷ 4s² ", "Co", "Cobalto")], height=hei, width=wid) 

        Co.grid(row = 4, column = 9) 

  

        Rh = Button(base, text = "Rh", fg = "black", bg = "orange red",command=lambda:[conta("orange red",45, "[Kr] 4d⁷ 5s²", "Rh", "Ródio")], height=hei, width=wid) 

        Rh.grid(row = 5, column = 9) 

  

        Ir = Button(base, text = "Ir", fg = "black", bg = "orange red",command=lambda:[conta("orange red",77, "[Xe] 4f¹⁴ 5d⁷ 6s²", "Ir", "Irídio")], height=hei, width=wid) 

        Ir.grid(row = 6, column = 9) 

  

        Mt = Button(base, text = "Mt", fg = "black", bg = "orange red",command=lambda:[conta("orange red",109, "Não possui", "Mt", "Meitnério")], height=hei, width=wid)  

        Mt.grid(row = 7, column = 9) 

  

        Sm = Button(base, text = "Sm", fg = "black", bg = "cyan",command=lambda:[conta("cyan",62, "[Xe] 4f⁶ 6s²", "Sm", "Samário")], height=hei, width=wid) 

        Sm.grid(row = 10, column = 9) 

  

        Pu = Button(base, text = "Pu", fg = "black", bg = "pink",command=lambda:[conta("pink",94, "[Rn] 5f⁶ 7s² ", "Pu", "Plutônio")], height=hei, width=wid) 

        Pu.grid(row = 11, column = 9) 

  

        Ni = Button(base, text = "Ni", fg = "black", bg = "orange red",command=lambda:[conta("orange red",28, "[Ar] 3d⁸ 4s²", "Ni", "Níquel")], height=hei, width=wid) 

        Ni.grid(row = 4, column = 10) 

  

        Pd = Button(base, text = "Pd", fg = "black", bg = "orange red",command=lambda:[conta("orange red",46, "[Kr] 4d⁸ 5s²", "Pd", "Paládio")], height=hei, width=wid) 

        Pd.grid(row = 5, column = 10) 

  

        Pt = Button(base, text = "Pt", fg = "black", bg = "orange red",command=lambda:[conta("orange red",78, "[Xe] 4f¹⁴ 5d⁸ 6s²", "Pt", "Platina")], height=hei, width=wid) 

        Pt.grid(row = 6, column = 10) 

  

        Ds = Button(base, text = "Ds", fg = "black", bg = "orange red",command=lambda:[conta("orange red",110, "Não possui", "Ds", "Darmstádtio")], height=hei, width=wid) 

        Ds.grid(row = 7, column = 10) 

  

        Eu = Button(base, text = "Eu", fg = "black", bg = "cyan",command=lambda:[conta("cyan",63, "[Xe] 4f⁷ 6s²", "Eu", "Európio")], height=hei, width=wid) 

        Eu.grid(row = 10, column = 10) 

  

        Am = Button(base, text = "Am", fg = "black", bg = "pink",command=lambda:[conta("pink",95, "[Rn] 5f⁷ 7s²", "Am", "Amerício")], height=hei, width=wid) 

        Am.grid(row = 11, column = 10) 

  

        Cu = Button(base, text = "Cu", fg = "black", bg = "orange red",command=lambda:[conta("orange red",29, "[Ar] 3d⁹ 4s²", "Cu", "Cobre")], height=hei, width=wid) 

        Cu.grid(row = 4, column = 11) 

  

        Ag = Button(base, text = "Ag", fg = "black", bg = "orange red",command=lambda:[conta("orange red",47, "[Kr] 4d⁹ 5s²", "Ag", "Prata")], height=hei, width=wid) 

        Ag.grid(row = 5, column = 11) 

  

        Au = Button(base, text = "Au", fg = "black", bg = "orange red",command=lambda:[conta("orange red",79, "[Xe] 4f¹⁴ 5d⁹ 6s¹", "Au", "Ouro")], height=hei, width=wid) 

        Au.grid(row = 6, column = 11) 

  

        Rg = Button(base, text = "Rg", fg = "black", bg = "orange red",command=lambda:[conta("orange red",111, "Não possui", "Rg", "Roentgênio")], height=hei, width=wid) 

        Rg.grid(row = 7, column = 11) 

  

        Gd = Button(base, text = "Gd", fg = "black", bg = "cyan",command=lambda:[conta("cyan",64, "[Xe] 4f⁸ 6s²", "Gd", "Gatolínio")], height=hei, width=wid) 

        Gd.grid(row = 10, column = 11) 

  

        Cm = Button(base, text = "Cm", fg = "black", bg = "pink",command=lambda:[conta("pink",96, "[Rn] 5f⁸ 7s²", "Cm", "Cúrio")], height=hei, width=wid) 

        Cm.grid(row = 11, column = 11) 

  

        Zn = Button(base, text = "Zn", fg = "black", bg = "orange red",command=lambda:[conta("orange red",30, "[Ar] 3d¹⁰ 4s²", "Zn", "Zinco")], height=hei, width=wid) 

        Zn.grid(row = 4, column = 12) 

  

        Cd = Button(base, text = "Cd", fg = "black", bg = "orange red",command=lambda:[conta("orange red",48, "[Kr] 4d¹⁰ 5s²", "Cd", "Câdmio")], height=hei, width=wid) 

        Cd.grid(row = 5, column = 12) 

  

        Hg = Button(base, text = "Hg", fg = "black", bg = "orange red",command=lambda:[conta("orange red",80, "[Xe] 4f¹⁴", "Hg", "Mercúrio")], height=hei, width=wid) 

        Hg.grid(row = 6, column = 12) 

  

        Cn = Button(base, text = "Cn", fg = "black", bg = "orange red",command=lambda:[conta("orange red",112, "Não possui", "Cn", "Copernício")], height=hei, width=wid) 

        Cn.grid(row = 7, column = 12) 

  

        Tb = Button(base, text = "Tb", fg = "black", bg = "cyan",command=lambda:[conta("cyan",65, "[Xe] 4f⁹ 6s²", "Tb", "Térbio")], height=hei, width=wid) 

        Tb.grid(row = 10, column = 12) 

  

        Bk = Button(base, text = "Bk", fg = "black", bg = "pink",command=lambda:[conta("pink",97, "[Rn] 5f⁹ 7s²", "Bk", "Berquélio")], height=hei, width=wid) 

        Bk.grid(row = 11, column = 12) 

  

        B = Button(base, text = "B", fg = "black", bg = "medium aquamarine",command=lambda:[conta("medium aquamarine",5, "Não possui", "B", "Boro")], height=hei, width=wid) 

        B.grid(row = 2, column = 13) 

  

        Al = Button(base, text = "Al", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",13, "[Ne] 3s² 3p¹", "Al", "Alumínio")], height=hei, width=wid) 

        Al.grid(row = 3, column = 13) 

  

        Ga = Button(base, text = "Ga", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",31, "[Ar] 3d¹⁰ 4s² 4p¹", "Ga", "Gálio")], height=hei, width=wid) 

        Ga.grid(row = 4, column = 13) 

  

        In = Button(base, text = "In", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",49, "[Kr] 4d¹⁰ 5s² 5p¹", "In", "ìndio")], height=hei, width=wid) 

        In.grid(row = 5, column = 13) 

  

        Ti = Button(base, text = "Ti", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",81, "[Ar] 3d² 4s²", "Ti", "Tálio")], height=hei, width=wid) 

        Ti.grid(row = 6, column = 13) 

  

        Nh = Button(base, text = "Nh", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",113, "Não possui", "Nh", "Nihonio")], height=hei, width=wid) 

        Nh.grid(row = 7, column = 13) 

  

        C = Button(base, text = "C", fg = "black", bg = "green yellow",command=lambda:[conta("green yellow",6, "Não possui", "C", "Carbono")], height=hei, width=wid) 

        C.grid(row = 2, column = 14) 

  

        Si = Button(base, text = "Si", fg = "black", bg = "medium aquamarine",command=lambda:[conta("medium aquamarine",14, "[Ne] 3s¹ 3p²", "Si", "Silício")], height=hei, width=wid) 

        Si.grid(row = 3, column = 14) 

  

        Ge = Button(base, text = "Ge", fg = "black", bg = "medium aquamarine",command=lambda:[conta("medium aquamarine",32, "[Ar] 3d¹⁰ 4s² 4p²", "Ge", "Germânio")], height=hei, width=wid) 

        Ge.grid(row = 4, column = 14) 

  

        Sn = Button(base, text = "Sn", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",50, "[Kr] 4d¹⁰ 5s² 5p²", "Sn", "Estanho")], height=hei, width=wid) 

        Sn.grid(row = 5, column = 14) 

  

        Pb = Button(base, text = "Pb", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",82, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p²", "Pb", "Chumbo")], height=hei, width=wid) 

        Pb.grid(row = 6, column = 14) 

  

        Fl = Button(base, text = "Fl", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",114, "Não possui", "Fi", "Fleróvio")], height=hei, width=wid) 

        Fl.grid(row = 7, column = 14) 

  

        N = Button(base, text = "N", fg = "black", bg = "green yellow",command=lambda:[conta("green yellow",7, "Não possui", "N", "Nitrogênio")], height=hei, width=wid) 

        N.grid(row = 2, column = 15) 

  

        P = Button(base, text = "P", fg = "black", bg = "green yellow",command=lambda:[conta("green yellow",15, "[Ne] 3s¹ 3p³", "P", "Fósforo")], height=hei, width=wid) 

        P.grid(row = 3, column = 15) 

  

        As = Button(base, text = "As", fg = "black", bg = "medium aquamarine",command=lambda:[conta("medium aquamarine",33, "[Ar] 3d¹⁰ 4s² 4p³", "As", "Arsênio")], height=hei, width=wid) 

        As.grid(row = 4, column = 15) 

  

        Sb = Button(base, text = "Sb", fg = "black", bg = "medium aquamarine",command=lambda:[conta("medium aquamarine",51, "[Kr] 4d¹⁰ 5s² 5p³", "Sb", "Antimônio")], height=hei, width=wid) 

        Sb.grid(row = 5, column = 15) 

  

        Bi = Button(base, text = "Bi", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",83, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p³", "Bi", "Bismuto")], height=hei, width=wid) 

        Bi.grid(row = 6, column = 15) 

  

        Mc = Button(base, text = "Mc", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",115, "Não possui", "Mc", "Moscovio")], height=hei, width=wid) 

        Mc.grid(row = 7, column = 15) 

  

        O = Button(base, text = "O", fg = "black", bg = "green yellow",command=lambda:[conta("green yellow",8, "Não possui", "O", "Oxigênio")], height=hei, width=wid) 

        O.grid(row = 2, column = 16) 

  

        S = Button(base, text = "S", fg = "black", bg = "green yellow",command=lambda:[conta("green yellow",16, "[Ne] 3s¹ 3p⁴", "S", "enxofre")], height=hei, width=wid) 

        S.grid(row = 3, column = 16) 

  

        Se = Button(base, text = "Se", fg = "black", bg = "green yellow",command=lambda:[conta("green yellow",34, "[Ar] 3d¹⁰ 4s² 4p⁴", "Se", "Selênio")], height=hei, width=wid) 

        Se.grid(row = 4, column = 16) 

  

        Te = Button(base, text = "Te", fg = "black", bg = "medium aquamarine",command=lambda:[conta("medium aquamarine",52, "[Kr] 4d¹⁰ 5s² 5p⁴", "Te", "Telúrio")], height=hei, width=wid) 

        Te.grid(row = 5, column = 16) 

  

        Po = Button(base, text = "Po", fg = "black", bg = "medium aquamarine",command=lambda:[conta("medium aquamarine",84, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p4", "Po", "Polônio")], height=hei, width=wid) 

        Po.grid(row = 6, column = 16) 

  

        Lv = Button(base, text = "Lv", fg = "black", bg = "light sky blue",command=lambda:[conta("light sky blue",116, "Não possui", "Lv", "Livermório")], height=hei, width=wid) 

        Lv.grid(row = 7, column = 16) 

  

        F = Button(base, text = "F", fg = "black", bg = "cadet blue",command=lambda:[conta("cadet blue",9, "Não possui", "F", "Flúor")], height=hei, width=wid) 

        F.grid(row = 2, column = 17) 

  

        Cl = Button(base, text = "Cl", fg = "black", bg = "cadet blue",command=lambda:[conta("cadet blue",17, "[Ne] 3s¹ 3p⁵", "Cl", "Cloro")], height=hei, width=wid) 

        Cl.grid(row = 3, column = 17) 

  

        Br = Button(base, text = "Br", fg = "black", bg = "cadet blue",command=lambda:[conta("cadet blue",35, "[Ar] 3d¹⁰ 4s² 4p⁵", "Br", "Bromo")], height=hei, width=wid) 

        Br.grid(row = 4, column = 17) 

  

        I = Button(base, text = "I", fg = "black", bg = "cadet blue",command=lambda:[conta("cadet blue",53, "[Kr] 4d¹⁰ 5s² 5p⁵", "I", "Iodo")], height=hei, width=wid) 

        I.grid(row = 5, column = 17) 

  

        At = Button(base, text = "At", fg = "black", bg = "cadet blue",command=lambda:[conta("cadet blue",85, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p5", "At", "Astato")], height=hei, width=wid) 

        At.grid(row = 6, column = 17) 

  

        Ts = Button(base, text = "Ts", fg = "black", bg = "cadet blue",command=lambda:[conta("cadet blue",117, "Não possui", "Ts", "Tennessio")], height=hei, width=wid) 

        Ts.grid(row = 7, column = 17) 

  

        He = Button(base, text = "He", fg = "black", bg = "steel blue",command=lambda:[conta("steel blue",2, "Não possui", "He", "Hélio")], height=hei, width=wid) 

        He.grid(row = 1, column = 18) 

  

        Ne = Button(base, text = "Ne", fg = "black", bg = "steel blue",command=lambda:[conta("steel blue",10, "Não possui", "Ne", "Neônio")], height=hei, width=wid) 

        Ne.grid(row = 2, column = 18) 

  

        Ar = Button(base, text = "Ar", fg = "black", bg = "steel blue",command=lambda:[conta("steel blue",18, "[Ne] 3s¹ 3p⁶", "Ar", "Argônio")], height=hei, width=wid) 

        Ar.grid(row = 3, column = 18) 

  

        Kr = Button(base, text = "Kr", fg = "black", bg = "steel blue",command=lambda:[conta("steel blue",36, "[Ar] 3d¹⁰ 4s² 4p⁶", "Kr", "Criptônio")], height=hei, width=wid) 

        Kr.grid(row = 4, column = 18) 

  

        Xe = Button(base, text = "Xe", fg = "black", bg = "steel blue",command=lambda:[conta("steel blue",54, "[Kr] 4¹⁰ 5s² 5p⁶", "Xe", "Xenônio")], height=hei, width=wid) 

        Xe.grid(row = 5, column = 18) 

  

        Rn = Button(base, text = "Rn", fg = "black", bg = "steel blue",command=lambda:[conta("steel blue",86, "[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶", "Rn", "Radônio")], height=hei, width=wid) 

        Rn.grid(row = 6, column = 18) 

  

        Og = Button(base, text = "Og", fg = "black", bg = "steel blue",command=lambda:[conta("steel blue",118, "Não possui", "Og", "Oganessio")], height=hei, width=wid) 

        Og.grid(row = 7, column = 18) 

  

        Dy = Button(base, text = "Dy", fg = "black", bg = "cyan",command=lambda:[conta("cyan",66, "[Xe] 4f¹⁰ 6s²", "Dy", "Disprósio")], height=hei, width=wid) 

        Dy.grid(row = 10, column = 13) 

  

        Cf = Button(base, text = "Cf", fg = "black", bg = "pink",command=lambda:[conta("pink",98, "[Rn] 5f¹⁰ 7s²", "Cf", "Califórnio")], height=hei, width=wid) 

        Cf.grid(row = 11, column = 13) 

  

        Ho = Button(base, text = "Ho", fg = "black", bg = "cyan",command=lambda:[conta("cyan",67, "[Xe] 4f¹¹ 6s²", "Ho", "Hólmio")], height=hei, width=wid) 

        Ho.grid(row = 10, column = 14) 

  

        Es = Button(base, text = "Es", fg = "black", bg = "pink",command=lambda:[conta("pink",99, "[Rn] 5f¹¹ 7s²", "Es", "Einstênio")], height=hei, width=wid) 

        Es.grid(row = 11, column = 14) 

  

        Er = Button(base, text = "Er", fg = "black", bg = "cyan",command=lambda:[conta("cyan",68, "[Xe] 4f¹² 6s²", "Er", "Érbio")], height=hei, width=wid) 

        Er.grid(row = 10, column = 15) 

  

        Fm = Button(base, text = "Fm", fg = "black", bg = "pink",command=lambda:[conta("pink",100, "[Rn] 5f¹² 7s²", "Fm", "Férmio")], height=hei, width=wid) 

        Fm.grid(row = 11, column = 15) 

  

        Tm = Button(base, text = "Tm", fg = "black", bg = "cyan",command=lambda:[conta("cyan",69, "[Xe] 4f¹³ 6s²", "Tm", "Túlio")], height=hei, width=wid) 

        Tm.grid(row = 10, column = 16) 

  

        Md = Button(base, text = "Md", fg = "black", bg = "pink",command=lambda:[conta("pink",101, "[Rn] 5f¹³ 7s²", "Md", "Mendelévio")], height=hei, width=wid) 

        Md.grid(row = 11, column = 16) 

  

        Yb = Button(base, text = "Yb", fg = "black", bg = "cyan",command=lambda:[conta("cyan",70, "[Xe] 4f¹⁴ 6s²", "Yb", "Itérbio")], height=hei, width=wid) 

        Yb.grid(row = 10, column = 17) 

  

        No = Button(base, text = "No", fg = "black", bg = "pink",command=lambda:[conta("pink",102, "[Rn] 5f¹⁴ 7s²", "No", "Nobélio")], height=hei, width=wid) 

        No.grid(row = 11, column = 17) 

  

        Lu = Button(base, text = "Lu", fg = "black", bg = "cyan",command=lambda:[conta("cyan",71, "[Xe] 4f¹⁴ 5d¹ 6s²", "Lu", "Lutécio")], height=hei, width=wid) 

        Lu.grid(row = 10, column = 18) 

  

        Lr = Button(base, text = "Lr", fg = "black", bg = "pink",command=lambda:[conta("pink",103, "Não possui", "Lr", "Laurêncio")], height=hei, width=wid) 

        Lr.grid(row = 11, column = 18) 

  

        nove = Label(base, text = "", fg = "white", bg = "white") 

        nove.grid(row = 9, column = 10)

          
        base.mainloop()

        stop = 1 
