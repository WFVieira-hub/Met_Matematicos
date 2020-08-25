def Lista(nn):
  y=[] # Lista dentro de outra lista
  for i in range(nn):
    x=[] # reinia a lista x para cada novo elemento i
    for j in range(nn):
      x.append(j)
    y.append(x)
  return y
