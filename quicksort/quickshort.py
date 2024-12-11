def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista)-1
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim) 
    
def partition(lista, inicio, fim):
    pivot=lista[fim]
    i= inicio - 1


    for j in range(inicio, fim): 
        if lista[j] <= pivot:
            i = i+1
            lista[j], lista[i] = lista[i], lista[j]
          
    lista[ i+1 ], lista[fim]=lista[fim], lista[i +1]
    return i+1


def main():
    exemplos =[
        [84, 55	,90	,33, 42 ,8 ,97 ,32 ,59 ,56],
        [83, 39, 86 ,52 ,38 ,14 ,24 ,53 ,29 ,82],
        [15, 16, 42 ,29 ,59 ,55 ,96 ,41 ,17 ,85]
    ]
      
    for lista in exemplos:
        print("lista original:", lista)
        quicksort(lista)    
        print("lista ordenada:", lista)
        print()

if __name__ == "__main__":
    main()