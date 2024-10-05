
[![MyTests](https://github.com/Illialla/TestingLab/actions/workflows/test-action.yml/badge.svg)](https://github.com/Illialla/TestingLab/actions/workflows/test-action.yml/badge.svg)
[![Coverage Status](https://coveralls.io/repos/Illialla/TestingLab/badge.svg?branch=main)](https://coveralls.io/github/Illialla/TestingLab?branch=main)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Illialla_TestingLab&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Illialla_TestingLab)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=Illialla_TestingLab&metric=bugs)](https://sonarcloud.io/summary/new_code?id=Illialla_TestingLab)
[![Code smells](https://sonarcloud.io/api/project_badges/measure?project=Illialla_TestingLab&metric=code_smells)](https://sonarcloud.io/dashboard?id=Illialla_TestingLab)
## План тестирования
| Тест |                                  Описание                                   |     Входные данные     |              Ожидаемый результат            |
|:----:|:---------------------------------------------------------------------------:|:----------------------:|:-------------------------------------------:|
|  1   | Тестирование с положительным дискриминантом (два разных вещественных корня) |     a=1, b=5, c=6      |             x1 = -2.0, x2 = -3.0            |
|  2   |      Тестирование с нулевым дискриминантом (один вещественный корень)       |     a=1, b=2, c=1      |             x1 = -1.0, x2 = -1.0            |
|  3   |     Тестирование с отрицательным дискриминантом (два комплексных корня)     |     a=1, b=2, c=5      |          x1 = -1 + 2j, x2 = -1 - 2j         |
|  4   |                   Тестирование с нулевыми коэффициентами                    |     a=0, b=2, c=3      | Ошибка (поскольку деление на ноль невозможно) |
|  5   |                 Тестирование с одним нулевым коэффициентом                  |     a=1, b=0, c=-4     |              x1 = 2.0, x2 = -2.0            |
|  6   |                Тестирование с отрицательными коэффициентами                 |    a=-1, b=-4, c=-4    |              x1 = -2.0, x2 = 2.0            |
|  7   |                    Тестирование с очень большими числами                    | a=10^6, b=10^6, c=10^6 |  Проверить, что функция работает без ошибок |
|  8   |               Тестирование с недостаточным числом аргументов                |        a=1, b=2        |     Проверить, что функция выдаёт ошибку    |
|  9   |                   Тестирование с неверным типом аргумента                   |    a="a", b=1, c=2     |    Проверить, что функция выдаёт ошибку     |