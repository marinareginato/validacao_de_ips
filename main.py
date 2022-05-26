#CONTROLADOR DO WHILE - PARTE 1 (

while True:
  requerimento= input("Quer inserir um novo ip ?")
  if requerimento=="Não" or requerimento== "não" or   requerimento=="Nao" or requerimento== "nao":
    exit()
  elif requerimento=="Sim" or requerimento== "sim":
    break
  else:
    print ("Somente respostas valídas (sim ou não)")
  
  
#)
    
#Lista dos ips obtidos:
#lista_ips são os ips especificos que queremos (os que passarem em todas as validações e ser da classe C)
lista_ips = []
#lista de classes:
classe_a=[]
classe_b=[]
classe_c=[]

#O while irá se repetir até o usúario informar no minímo 10 IPS e responder a variavel "requerimento" com um "não".
while requerimento:
    while True: #Esse while repete a pergunta inicial até o usúario inserir um IP que contenha apenas números e o número certo de octetos. 
        IP=input("Informe o novo ip: ")
        sem_ponto=IP.replace(".", "")#Tira o "." inserido, juntado os números.
        ip_separado=IP.split(".")
        while (len(ip_separado))!=4:
            print(ip_separado, "Número de IP não válido")
            break
        else:
            try:
                conferir_int = int(sem_ponto)#Transforma os dados inseridos em inteiro (estava em string).
                break
            except:
                print("Você inseriu alguma letra. Por favor, insira somente números")
            
                
    #Separa os elementos do ip e transforma em inteiros.
    prim_elemento_ip=(int(ip_separado[0]))
    seg_elem=(int(ip_separado[1]))
    terc_elem=(int(ip_separado[2]))
    quar_elem=(int(ip_separado[3]))


        
  #Classificando o ip na respectiva classe.
    #CLASSE A:    
    if prim_elemento_ip>= 1 and prim_elemento_ip<=127:
        if seg_elem==0 and terc_elem==0 and quar_elem==0 or seg_elem==255 and terc_elem==255 and quar_elem==255:
            print("Ip invalido. Não se encaixa em nenhuma classe")
        else:
            classe_a.append(IP)
            print ("Esse ip é da classe a")
            
    #CLASSE B:
    elif prim_elemento_ip>=128 and prim_elemento_ip<=191:
        if quar_elem==0 and terc_elem==0 or terc_elem==255 and quar_elem==255:
            print("Ip invalido. Não se encaixa em nenhuma classe")
        else:
            classe_b.append(IP)
            print ("Esse ip é da classe b")
            
    #CLASSE c:        
    elif prim_elemento_ip>=192 and prim_elemento_ip<=223: 
        if quar_elem>=1 and quar_elem<=254:
            classe_c.append(IP)
            lista_ips.append(IP)
            if prim_elemento_ip ==192 and seg_elem == 168:
                if terc_elem >=0 and terc_elem <=255 and quar_elem >=0 and quar_elem <=255:
                    print ("Esse ip é da classe C e de rede privada")
            else:
                print("Esse ip é da classe C e de uma rede pública")
    #Se o IP inserido não for classificado em nenhuma classe,ele será considerado invalido. 
    else:
        print("Ip invalido. Não se encaixa em nenhuma classe")

        
   #transformando a lista de ips em set para excluir os repetido (se caso houver) e em tuplas para não ser alterados.
    sets_ips= set()
    sets_ips.update(tuple(lista_ips))     
    print ("Total de ips validos inseridos :", sets_ips)

    
#CONTROLADOR DO WHILE - PARTE 2 (
    if len(sets_ips)>= 2:
        requerimento= input("Quer inserir um novo ip ?")
        if requerimento=="Não" or requerimento== "não" or requerimento=="Nao" or requerimento== "nao":
            #transformando listas em tuplas para adicionar do Dic.
            classe_a_tupla=(classe_a)
            classe_b_tupla=(classe_b)
            classe_c_tupla=(classe_c)
            #Criando um dic para as classes. O valor das chaves são as tuplas criadas.
            classes = {"Classe A": classe_a_tupla, "Classe B": classe_b_tupla, "Classe C": classe_c_tupla}
            print (classes)
            break
    else:
        continue

#)
