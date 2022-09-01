from PIL import Image
import numpy as np
import otwarcie

def filtracja_mono():
    obraz = Image.open("cameraman.png")
    image_array = np.array(obraz)

    #podanie maski
    print("Kształty masek:\n"
          "1.Kołowa\n"
          "2.Prostokątna\n")
    choice = input("Wybierz numer maski: ")
    if choice == '1':
        r = int( input("Podaj promień: ") )
        SE = create_SE('circle',r)
    else:
        x = int( input("Podaj długość: ") )
        y = int( input("Podaj szerokość: ") )
        SE = create_SE('rectangle',x,y)

    (SE_row,SE_col) = SE.shape
    pad_width = max(SE_row,SE_col)
    image_array = np.pad(image_array, pad_width=pad_width, mode='symmetric')
    (row,col) = image_array.shape
    obraz_filter = filter(SE_row,SE_col,row,col,image_array,SE)
    obraz_filter = obraz_filter[pad_width:-pad_width,pad_width:-pad_width]
    obraz_filter = normalise_mono(obraz_filter)
    obraz_filter = Image.fromarray( obraz_filter )
    obraz_filter.save("cameraman_filt.png")

def filtracja_rgb():
    obraz = Image.open("white_tern.bmp")
    image_array = np.array(obraz)

    #podanie maski
    print("Kształty masek:\n"
          "1.Kołowa\n"
          "2.Prostokątna\n")
    choice = input("Wybierz numer maski: ")
    if choice == '1':
        r = int( input("Podaj promień: ") )
        SE = create_SE('circle',r)
    else:
        x = int( input("Podaj długość: ") )
        y = int( input("Podaj szerokość: ") )
        SE = create_SE('rectangle',x,y)

    (SE_row,SE_col) = SE.shape
    pad_width = max(SE_row,SE_col)
    image_array = np.pad(image_array, pad_width= ( (pad_width,pad_width),(pad_width,pad_width),(0,0)) , mode='symmetric')
    (row,col,d) = image_array.shape
    obraz_filter = filter(SE_row,SE_col,row,col,image_array,SE)
    obraz_filter = obraz_filter[pad_width:-pad_width,pad_width:-pad_width]
    obraz_filter = normalise_rgb(obraz_filter)
    obraz_filter = Image.fromarray( obraz_filter )
    obraz_filter.save("white_tern_filt.png")

def create_SE(shape,x,y=0):
    if shape == 'circle':
        return otwarcie.create_SE(x)
    se = np.ones((x,y), dtype=np.uint8) * 255
    return se


def filter(x,y,row,col,image_array,SE):
    image_array_cp = image_array.copy()
    for i in range(x,row-x):
        for j in range(y,col-y):
             image_array_cp[i,j] = get_std(x,y,image_array[i-x:i+x+1, j-y:j+y+1],SE)
    return image_array_cp


def get_std(x,y,arr,SE):
    pixels = list()
    for i in range(x):
        for j in range(y):
            if SE[i,j] == 255:
                pixels.append(arr[i,j])
    return np.std(pixels)


def normalise_mono(arr):
    arr_copy = arr.copy()
    (x,y) = arr.shape
    L = 0
    U = 255
    M = np.amin(arr)
    N = np.amax(arr)

    for i in range(x):
        for j in range(y):
            arr_copy[i,j] = ( (L - U) / ( int(M) - int(N)) ) * ( int(arr[i,j]) - int(M) ) + L
    return arr_copy

def normalise_rgb(arr):
    arr_copy = arr.copy()
    (x,y,z) = arr.shape
    L = 0
    U = 255
    M = np.amin(arr)
    N = np.amax(arr)

    for i in range(x):
        for j in range(y):
            arr_copy[i,j] = ( (L - U) / ( int(M) - int(N)) ) * ( int(arr[i,j,0]) - int(M) ) + L
    return arr_copy

