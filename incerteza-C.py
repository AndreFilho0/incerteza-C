import customtkinter as cus
import math as mat
import sympy as sp



def obter_valores():
  janela2=cus.CTk()
  janela2.title(" Incerteza")
  janela2.geometry("1000x1000")
  x,y,z,t,h=sp.symbols('x y z t h')
  v4=funcao.get()
  texto3=cus.CTkLabel(janela2,text=f"sua função é {v4}")
  texto3.pack(padx=10,pady=10)
  v5=sp.diff(v4,x)
  v6=sp.diff(v4,y)
  v7=sp.diff(v4,z)
  v8=sp.diff(v4,t)
  v9 =sp.diff(v4,h)
  lista=[v5,v6,v7,v8,v9]
  lista_v=['x','y','z','t','h']
  for valor,variavel in zip(lista,lista_v):
    texto4=cus.CTkLabel(janela2,text=f"sua derivada parcial em relação a '{variavel}' são respectivamente:\n{valor}")
    texto4.pack(padx=10,pady=10)
  v10=float(x_.get())
  i1=float(x_i.get())
  v12=float(y_.get())
  i2= float(y_i.get())
  v13= float(z_.get())
  i3= float(z_i.get())
  v14= float(t_.get())
  i4= float(t_i.get())
  v15= float(h_.get())
  i5= float(h_i.get())
  v20 =v5.subs([(x, v10), (y, v12), (z, v13),(t,v14),(h,v15)])
  v21 =v6.subs([(x, v10), (y, v12), (z, v13), (t, v14), (h, v15)])
  v22 =v7.subs([(x, v10), (y, v12), (z, v13), (t, v14), (h, v15)])
  v23 =v8.subs([(x, v10), (y, v12), (z, v13), (t, v14), (h, v15)])
  v24 =v9.subs([(x, v10), (y, v12), (z, v13), (t, v14), (h, v15)])
  upc=mat.sqrt(pow(v20,2)*pow(i1,2) + pow(v21,2)*pow(i2,2) + pow(v22,2)*pow(i3,2) + pow(v23,2)*pow(i4,2) + pow(v24,2)*pow(i5,2))
  texto4=cus.CTkLabel(janela2,text=f"sua incerteza do tipo C é: {upc}")
  texto4.pack(padx=10,pady=10)


  
  janela2.mainloop()



cus.set_appearance_mode("Dark")

janela1 = cus.CTk()
janela1.title(" Incerteza")
janela1.geometry("1200x1200")


texto1=cus.CTkLabel(janela1,text="calculando a Incerteza tipo C")
texto1.pack(padx=10,pady=10)

texto2=cus.CTkLabel(janela1,text="a função que vai ser derivada pode ter as seguintes variaveis:\nx,y,z,t,h\n PRESTA ATENÇÃO")
texto2.pack(padx=10,pady=10)


funcao=cus.CTkEntry(janela1,placeholder_text="coloca a função")
funcao.pack(padx=10,pady=10)

x_ = cus.CTkEntry(janela1,placeholder_text="infome o valor de x")
x_.pack(padx=10,pady=10)

x_i = cus.CTkEntry(janela1,placeholder_text="incerteza de x")
x_i.pack(padx=10,pady=10)

y_ =cus.CTkEntry(janela1,placeholder_text="informe o valor de y")
y_.pack(padx=10,pady=10)

y_i=cus.CTkEntry(janela1,placeholder_text=" incerteza de y")
y_i.pack(padx=10,pady=10)

z_=cus.CTkEntry(janela1,placeholder_text="informe o valor de z")
z_.pack(padx=10,pady=10)

z_i=cus.CTkEntry(janela1,placeholder_text="incerteza de z")
z_i.pack(padx=10,pady=10)

t_=cus.CTkEntry(janela1,placeholder_text="informe o valor de t")
t_.pack(padx=10,pady=10)

t_i=cus.CTkEntry(janela1,placeholder_text="incerteza de t")
t_i.pack(padx=10,pady=10)
 
h_=cus.CTkEntry(janela1,placeholder_text="informe o valor de h")
h_.pack(padx=10,pady=10)

h_i=cus.CTkEntry(janela1,placeholder_text=" incrteza de h")
h_i.pack(padx=10,pady=10)
  
  #button=cus.CTkButton(janela2,text="Continuar...",command=calcular_i)
  #button.pack(padx=10,pady=15)

button=cus.CTkButton(janela1,text="Start",command=obter_valores)
button.pack(padx=10,pady=15)

janela1.mainloop()