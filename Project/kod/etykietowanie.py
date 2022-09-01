from PIL import Image
import numpy as np

#Wartosc etykiety, zwiekszana o 1 po kazdym elemencie
label = 1

def etykietowanie():
    obraz = Image.open("coins_bin.bmp")
    image_array = np.array(obraz)
    (row, col) = image_array.shape
    #Zamiana na uint8 0,255
    image_array = image_array.astype(np.uint8)
    image_array = image_array * 255

    image_array_copy = image_array.copy()
    #Pętla po kolumnach
    for j in range(col):
        for i in range(row):
            if image_array[i, j] == 255:
                marker = reconstruct(image_array_copy, i, j)  # stworz marker ze znalezionym elementem
                image_array = fill(image_array, marker)  # dodaj etykiety w obrazie wejsciowym
                #image_array_copy = remove(image_array_copy, marker) usuniecie, moze sie przydac w przyszlosci

    obraz_etykietowanie = Image.fromarray(image_array * 20)
    obraz_etykietowanie.save("coins_ety.png")


def reconstruct(image_array, i, j):
    (row, col) = image_array.shape
    marker = np.zeros((row, col))
    marker[i, j] = 255
    while 1:
        tmp = marker.copy()
        marker = intersect(dylacja(1, marker), image_array)
        if np.array_equal(tmp, marker):
            break
    return marker.astype(np.uint8)


def dylacja(r, image_array):
    image_array = np.pad(image_array, pad_width=r, mode='constant', constant_values=0)
    (row, col) = image_array.shape
    image_array_cp = image_array.copy()
    for i in range(r, row - r):
        for j in range(r, col - r):
            if check(r + 2, image_array[i - r:i + r + 1, j - r:j + r + 1]):
                image_array_cp[i, j] = 255
    image_array_cp = image_array_cp[r:-r, r:-r]
    return image_array_cp


def remove(arr1, arr2):
    (x, y) = arr1.shape
    for i in range(x):
        for j in range(y):
            if arr2[i, j] == 255:
                arr1[i, j] = 0
    return arr1


def check(r, arr):
    for i in range(r):
        for j in range(r):
            if arr[i, j] == 255:
                return 1
    return 0


def intersect(arr1, arr2):
    arr = arr1.copy()
    (x, y) = arr1.shape
    for i in range(x):
        for j in range(y):
            if arr1[i, j] == 255 and arr2[i, j] == 255:
                arr[i, j] = 255
            else:
                arr[i, j] = 0
    return arr


def fill(arr1, arr2):
    (x, y) = arr1.shape
    global label
    for i in range(x):
        for j in range(y):
            if arr2[i, j] == 255:
                arr1[i, j] = label
    label += 1
    return arr1
