import numpy as np

for m in range(1,16):

    implicant = np.array([])

    for reason in range(0,np.pow(3,m)-1):

        num_of_two = 0

        for pos in range(0,m):

            if (reason//np.pow(3,m-pos-1))%3 == 2:

                num_of_two += 1

        implicant = np.append(implicant,num_of_two)

    implicant = np.argsort(implicant)[::-1]

    file = open(f"implicant/m_is_{str(m)}.npy","w")

    np.save(f"implicant/m_is_{str(m)}.npy",implicant)

    print(np.load(f"implicant/m_is_{str(m)}.npy"))