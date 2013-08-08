import numpy as np
import sys

np.set_printoptions(linewidth=200, precision=6)

# creates an n x n matrix where A_ij = 1 if i == j, and = i/(i+j)^2 otherwise
def create_matrix(n):
    mat = np.empty([n,n], dtype=float)
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                mat[i,j] = 1
            else:
                mat[i,j] = 1/(i + j)**2
    return mat

# creates a n x 1 vector from 1 to n
def create_vec(n):
    vec = np.empty([n,1], dtype=float)
    for i in range(0,n):
        vec[i,0] = i+1

    return vec


# does gaussian elimination (RREF) and backwards substitution to solve the system
def gaussian_sub(x, y, n):
    aug = np.concatenate((x, y), -1)
    found_p = False
    print('your augmented matrix: ')
    print(aug)

    # elimination step
    for i in range(0, n):
        p_f = i
        while (p_f < n):
            if aug[p_f,i] != 0:
                p = p_f
                found_p = True
                break
            p_f = p_f + 1
        if found_p == False or aug[p][i] == 0:
            print('no unique solutions exist')
            sys.exit(1)
        else:
            if p != i:
                t = np.array(aug[p], copy=1, dtype=float)
                aug[p] = aug[i]
                aug[i] = t

            for j in range(i+1, n):  
                k = aug[j,i]/aug[i,i]
                t2 = np.array(aug[j] - k*aug[i], copy=1, dtype=float)
                aug[j] = t2

    if aug[n-1,n-1] == 0:
       print("no unique solution exists")
       sys.exit(1)

    # start backwards substitution
    x_sol = np.copy(aug[:,n])
    x_sol[n-1] = aug[n-1,n]/aug[n-1,n-1]
    for i in range(n-2, -1, -1):
        summ = 0
        for r in range(i+1, n):
            summ = summ + aug[i,r]*x_sol[r]
        x_sol[i] = (aug[i,n] - summ)/aug[i,i]

    print()
    print('the solutions are')
    print(x_sol)

    return aug





choices = {'1':'6a', '2':'6b', '3':'6c', '4':'6d', '5':'add1', '6':'add2'}
user_in = input("Select problem: ")
if user_in in choices:
    if user_in == '1':
        #6a.
        n = 3
        d = np.array([[0,1,-2],[1,-1,1],[1,0,-1]])
        x = np.array([[4],[6],[2]])
    elif user_in == '2':
        #6b.
        n = 4
        d = np.array([[1,-1/2,1,0],[2,-1,-1,1],[1,1,1/2,0],[1,-1/2,1,1]])
        x = np.array([[4],[5],[2],[5]])
    elif user_in == '5':
        # additional problem
        n = 10
        d = create_matrix(n)
        x = create_vec(n)
    else:
        # additional problem
        n = 100
        d = create_matrix(n)
        x = create_vec(n)

    augmented = gaussian_sub(d, x, n)
    print(augmented)    














