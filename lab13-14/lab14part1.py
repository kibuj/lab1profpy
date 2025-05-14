import matplotlib.pyplot as plt
from collections import Counter
import string

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read().lower()

letters_only = [char for char in text if char in string.ascii_lowercase]

counts = Counter(letters_only)

plt.figure(figsize=(10, 5))
plt.bar(counts.keys(), counts.values(), color='skyblue')
plt.xlabel("Літери")
plt.ylabel("Частота")
plt.title("Гістограма частоти появи літер у тексті")
plt.grid(axis='y')


plt.savefig("letter_histogram.png")
plt.show()
