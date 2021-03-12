import numpy
import math
import matplotlib.pyplot as plot
import random

# Declarando e atribuindo as variaveis necessarias
N = 50000   # Quantidade de interações por realização
V = 100      # Quantidade de realizações
np = 0.01   # Potencia do ruido
sp = 1      # Potencia do sinal ou seja 20dB = 1
mu = 0.005  # Tamanho do passo

# Resposta do Impulso Desconhecido
h = numpy.array([0.0098, -0.0143, -0.0251, -0.0399, -0.0518, -0.0619, -0.0709, -0.0781, -0.0834, -0.0869, -0.0886, -0.0886, -0.0869, -0.0836, -0.0789, -0.0729, -0.0657, -0.0576, -0.0488, -0.0394, -0.0297, -0.0198, -0.0100, -0.0004, 0.0088, 0.0175, 0.0254, 0.0325, 0.0387, 0.0439, 0.0480, 0.0510, 0.0530, 0.0538, 0.0536, 0.0524, 0.0503, 0.0473, 0.0435, 0.0391, 0.0341, 0.0287, 0.0230, 0.0172, 0.0112, 0.0053, -0.0004, -0.0059, -0.0110, -0.0157, -0.0199, -0.0236, -0.0266, -0.0290, -0.0307, -0.0318, -0.0322, -0.0320, -0.0312, -0.0299, -0.0280, -0.0257, -0.0231, -0.0201, -0.0168, -0.0134, -0.0099, -0.0064, -0.0029, 0.0005, 0.0037, 0.0067, 0.0095, 0.0119, 0.0140, 0.0158, 0.0171, 0.0181, 0.0187, 0.0190, 0.0188, 0.0183, 0.0175, 0.0164, 0.0150, 0.0135, 0.0117, 0.0098, 0.0078, 0.0058, 0.0037, 0.0017, -0.0003, -0.0022, -0.0039, -0.0055, -0.0069, -0.0081, -0.0091, -0.0099, -0.0105, -0.0108, -0.0109, -0.0109, -0.0106, -0.0101, -0.0095, -0.0087, -0.0078, -0.0068, -0.0057, -0.0045, 0.0034, -0.0022, -0.0010, 0.0001, 0.0012, 0.0022, 0.0031, 0.0039, 0.0046, 0.0051, 0.0056, 0.0059, 0.0061, 0.0062, 0.0062, 0.0060, 0.0057, 0.0054, 0.0049, 0.0044, 0.0039, 0.0033, 0.0026, 0.0020, 0.0013, 0.0007, 0.0000, -0.0006, -0.0011, -0.0016, -0.0021, -0.0025, -0.0028, -0.0031, -0.0033, -0.0034, -0.0034, -0.0034])
#h = numpy.array([0.5, 1, 1.2, 1.5, 2])
# Definição das matrizes que irão guardar os dados de todas as realizações
E = numpy.zeros((N+1), dtype=float)        # Erro media de todas as realizações
W = numpy.zeros((len(h), N+2), dtype=float)   # W medio de todas as realizações
X = numpy.zeros((len(h), N + len(h)), dtype=float)        # X medio de todas as realizações
x = numpy.zeros((N + len(h)), dtype=float)
zx = numpy.zeros((N + len(h)), dtype=float) #Numeros Randomicos
zr = numpy.zeros((N + len(h)), dtype=float) #Numeros Randomicos

# Definição para poder controlar a posição dos dados nos vetores e matrizes
for _ in range(V):
    cont = 0
    for _ in range(N + len(h)):  # Criar vetor com numero randomico
        zx[cont] = random.random()
        cont = cont + 1
    cont = 0
    for _ in range(N + len(h)):  # Criar vetor com numero randomico
        zr[cont] = random.random()
        cont = cont + 1
    cont = 0
    # Definir e zerar os vetores e matrizes
    w = numpy.zeros((len(h), N+2), dtype=float)
    y = numpy.zeros((N+1), dtype=float)
    e = numpy.zeros((N+1), dtype=float)
    d = numpy.zeros((N+1), dtype=float)
    aux = numpy.zeros((N+1), dtype=float)
    x = math.sqrt(sp) * zx
    print(x)
    D = numpy.convolve(x, h)
    d = D[:len(zr)] + math.sqrt(np) * zr
    i=0
    for _ in range(len(h)):
        X[i, :N+len(h) - i] = x[i:N+len(h)]
        i = i + 1
        #X[0][:] = x[0:N + 1]
        #X[1][:] = x[1:N + 2]
    cont = 0
    #for _ in range(N + 1):
    #    X[0][cont + 1] = x[cont + 1]
     #   X[1][cont] = X[0][cont + 1]
    #Inicio do filtro
    #w = numpy.array([[i][i]])
    #y[i] = numpy.dot(numpy.transpose(w[:][i]), X[:][i])
    #e[i] = d[i] - y[i]
    #w[:][i+1] = w[:][i] + 2 * mu * e[i] * X[:][i]
    i=0
    for _ in range(N):
        auxt = numpy.transpose(w)
        #print(X[:][1])
        #print(X[1][1])
        y[i] = numpy.dot(auxt[i, :], X[:, i])
        e[i] = d[i] - y[i]
        w[:, i+1] = w[:, i] + 2 * mu * e[i] * X[:, i]
        i = i + 1
    W = W + w/V
    es = e*e
    E = E + es/V
# Vetor para a plotagem
W = W[:, :-1]
E = E[:-1]
#Edb = 10*numpy.log(E)
n = numpy.arange(N+1)
#PLOTAGEM
plot.plot(n, W[0], color="blue")
plot.plot(n, W[10], color="orange")
#plot.plot(n, W[2], color="red")
#plot.plot(n, W[3], color="green")
#plot.plot(n, W[4], color="yellow")
plot.plot(n, W[40], color="red")
plot.plot(n, W[60], color="green")
plot.plot(n, W[100], color="yellow")
plot.axis([1, N+N/10, min(W[0] - 1, key=float), max(W[100] + 1, key=float)])
plot.grid()
plot.ylabel("E(w[n])", fontsize = 20)
plot.xlabel("Numero de interações", fontsize = 20)

m = numpy.arange(N)
plot.figure(2)
plot.plot(m, E)
plot.axis([1, N+N/10, 0, max(E, key=float)])
plot.grid()
plot.yscale("log")
plot.ylabel("MSE", fontsize = 20)
plot.xlabel("Numero de interações", fontsize = 20)

plot.show()