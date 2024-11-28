import re
from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

# Завантажити список стоп-слів
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

with open('carroll-alice.txt', 'r') as file:
    text = file.read().lower()

# Видалення пунктуації та поділ тексту на слова
words = re.findall(r'\b\w+\b', text)

# Визначення кількості слів у тексті
word_count = len(words)
print(f"Кількість слів у тексті: {word_count}")

# Обчислення найбільш вживаних слів без стоп-слів
filtered_words = [word for word in words if word not in stop_words]
word_counts = Counter(filtered_words)

# Визначення 10 найбільш вживаних слів
most_common_words = word_counts.most_common(10)
print("10 найбільш вживаних слів:")
for word, count in most_common_words:
    print(f"{word}: {count}")

# Побудова стовпчастої діаграми для найбільш вживаних слів
words, counts = zip(*most_common_words)
plt.figure(figsize=(10, 6))
plt.bar(words, counts, color='skyblue')
plt.title('10 найбільш вживаних слів')
plt.xlabel('Слова')
plt.ylabel('Кількість вживань')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()