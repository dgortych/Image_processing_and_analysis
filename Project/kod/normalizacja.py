from PIL import Image
import numpy as np


def normalizacja_mono():
    obraz = Image.open("cameraman.png")
    image_array = np.array(obraz)
    image_array_copy = image_array.copy()
    (x,y) = image_array.shape
    #Wczytanie zadanych punktów
    points = get_points()
    points = [0,0] + points + [255,255]

    for n in range(0, len(points), 2):
        for i in range(x):
            for j in range(y):
                if points[n] <= image_array[i, j] <= points[n + 2]:  # Sprawdz czy pixel znajduje sie w normalizowanym obszarze
                    L = points[n+1]   # min skali
                    U = points[n+3]   # max skali
                    #M = get_min( image_array,points[n],points[n+2] )  #min w normalizowanym obszarze
                    #N = get_max( image_array,points[n],points[n+2] )  #max w normalizowanym obszarze
                    M = points[n]
                    N = points[n+2]
                    image_array_copy[i,j] = ( (L - U) / ( int(M) - int(N)) ) * ( int(image_array[i,j]) - int(M) ) + L  #normalizacja

    obraz_norm = Image.fromarray( image_array_copy )
    obraz_norm.save("cameraman_norm.png")


def normalizacja_rgb():
    obraz = Image.open("white_tern.bmp")
    image_array = np.array(obraz)
    image_array_copy = image_array.copy()
    (x,y,z) = image_array.shape
    #Wczytanie zadanych punktów
    points = get_points()
    points = [0,0] + points + [255,255]

    for n in range(0, len(points), 2):
        for i in range(x):
            for j in range(y):
                for k in range(z):
                    if points[n] <= image_array[i, j, k] <= points[n + 2]:  # Sprawdz czy pixel znajduje sie w normalizowanym obszarze
                        L = points[n+1]  # min skali
                        U = points[n+3]  # max skali
                        # M = get_min_rgb( image_array,points[n],points[n+2],k )  #min w normalizowanym obszarze
                        # N = get_max_rgb( image_array,points[n],points[n+2],k )  #max w normalizowanym obszarze
                        M = points[n]
                        N = points[n+2]
                        image_array_copy[i,j,k] = ( (L - U) / ( int(M) - int(N)) ) * ( int(image_array[i,j,k]) - int(M) ) + L  #normalizacja

    obraz_norm = Image.fromarray( image_array_copy )
    obraz_norm.save("white_tern_norm.png")


def get_points():
    points_str = input('Enter points, each number separated by space:')
    points_list = points_str.split()
    points_list = [int(i) for i in points_list]
    return points_list


def get_min(arr,min_val,max_val):
    min = 255
    (x,y) = arr.shape
    for i in range(x):
        for j in range(y):
            if min_val <= arr[i, j] <= max_val and arr[i, j] < min:
                min = arr[i,j]
    return min

def get_max(arr,min_val,max_val):
    max = 0
    (x,y) = arr.shape
    for i in range(x):
        for j in range(y):
            if min_val <= arr[i, j] <= max_val and arr[i, j] > max:
                max = arr[i,j]
    return max

def get_min_rgb(arr,min_val,max_val,k):
    min = 255
    (x,y,z) = arr.shape
    for i in range(x):
        for j in range(y):
            if min_val <= arr[i, j, k] <= max_val and arr[i, j, k] < min:
                min = arr[i, j, k]
    return min

def get_max_rgb(arr,min_val,max_val,k):
    max = 0
    (x,y,z) = arr.shape
    for i in range(x):
        for j in range(y):
            if min_val <= arr[i, j, k] <= max_val and arr[i, j, k] > max:
                max = arr[i, j, k]
    return max

