from typing import Tuple
import math
from scipy import stats


# Оценочные параметры
def estimated_parameters(N: int, n: int) -> Tuple[float, float]:
    p = n / N
    sigma = math.sqrt(p * (1 - p) / N)
    return p, sigma


# Проверка нулевой гипотезы о том, что Pa и Pb являются одинаковыми
def a_b_test_statictic(N_A: int, n_A: int, N_B: int, n_B: int) -> float:
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A) / math.sqrt(sigma_A ** 2 + sigma_B ** 2)

# Рассчитываем z
# Реклама "А" получает 200 откликов на 1000 просмотров, реклама "В" 180 на 1000
z_value = a_b_test_statictic(1000, 200, 1000, 180)
print(z_value)

# Рассчитываем p
distr = stats.norm(0, 1)
p_value = (1 - distr.cdf(abs(z_value))) * 2
print('p-значение: ', p_value)

alpha = .05
if (p_value < alpha):
    print("Отвергаем нулевую гипотезу: между долями есть значимая разница")
else:
    print("Не получилось отвергнуть нулевую гипотезу, нет оснований считать доли разными")
