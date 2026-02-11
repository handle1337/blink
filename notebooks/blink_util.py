import numpy as np


def get_FoH(df):
    P = df['period'].to_numpy()
    phi1 = df['phi1'].to_numpy()
    phi3 = df['phi3'].to_numpy()

    phi31 = phi3 - 3*phi1
    phi31

    for i in range(len(phi31)):
        Val = phi31[i]
        OldVal = Val
        while Val < 0:
            Val += 2*np.pi
        while Val > 2*np.pi:
            Val -= 2*np.pi
        phi31[i] = Val
        print(f'Was {OldVal} and now is {Val}.')

    phi31

    Fe_on_H = -5.038-5.394*P+1.345*phi31
    return Fe_on_H