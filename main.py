from bbcon import *

if __name__ == '__main__':
    # Endrer MasterFlag for å få kjørt ønsket kode
    MasterFlag = {
        -1: 'Testspace',
        0: 'run BBCon'
    }[-1]
    if MasterFlag == 'Testspace':
        print('Welcome to testspace')

        target_matrix = [[i * j for i in range(1, 10)] for j in range(1, 2)]
        width = len(target_matrix[0])
        left_right_size = int(width / 3)
        middle_size = width - 2 * left_right_size
        left_1s = 0
        middle_1s = 0
        right_1s = 0
        for r in target_matrix:
            print(r)
        for r in target_matrix:
            for e in r[:left_right_size]:
                print(e)
            for e in r[left_right_size:left_right_size + middle_size]:
                print(e)
            for e in r[width - left_right_size:]:
                print(e)

    elif MasterFlag == "run BBCon":
        print("Running BBCon")

        BBCon = BBCon()
        while 1:
            BBCon.run_one_timestep()
