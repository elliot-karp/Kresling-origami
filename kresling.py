import numpy as np
import matplotlib.pyplot as plt

def draw_kresling_origami(a, b, alpha_deg, n, m):
    """
    Given
       a = length of side AB
       b = length of side AC
       alpha_deg = angle at A (in degrees) between AB and AC
       n, m = how many parallelograms horizontally and vertically
    Return
        Printable visual origami pattern which can be folded into a kresling structure with the given parameters
    """
    alpha = np.radians(alpha_deg)
    L_AB = a
    L_AC = b  

    # coordinates of the base parallelogram corners
    # A = (0, 0)
    # B = (a, 0) = (a, 0)
    # C = L_AC * (cos alpha, sin alpha) = (L_AC cos alpha, L_AC sin alpha)
    A = np.array([0.0, 0.0])
    B = np.array([L_AB, 0.0])
    C = L_AC * np.array([np.cos(alpha), np.sin(alpha)]) 
    H = np.round(b * np.sin(alpha), 2)   

    # init lists to store line segments
    segments_solid = []
    segments_dashed = []

    # functions to append segments to lists
    def add_solid(p1, p2):
        segments_solid.append(((p1[0], p2[0]), (p1[1], p2[1])))

    def add_dashed(p1, p2):
        segments_dashed.append(((p1[0], p2[0]), (p1[1], p2[1])))

    # iterate over columns (n) and rows (m), adding parallelogram segments
    for j in range(m):
        for i in range(n):

            shift = i*(B - A) + j*(C - A)
            Ai = A + shift
            Bi = B + shift
            Ci = C + shift
            Di = Bi + (C - A) 

            # add solid edges 
            add_solid(Ai, Bi)
            add_solid(Bi, Di)
            add_solid(Di, Ci)
            add_solid(Ci, Ai)

            # add dashed edges 
            add_dashed(Ai, Di)

    # plotting:
    fig, ax = plt.subplots()
    
    # plot solid edges
    for seg in segments_solid:
        xs, ys = seg
        ax.plot(xs, ys, 'k-')
    # plot dashed diagonals
    for seg in segments_dashed:
        xs, ys = seg
        ax.plot(xs, ys, 'k--')  

    # Formatting
    ax.set_aspect('equal', 'box')
    ax.set_xticks([])  
    ax.set_yticks([]) 
    ax.set_xlabel('')
    ax.set_ylabel('')

    # height computation and characteristics of the Kresling
    ax.set_title(f"Kresling origami: a={a}, b={b}, alpha={alpha_deg}°, (computed H={H}), n={n}, m={m}")
    plt.show()

if __name__ == "__main__":
    # define Kresling characteristics 
    draw_kresling_origami(a=13.3, b=16.6, alpha_deg=53, n=6, m=4)