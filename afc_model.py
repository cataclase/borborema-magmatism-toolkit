import numpy as np


def afc_curve(Sr_m, R_m, Sr_c, R_c, r, D):
    """
    Compute AFC evolution curve.

    Parameters
    ----------
    Sr_m : float
        Sr concentration of parental magma.

    R_m : float
        87Sr/86Sr ratio of parental magma.

    Sr_c : float
        Sr concentration of crust.

    R_c : float
        87Sr/86Sr ratio of crust.

    r : float
        Assimilation/crystallization ratio.

    D : float
        Bulk partition coefficient.

    Returns
    -------
    Sr_model : ndarray
    R_model : ndarray
    """

    F = np.linspace(1,0.01,500)

    Sr_model = (Sr_m*F**D + Sr_c*r*(1-F))/(F + r*(1-F))

    R_model = (R_m*Sr_m*F**D + R_c*Sr_c*r*(1-F))/(Sr_model*(F+r*(1-F)))

    return Sr_model, R_model


def monte_carlo_afc(x_data, y_data, Sr_m, R_m, Sr_c, R_c, iterations=10000):
    """
    Estimate AFC parameters via Monte Carlo simulation.
    """

    best_error = np.inf

    best_r = None
    best_D = None
    best_curve = None

    for _ in range(iterations):

        r = np.random.uniform(0.01,0.5)
        D = np.random.uniform(0.5,3.0)

        Sr_model, R_model = afc_curve(Sr_m,R_m,Sr_c,R_c,r,D)

        dist = abs(R_model[:,None]-y_data) + abs(Sr_model[:,None]-x_data)/1000

        error = np.sum(np.min(dist,axis=0))

        if error < best_error:

            best_error = error
            best_r = r
            best_D = D
            best_curve = (Sr_model,R_model)

    return best_r, best_D, best_curve