from equiter.data.set1 import parameters
from equiter.src.main import Equiter
from equiter.src.core.view import View

# Przewidywane wyniki dla podanego zestawu danych
# x0: [0.0000, 0.0000, 0.0000]
# x1: [0.5000, 1.5000, 0.5000]
# x2: [0.8750, 1.7500, 0.8750]
# x3: [0.9375, 1.9375, 0.9375]
# x4: [0.9844, 1.9688, 0.9844]

print("##### Metoda stacjonarna - Jacobi - Przykład 1")

View.showMatrix(parameters.A)

Equiter.solve(method='jacobi', parameters=parameters, visualize=True)
