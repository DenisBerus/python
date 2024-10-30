#Четвертый семинар
"""
import pandas as pd
import random
# Генерация DataFrame
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})
# Создание one-hot кодирования
unique_values = data['whoAmI'].unique() # Находим уникальные
значения
one_hot = pd.DataFrame()
for value in unique_values:
one_hot[value] = (data['whoAmI'] == value).astype(int)
# Объединение one-hot кодирования с исходным DataFrame (опционально)
data = pd.concat([data, one_hot], axis=1)
print(data.head())
"""


"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Загрузка данных
df = pd.read_csv('data.csv')
# Проверка названий столбцов
print(df.columns)
sns.lineplot(x='age', y='spending_score', data=df)
plt.title('Age vs Spending Score')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.show()
"""


"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Загрузка данных из CSV-файла
df = pd.read_csv('data.csv')
# Создание точечного графика с использованием Seaborn
# Ось X: зарплата (salary)
# Ось Y: бонусы (bonus)
# Размер точек пропорционален количеству лет в компании (years_at_company)
sns.scatterplot(x='salary', y='bonus', size='years_at_company', data=df)
# Настройка заголовка графика
plt.title('Salary vs Bonus with Years at Company')
# Настройка меток осей
plt.xlabel('Salary')
plt.ylabel('Bonus')
# Отображение графика
plt.show()
"""
