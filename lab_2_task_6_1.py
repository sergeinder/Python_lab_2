with open("article_rus.txt", encoding="utf8") as file:
    text = file.read()

total_counter = 0
alphabet = "аАбБвВгГдДеЕёЁжЖзЗиИйЙкКлЛмМнНоОпПрРсСтТуУфФхХцЦчЧшШщЩъЪыЫьЬэЭюЮяЯ"
result = {}

for i in range(0, len(alphabet), 2):
    result[alphabet[i]] = text.count(alphabet[i]) + text.count(alphabet[i + 1])
    total_counter += result[alphabet[i]]

for key in result:
    result[key] = result[key] / total_counter

with open("article_rus_solve.txt", "w") as file:
    for key in result:
        file.write(key + " - " + str(result[key])[:6] + "\n")
