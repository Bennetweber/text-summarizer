from summarizer import Smmry
import io
import io

#paste the directory of your text document here
text = io.open('example-text.txt', 'r', encoding='utf-8').read()
smmry = Smmry(text, lang="english")
summarized_sentence = smmry.summarize(length=2)

print(summarized_sentence)
