import msvcrt
import os
import AsciiImgs
import battlesystem
from time import sleep

red = '\033[91m'
setar_cor = '\033[97m'
esc = 0

def clear():
    os.system('cls')

def menu():

    clear()
    esc = 0
    print(red)
    AsciiImgs.printUTF8(AsciiImgs.menuImg)
    print(setar_cor)
    print('Use as teclas A e D', '\n', 'E ENTER para selecionar')
    print('\n' * 1)
    print(' '*15, red, '-(> INICIAR', setar_cor)
    print(' '*15, 'SAIR')

    while True:

        if msvcrt.kbhit():

            tecla = msvcrt.getch()
            if tecla == b'A' or tecla == b'a':
                clear()
                esc = 0
                print(red)
                AsciiImgs.printUTF8(AsciiImgs.menuImg)
                print(setar_cor)
                print('Use the keys A and D to navigate','\n','Press ENTER to select\n')
                print(' '*4, red, '-(> INICIAR', setar_cor)
                print(' '*4, 'SAIR')
 
            if tecla == b'd' or tecla == b'D':
                clear()
                esc = 1
                print(red)
                AsciiImgs.printUTF8(AsciiImgs.menuImg)
                print(setar_cor)
                print('Use the keys A and D to navigate','\n','Press ENTER to select\n')
                print(' '*4, 'INICIAR')
                print(' '*4, red,'-(> SAIR', setar_cor)
            
            if tecla == b'\r' and esc == 0:
                print('Starting the game')
                sleep(1)
                battlesystem.StartBattle()
                break
            elif tecla == b'\r' and esc == 1:
                print('Closing terminal')
menu()