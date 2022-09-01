from PIL import Image
import numpy as np

def otwarcie_bin():
    obraz = Image.open("blobs.png")
    r = input("Podaj promień maski: ")
    r = int(r)
    image_array = np.array(obraz)
    #Zamiana na uint8 0,255
    image_array = image_array.astype(np.uint8)
    image_array = image_array * 255
    #Stworzenie elementu strukturalnego
    SE = create_SE(r)
    #dodanie pixeli na krawędziach
    image_array = np.pad(image_array, pad_width=r, mode='constant', constant_values=255)
    (row,col) = image_array.shape
    obraz_otwarcie = Image.fromarray(dylacja_bin( r,row,col,erozja_bin(r,row,col,image_array,SE),SE))
    obraz_otwarcie.save("blobs_open.png")


def otwarcie_mono():
    obraz = Image.open("cameraman.png")
    r = input("Podaj promień maski: ")
    r = int(r)
    image_array = np.array(obraz)
    #Stworzenie elementu strukturalnego
    SE = create_SE(r)
    #dodanie pixeli na krawędziach
    image_array = np.pad(image_array, pad_width=r, mode='constant', constant_values=255)
    (row,col) = image_array.shape
    obraz_otwarcie = Image.fromarray(dylacja_mono( r,row,col,erozja_mono(r,row,col,image_array,SE),SE))
    obraz_otwarcie.save("cameraman_open.png")

def create_SE(r):
    SE = np.zeros((r*2-1,r*2-1), dtype=np.uint8)
    Sx = Sy = r-1
    for i in range(r*2-1):
        for j in range(r*2-1):
            if np.sqrt( abs(i - Sx)**2 + abs(j - Sy)**2 ) <= r:
                SE[i,j] = 255
    return SE


def check(r,arr,SE):
    for i in range(r*2-1):
        for j in range(r*2-1):
            if SE[i,j] == 255 and arr[i,j] != 255:
                return 1
    return 0

def check2(r,arr,SE):
    for i in range(r*2-1):
        for j in range(r*2-1):
            if SE[i,j] == 255 and arr[i,j] == 255:
                return 1
    return 0


def get_min(r,arr,SE):
    min = 255
    for i in range(r*2-1):
        for j in range(r*2-1):
            if SE[i,j] == 255 and arr[i,j] < min:
                min = arr[i,j]
    return min

def get_max(r,arr,SE):
    max = 0
    for i in range(r*2-1):
        for j in range(r*2-1):
            if SE[i,j] == 255 and arr[i,j] > max:
                max = arr[i,j]
    return max


def erozja_bin(r,row,col,image_array,SE):
    image_array_cp = image_array.copy()
    for i in range(r,row-r):
        for j in range(r,col-r):
            if image_array[i,j] == 255:
                if check(r,image_array[i-r:i+r+1, j-r:j+r+1],SE):
                    image_array_cp[i,j] = 0
    return image_array_cp


def dylacja_bin(r,row,col,image_array,SE):
    image_array = image_array[r:-r,r:-r]
    image_array = np.pad(image_array, pad_width=r, mode='constant', constant_values=0)
    image_array_cp = image_array.copy()
    for i in range(r,row-r):
        for j in range(r,col-r):
            if check2(r,image_array[i-r:i+r+1, j-r:j+r+1],SE):
                image_array_cp[i,j] = 255
    image_array_cp = image_array_cp[r:-r,r:-r]
    return image_array_cp


def erozja_mono(r,row,col,image_array,SE):
    image_array_cp = image_array.copy()
    for i in range(r,row-r):
        for j in range(r,col-r):
            image_array_cp[i,j] = get_min(r,image_array[i-r:i+r+1, j-r:j+r+1],SE)
    return image_array_cp


def dylacja_mono(r,row,col,image_array,SE):
    image_array = image_array[r:-r,r:-r]
    image_array = np.pad(image_array, pad_width=r, mode='constant', constant_values=0)
    image_array_cp = image_array.copy()
    for i in range(r,row-r):
        for j in range(r,col-r):
            image_array_cp[i,j] = get_max(r,image_array[i-r:i+r+1, j-r:j+r+1],SE)
    image_array_cp = image_array_cp[r:-r,r:-r]
    return image_array_cp
