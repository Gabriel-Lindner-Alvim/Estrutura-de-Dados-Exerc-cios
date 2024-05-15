class Nó:
    def __init__(self, data=None, proximo=None):
        self.data = data #pode conter int, num ou objetos complexos
        self.proximo = proximo #ponteiro para proximo elemento

class ListaEncadeada:
    def __init__(self):
        self.head = None #aponta para o primeiro item  (ou head = cabeça) da lista encadeada
    
    
    def inserir_no_comeco(self, data): #pega a data e insere no comeco da lista
        nó = Nó(data, self.head)
        self.head = nó #atribui o novo nó como sendo o primeiro da lista encadeada

    
    def inserir_no_final(self, data): #pega a data e insere no final da lista
        if self.head is None: #checa se a lista está vazia
            self.head = Nó(data, None) # se estiver vazia, adiciona novo nó e retorna. terminando a função
            return 
        
        iterador = self.head # se nao estiver vazia, passa por aqui, começando no primeiro item da lista, self.head.
        while iterador.proximo: # enquanto iterador não for Null, percorre os itens da lista encadeada
            iterador = iterador.proximo # percorre os itens da lista, até que iterador.proximo = Null, quebrando o while
    
        iterador.proximo = Nó(data, None) # inclui o nó na última posição da lista.
    
    
    def inserir_valores(self, lista_data): # insere multiplos valores de uma so vez, mas cria uma lista encadeada nova. (é possível incluir em uma já existente, apenas optei por criar uma nova)
        self.head = None # exclui a lista encadeada existente
        for data in lista_data:
            self.inserir_no_final(data) 
    
    
    def descobrir_tamanho(self):
        contador = 0
        iterador = self.head #iterador começa no inicio da lista
        while iterador: #enquanto iterador nao for nulo:
            contador += 1
            iterador = iterador.proximo # passa para proximo item da lista
        
        return contador
    
    
    def excluir_no_index(self, index):
        if index < 0 or index >= self.descobrir_tamanho():
            raise Exception('Index inválido')
        
        if index == 0:
            self.head = self.head.proximo
            return
        
        contador = 0
        iterador = self.head
        while iterador:
            if contador == index - 1: # se o contador for igual ao index recebido na função, entra no if
                iterador.proximo = iterador.proximo.proximo # "transforma" o iterador.proximo.proximo no iterador.proximo, assim excluindo o item que ficava entre o interador e o interador.proximo.proximo 
                break # quebra o while quando conseguir fazer isso
            iterador = iterador.proximo
            contador += 1
    

    def remover_por_valor(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.proximo
            return
        
        iterador = self.head
        while iterador.proximo:
            if iterador.proximo.data == data:
                iterador.proximo = iterador.proximo.proximo
                break
            iterador = iterador.proximo
    
    
    def inserir_depois_valor(self, data_depois, data_pra_inserir):
        iterador = self.head
        while iterador:
            if iterador.data == data_depois:
                nó = Nó(data_pra_inserir, iterador.proximo)
                iterador.proximo = nó
                break
            iterador = iterador.proximo
    
    
    def incluir_no_index(self, index, data):
        if index < 0 or index >= self.descobrir_tamanho():
            raise Exception('Index inválido')
        
        if index == 0:
            self.inserir_no_comeco(data)
            return

        contador = 0
        iterador = self.head
        while iterador:
            if contador == index - 1:
                nó = Nó(data, iterador.proximo)
                iterador.proximo = nó
                break
            iterador = iterador.proximo
            contador += 1

    
    def print(self):
        if self.head is None: 
            print("Lista Encadeada está vazia") # se lista estiver vazia, quando cahamar lis_enc.print(), retorna Lista Encadeada está vazia
            return
        
        iterador = self.head
        lista_encadeada_str = ''
        while iterador: # enquanto iterador nao for igual a Null
            lista_encadeada_str += str(iterador.data) + '-->' # adiciona ao string o dado do item da lista atual, onde o ponteiro está
            iterador = iterador.proximo # passa para o próximo iterador, até o mesmo ser nulo, no qual esse quebra o loop do while
        
        print(lista_encadeada_str) # se a lista não estiver vazia, aqui está todos os itens da lista já 'formatados'.



if __name__ == '__main__':
    lis_enc = ListaEncadeada()
    lis_enc.inserir_valores(["banana", "mango", "grape", "orange"])
    lis_enc.print()
    lis_enc.inserir_depois_valor("mango", "apple")
    lis_enc.print()
    lis_enc.remover_por_valor("orange")
    lis_enc.print()
    lis_enc.remover_por_valor("figs")
    lis_enc.print()
    lis_enc.remover_por_valor("banana")
    lis_enc.remover_por_valor("mango")
    lis_enc.remover_por_valor("apple")
    lis_enc.remover_por_valor("grape")
    lis_enc.print()