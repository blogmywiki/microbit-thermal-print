# program for BBC micro:bit to print  on a thermal printer 
# a random poem when you press button A
# or a random Christmas cracker joke when you press button B
# based on The Little Box of Poems by @blogmywiki / Giles Booth

import microbit
import random

microbit.uart.init(baudrate=19200, bits=8, parity=None, stop=1, tx=microbit.pin8, rx=None)

def normal_print(msg):
    microbit.uart.write(msg+"\x0A\x0A")

def wide_print(msg):
    microbit.uart.write("\x1B\x0E"+msg+"\x0A\x0A\x1B\x14")

def big_print(msg):
    microbit.uart.write("\x1D\x211"+msg+"\x0A\x0A\x1D\x210")
    
def bold_print(msg):
    microbit.uart.write("\x1B\x451"+msg+"\x0A\x0A\x1B\x450")

def inverse_print(msg):
    microbit.uart.write("\x1D\x421"+msg+"\x0A\x0A\x1D\x420")
    
def print_barcode(msg):
    microbit.uart.write("\x1D\x6B\x43\x0D"+msg+"\x0A\x0A")

poemtitle = ['In a station of the Metro', 'The Sick Rose', 'This is just to say', 'Surprise']

poemtext = ['The apparition of these faces in the crowd;\n\
Petals on a wet, black bough.', 'O Rose thou art sick.\n\
The invisible worm,\n\
That flies in the night\n\
In the howling storm:\n\n\
Has found out thy bed\n\
Of crimson joy:\n\
And his dark secret love\n\
Does thy life destroy.', 'I have eaten\n\
the plums\n\
that were in\n\
the icebox\n\n\
and which\n\
you were probably\n\
saving\n\
for breakfast\n\n\
Forgive me\n\
they were delicious\n\
so sweet\n\
and so cold', 'I lift the toilet seat\n\
as if it were the nest of a bird\n\
and i see cat tracks\n\
all around the edge of the bowl.']

poemauthor = ['Ezra Pound\n', 'William Blake\n', 'William Carlos Williams\n', 'Richard Brautigan\n']

joke_question = ['Why are Christmas trees so bad\nat sewing?\n', 
'Why did the turkey join\nthe band?\n', 
'What song do you sing at a\nsnowman\'s birthday party?\n', 
'Which famous playwright was\nterrified of Christmas?\n']

joke_answer = ['They always drop their needles!\n','Because it had\nthe drumsticks\n','Freeze a jolly\ngood fellow\n','Noel Coward!\n']

# increase printing temperature - increase hex number A0 for darker print
microbit.uart.write("\x1B\x37\x07\xFF\xFF")

microbit.display.scroll("Press <A for poem B> for joke", delay=150, wait=False, loop=True, monospace=False)

while True:
    if microbit.button_a.is_pressed():
        poem = random.randrange(0,4)
        wide_print(poemtitle[poem])
        normal_print(poemtext[poem])
        inverse_print(poemauthor[poem])
    elif microbit.button_b.is_pressed():
        joke = random.randrange(0,4)
        wide_print("I say, I say, I say...")
        normal_print(joke_question[joke])
        wide_print(joke_answer[joke])   
    microbit.sleep(200)
    
  
