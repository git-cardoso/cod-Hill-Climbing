from numpy import asarray
from numpy.random import randn
from numpy.random import rand


point1 = [1,5]
point2 = [6,4]
point3 = [5,2]
point4 = [2,1]

def objective(x):

    return x[0]**2.0

limite = asarray([[-5.0, 5.0]])
step_size = 0.1
solucao = limite[:, 0] + rand(len(limite)) * (limite[:, 1] - limite[:, 0])
avaliacao_solucao = objective(solucao)
solucoes = []

solucoes+=[solucao]
for i in range(0,1000):
  candidato = solucao + randn(len(limite)) * step_size
  avaliacao_candidato = objective(candidato)
  if avaliacao_candidato <= avaliacao_solucao:
     solucao, avaliacao_solucao = candidato, avaliacao_candidato
     solucoes = solucoes + [solucao]
     print(i, solucao, avaliacao_solucao)
  else:
     print(solucao, avaliacao_solucao, solucoes)
