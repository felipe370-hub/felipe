def selection_sort(lista, inicio, fim):
    pivot=lista[fim]
    i=inicio -1

    for j in range(len(inicio, fim)):
        if lista[j]<= pivot:
            i+1
            lista[j], lista[i] = lista[i], lista[j]

    lista[i+1], lista[fim]= lista[fim], lista [i+1]
    return i+1
def main():
    exemplos=[
    [64, 31, 53, 65, 67, 89, 64, 66, 62]
    ]

    for lista in exemplos:
        print("lista original:", lista)
        selection_sort(lista)
        print("lista ordenada:", lista)
        print()

if __name__ =="__main__":
    main()