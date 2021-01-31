import time
import random 

sentences = ['The quick brown fox jumps over the lazy dog',"The duckling's questionable mum and pet zebra skydived out of an expensive jet which crashed but that is pretty boring","The July sun oused a fragment of black pine waxto ooze on the velvet quilt","Jaded zombies acter quaintly but kept driving their oxen forward","Sixty zippers were quickly picked from the woven jute bag","Heavy boxes perform quick waltzes and jigs","The five boxing wizards jump quickly",]
string = random.choice(sentences)
word_count = len(string.split())

st = time.time()
inputText = input('Enter the phrase: "%s" as fast as possible:\n'% string )
et = time.time()
acc = len(set(inputText.split()) & set(string.split()))
acc = acc/word_count*100
timeTaken = et - st
WPM = (word_count/timeTaken)*100
WPM = round(WPM)
print('\n')
print(f'{WPM} WPM \n {acc}% accuracy')
