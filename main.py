#CONTROLADOR DO WHILE - PARTE 1 (

while True:#1
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
    while True: #2. Esse while repete a pergunta inicial até o usúario inserir um IP que contenha apenas caracter que possa ser transformado em inteiro e o número certo de octetos. 
        IP=input("Informe o novo ip: ")
        sem_ponto=IP.replace(".", "")#Tira o "." inserido, concatenando os números(que estão em str).
        ip_separado=IP.split(".")#cria uma lista onde cada elemento da mesma, será o conjunto de string até o próximo ".".
        while (len(ip_separado))!=4:#se a quantidade de elementos da lista "ip_separado" for diferente de 4, esse loop irá parar de executar as condições e voltar para a variável "IP". (Isso porque um ip precisa ter ao menos 4 octetos, se não, não é um ip)
            print(ip_separado, "Número de IP não válido")
            break
        else:
            try:#Aqui ele vai tentar transformar o valor da variavél "sem_ponto" em inteiro, se não conseguir, pula para o except e volta para o inicio do while true 2. 
                conferir_int = int(sem_ponto)#Transforma os dados inseridos em inteiro (estava em string).
                break
            except:
                print("Você inseriu alguma letra. Por favor, insira somente números")
            
                
    #Separa os elementos do ip e transforma em inteiros. Foi uma forma de transformar o ip que estava em string para inteiros. Além disso, tendo variavéis contendo cada "bloquinho"(chamarei de octetos futuramente) de números do ip, irá facilitar o codigo a seguir. 
    prim_elemento_ip=(int(ip_separado[0]))
    seg_elem=(int(ip_separado[1]))
    terc_elem=(int(ip_separado[2]))
    quar_elem=(int(ip_separado[3]))

#Confere se os números inseridos estão entre 0 e 255. (Mais uma restrição... se os números inserido forem maiores que 255 e menores que 0, não serão ips)
    if seg_elem <0 or seg_elem >255 or terc_elem <0 or terc_elem >255 or quar_elem <0 or quar_elem>255:
        print("Ip invalido. Não se encaixa em nenhuma classe")
        
  #Classificando o ip na respectiva classe.
    #CLASSE A: Para um ip ser da classe A, ele precisa começar com números entre 1 a 127 e não pode ter o resto com números iguais.
    if prim_elemento_ip>= 1 and prim_elemento_ip<=127:
        if seg_elem==0 and terc_elem==0 and quar_elem==0 or seg_elem==255 and terc_elem==255 and quar_elem==255:
            print("Ip invalido. Não se encaixa em nenhuma classe")
        else:
            classe_a.append(IP)
            print ("Esse ip é da classe a")
            
    #CLASSE B: Para um ip ser da classe B, ele precisa começar com números entre 128 a 191 e não pode ter o 3º e 4º octetos com números iguais. 
    elif prim_elemento_ip>=128 and prim_elemento_ip<=191:
        if quar_elem==0 and terc_elem==0 or terc_elem==255 and quar_elem==255:
            print("Ip invalido. Não se encaixa em nenhuma classe")
        else:
            classe_b.append(IP)
            print ("Esse ip é da classe b")
            
    #CLASSE c: Para um ip ser da classe C, ele precisa começar com números entre 192 a 223 .      
    elif prim_elemento_ip>=192 and prim_elemento_ip<=223: 
        if quar_elem>=1 and quar_elem<=254:
            classe_c.append(IP)
            lista_ips.append(IP)
          #Na classe C, ele pode ser subclassificado em dois tipos de redes: privada ou publica. E o proxímo if/else faz exatamente isso. 
            if prim_elemento_ip ==192 and seg_elem == 168:
                if terc_elem >=0 and terc_elem <=255 and quar_elem >=0 and quar_elem <=255:
                    print ("Esse ip é da classe C e de rede privada")
            else:
                print("Esse ip é da classe C e de uma rede pública")
    #Se o IP inserido não for classificado em nenhuma classe,ele será considerado invalido. 
    else:
        print("Ip invalido. Não se encaixa em nenhuma classe")

        
   #transformando a lista de ips em set para excluir os repetidos (se caso houver) e em tuplas para não serem alterados.
    sets_ips= set()
    sets_ips.update(tuple(lista_ips))     
    print ("Total de ips validos inseridos :", sets_ips)

    
#CONTROLADOR DO WHILE - PARTE 2 (
    if len(sets_ips)>= 2:
        requerimento= input("Quer inserir um novo ip ?")
        if requerimento=="Não" or requerimento== "não" or requerimento=="Nao" or requerimento== "nao":
            #transformando listas em tuplas para adicionar no Dic.
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
