import otwarcie
import etykietowanie
import filtracja
import normalizacja

print("Projekt Damian Gortych 402663")

print("Operacje do wyboru:\n"
      "1.Normalizacja wg łamanej\n"
      "2.Filtracja odchylenia standardowego\n"
      "3.Otwarcie elementem kołowym\n"
      "4.Etykietowanie\n")
nr = input("Wprowadz numer operacji, którą chcesz wykonać:")

if nr == '1':
    im_type = input("Wybierz rodzaj obrazu\n 1.RGB\n 2.Mono\n")
    if im_type == '1':
        normalizacja.normalizacja_rgb()
    else:
        normalizacja.normalizacja_mono()

if nr == '2':
    im_type = input("Wybierz rodzaj obrazu\n 1.RGB\n 2.Mono\n")
    if im_type == '1':
        filtracja.filtracja_rgb()
    else:
        filtracja.filtracja_mono()

if nr == '3':
    im_type = input("Wybierz rodzaj obrazu\n 1.Mono\n 2.Logiczny\n")
    if im_type == '1':
        otwarcie.otwarcie_mono()
    else:
        otwarcie.otwarcie_bin()

if nr == '4':
    etykietowanie.etykietowanie()



