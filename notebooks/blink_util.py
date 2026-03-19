import numpy as np


def twopi_normalize(phi_n1, phi_n2, coef, verbose=False):
    """
    Docstring for twopi_normalize

    Generates phi_sub_n2n1 where phi_sub_n1n2 = phi_sub_n2 - N2*phi_sub_n1
    
    :param phi_n1: phi_sub_n1 where n1 is an integer
    :param phi_n2: phi_sub_n2 where n2 is an integer not equals n1
    :param coef: coefficient which is equals integer n2 of phi_sub_n1
    :param verbose: True to print old and new values for normalization

    :returns phi_sub_n2n1: Ex: for n2=3 and n1=1 returns Phi_31
    """

    phi_sub_n2n1 = phi_n2 - coef*phi_n1  
    

    for i in range(len(phi_sub_n2n1)):
        Val = phi_sub_n2n1[i]
        OldVal = Val
        while Val < 0:
            Val += 2*np.pi
        while Val > 2*np.pi:
            Val -= 2*np.pi
        phi_sub_n2n1[i] = Val
        if verbose == True:
            print(f'Was {OldVal} and now is {Val}.')

    return phi_sub_n2n1



def get_FoH(df, verbose=False):
    P = df['period'].to_numpy()
    phi1 = df['phi1'].to_numpy()
    phi3 = df['phi3'].to_numpy()

    #print(P)

    phi31 = twopi_normalize(phi1,phi3,coef=3,verbose=verbose)


    Fe_on_H = -5.038-5.394*P+1.345*phi31
    return Fe_on_H

def Calc_R2(TrueValues, PredValues):
    # https://en.wikipedia.org/wiki/Coefficient_of_determination
    n = len(TrueValues)
    x_sum = TrueValues.sum()
    y_sum = PredValues.sum()
    xy_sum = (TrueValues*PredValues).sum()
    x2_sum = (TrueValues * TrueValues).sum()
    y2_sum = (PredValues * PredValues).sum()

    r_top = n*xy_sum - x_sum*y_sum
    r2_bottom = (n*x2_sum - x_sum*x_sum)*(n*y2_sum - y_sum*y_sum)

    if r2_bottom == 0:
        return np.nan
    else:
        return (r_top * r_top)/r2_bottom