import numpy as np
import scipy.linalg
import warnings


class Rho():

    def __init__(self):
        warnings.filterwarnings("ignore")

    def set_debruijn_G(self, q):
        G = np.zeros((q**2, q**2))
        for i in range(q):
            for j in range(q):
                for k in range(q):
                    G[j+q*i, k+q*j] = 1
        for n in range(q - 1):
            G[q*(q-1)+n, q*(n+1)-1] = 0
        return G

    def asym_freq_of_trans(self, G):
        # Compute the dominant eigenvalue and its corresponding left and right eigenvectors
        values, left, right = scipy.linalg.eig(G, right=True, left=True)
        lambda_1 = max(np.linalg.eigvals(G))

        V_l = 0
        V_r = 0

        for i in range(len(values)):

            if values[i] == lambda_1:
                V_l = left[:, i]
                V_r = right[:, i]

        T = np.zeros((len(V_l), len(V_r)))

        for s in range(len(V_l)):
            for t in range(len(V_r)):
                T[s, t] = V_l[s] * G[s, t] * V_r[t]

        result = T/np.sum(T)
        return result

    def get_freq(self, result, q):
        sum = 0
        for i in range(q):
            for j in range(q):
                sum += result[i*q+j, q*(j+1)-1]
        return sum

    def get_table(self, size):
        table = {}
        for q in range(2, size+1):
            table.update({q: self.main(q)})
        return table

    def main(self, q):
        G = self.set_debruijn_G(q)
        result = self.asym_freq_of_trans(G)
        sum = round(self.get_freq(result, q), 6)
        return sum


if __name__ == "__main__":
    print "Please input q"
    q = int(raw_input())
    print Rho().main(q)
