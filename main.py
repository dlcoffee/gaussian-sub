import numpy as np
import copy
import sys

np.set_printoptions(linewidth=200, precision=6)

def create_matrix(n):
    mat = np.empty([n,n], dtype=float)
    for i in range(0, n):
        for j in range(0, n):
            if i == j:
                mat[i,j] = 1
            else:
                mat[i,j] = 1/(i + j)**2
    return mat

def create_vec(n):
    vec = np.empty([n,1], dtype=float)
    for i in range(0,n):
        vec[i,0] = i+1

    return vec


'''
test = create_matrix(n)
print(test)

v = create_vec(n)
print(v)
'''

#d = np.array([[1,1,0,1],[2,1,-1,1],[-1,2,3,-1],[3,-1,-1,2]])
#x = np.array([[2],[1],[4],[-3]])
#n = 4

#6a.
#d = np.array([[0,1,-2],[1,-1,1],[1,0,-1]])
#x = np.array([[4],[6],[2]])
#n = 3

#6b.
d = np.array([[1,-1/2,1,0],[2,-1,-1,1],[1,1,1/2,0],[1,-1/2,1,1]])
x = np.array([[4],[5],[2],[5]])
n = 4


def gaussian_sub(x, y, n):
    aug = np.concatenate((x, y), -1)
    found_p = False
    print('your augmented matrix: ')
    print(aug)

    for i in range(0, n):
        # find p
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

#augmented = gaussian_sub(test,v, n)
augmented = gaussian_sub(d, x, n)
print(augmented)
