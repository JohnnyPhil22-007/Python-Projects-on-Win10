from tkinter import *
from tkinter import messagebox
import random
import time

root = Tk()
root.geometry('400x210')
root.title('Typing Test')

word_list = ['a', 'able', 'about', 'above', 'across', 'add', 'after', 'again', 'against', 'ago', 'air', 'all', 'almost', 'alone', 'along', 'already', 'also', 'although', 'always', 'am', 'American', 'among', 'an', 'and', 'animal', 'animals', 'another', 'answer', 'any', 'anything', 'are', 'area', 'around', 'as', 'asked', 'at', 'away', 'back', 'ball', 'be', 'beautiful', 'became', 'because', 'become', 'been', 'before', 'began', 'begin', 'behind', 'being', 'below', 'bet', 'better', 'between', 'big', 'black', 'blue', 'boat', 'body', 'book', 'both', 'bottom', 'box', 'boy', 'bring', 'brought', 'build', 'built', 'but', 'by', 'called', 'came', 'can', 'can\'t', 'cannot', 'car', 'care', 'carefully', 'carry', 'center', 'certain', 'change', 'check', 'children', 'city', 'class', 'close', 'cold', 'come', 'common', 'complete', 'could', 'country', 'course', 'cut', 'dark', 'day', 'deep', 'did', 'didn\'t', 'different', 'distance', 'do', 'does', 'dog', 'don\'t', 'done', 'door', 'down', 'draw', 'dry', 'during', 'each', 'early', 'earth', 'easy', 'eat', 'either', 'else', 'end', 'English', 'enough', 'even', 'ever', 'every', 'everyone', 'everything', 'example', 'face', 'fact', 'fall', 'family', 'far', 'fast', 'father', 'feel', 'feet', 'felt', 'few', 'field', 'finally', 'find', 'fine', 'fire', 'first', 'fish', 'five', 'floor', 'follow', 'food', 'foot', 'for', 'form', 'found', 'four', 'friend', 'from', 'front', 'full', 'game', 'gave', 'get', 'girl', 'give', 'glass', 'go', 'going', 'gold', 'gone', 'good', 'got', 'great', 'green', 'ground', 'group', 'grow', 'had', 'half', 'hand', 'happened', 'hard', 'has', 'have', 'he', 'head', 'hear', 'heard', 'heart', 'heavy', 'held', 'help', 'her', 'here', 'high', 'him', 'himself', 'his', 'hold', 'home', 'horse', 'hot', 'hour', 'house', 'how', 'however', 'hundred', 'I', 'I\'ll', 'I\'m', 'ice', 'idea', 'if', 'important', 'in', 'inside', 'instead', 'into', 'is', 'it', 'it\'s', 'its', 'itself', 'job', 'just', 'keep', 'kept', 'kind', 'knew', 'know', 'land', 'language', 'large', 'last', 'later', 'lay', 'learn', 'learned', 'least', 'leave', 'leaves', 'left', 'less', 'let', 'letter', 'life', 'light', 'like', 'line', 'list', 'little', 'live', 'lived', 'living', 'long', 'longer', 'look', 'low', 'made', 'main', 'make', 'man', 'many', 'map', 'matter', 'may', 'me', 'mean', 'men', 'might', 'mind', 'miss', 'money', 'moon', 'more', 'morning', 'most', 'mother', 'move', 'much', 'must', 'my', 'name', 'near', 'need', 'never', 'new', 'next', 'night', 'no', 'not', 'nothing', 'notice', 'now', 'number', 'of', 'off', 'often', 'oh', 'old', 'on', 'once', 'one', 'only', 'open', 'or', 'order', 'other', 'our', 'out', 'outside', 'over', 'own', 'page', 'paper', 'part', 'past', 'pattern', 'people', 'perhaps', 'person', 'picture', 'piece', 'place', 'plants', 'play', 'point', 'poor', 'possible', 'power', 'probably', 'problem', 'put', 'question', 'quite', 'rain', 'ran', 'read', 'ready', 'real', 'really', 'red', 'remember', 'rest', 'right', 'river', 'road', 'rock', 'room', 'round', 'run', 'sad', 'said', 'same', 'sat', 'saw', 'say', 'school', 'sea', 'second', 'see', 'seen', 'sentence', 'set', 'several', 'shall', 'she', 'ship', 'short', 'should', 'show', 'shown', 'side', 'simple', 'since', 'six', 'size', 'sky', 'small', 'snow', 'so', 'some', 'someone', 'something', 'soon', 'sound', 'space', 'special', 'stand', 'start', 'state', 'stay', 'still', 'stood', 'stop', 'story', 'strong', 'study', 'such', 'suddenly', 'summer', 'sun', 'sure', 'surface', 'system', 'table', 'take', 'talk', 'tall', 'tell', 'ten', 'than', 'that', 'that\'s', 'the', 'their', 'them', 'themselves', 'then', 'there', 'these', 'they', 'thing', 'think', 'third', 'this', 'those', 'though', 'thought', 'three', 'through', 'time', 'tiny', 'to', 'today', 'together', 'told', 'too', 'took', 'top', 'toward', 'town', 'tree', 'true', 'try', 'turn', 'turned', 'two', 'under', 'understand', 'United States', 'until', 'up', 'upon', 'us', 'use', 'usually', 'very', 'voice', 'walk', 'walked', 'want', 'warm', 'was', 'watch', 'water', 'way', 'we', 'weather', 'well', 'went', 'were', 'what', 'when', 'where', 'whether', 'which', 'while', 'white', 'who', 'whole', 'why', 'wide', 'wild', 'will', 'wind', 'winter', 'with', 'within', 'without', 'words', 'work', 'world', 'would', 'write', 'year', 'yes', 'yet', 'you', 'young', 'your']

new_timer = 60

def start():
    global new_timer
    for i in range(60):
        new_timer -= 1
        time.sleep(1)
        timer.configure(text=new_timer)
        continue

    if len(display_word) == len(input_word):
        display_word.configure(
            text=word_list[random.randint(0, len(word_list))])

heading = Label(root, text='Typing Test', font=('Arial', 20, ''), justify=CENTER)
heading.place(x=126, y=0)

timer = Label(root, text='60', font=('Arial', 14, ''), justify=CENTER)
timer.place(x=187, y=40)

display_word = Label(root, width=20, text=word_list[random.randint(0, len(word_list))], font=('Arial', 14, ''), justify=CENTER)
display_word.place(x=87, y=70)

input_word = Entry(root, width=10, font=('Arial', 14, ''), justify=CENTER)
input_word.place(x=145, y=100)

timer_start = Button(root, text='Set Timer', font=('Arial', 12, ''), bd=5, command=start)
timer_start.place(x=157, y=128)

statistics = Label(root, width=25, text='WPM:\tAccuracy:\t', font=('Arial', 14, ''), justify=CENTER)
statistics.place(x=60, y=170)

root.mainloop()