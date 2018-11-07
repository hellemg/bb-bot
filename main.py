from bbcon import *

if __name__ == '__main__':
    # Endrer MasterFlag for å få kjørt ønsket kode
    MasterFlag = {
        -1: 'Testspace',
        0: 'run BBCon'
    }[0]
    if MasterFlag == 'Testspace':
        print('Welcome to testspace')
    elif MasterFlag == "run BBCon":
        print("Running BBCon")

        BBCon = BBCon()
        while 1:
            BBCon.run_one_timestep()