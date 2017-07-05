import math;
import random;

#Question 1
def is_divisible(m, n):
    return not(m % n);

#Question 2
def yikes(x):
    return ((x * math.exp(-x)) + (math.sqrt(1 - math.exp(-x))));

#Question 3
def roots(a, b, c):
    D = math.pow(b, 2) - (4 * a *c);
    if(D >= 0):
        alpha = float(((-b) + math.sqrt(D)) / (2 * a));
        beta = float(((-b) - math.sqrt(D)) / (2 * a));
    else:
        D = -D;
        alpha = complex(float((-b) / (2 * a)), float(math.sqrt(D)) / (2 * a));
        beta = complex(float((-b) / (2 * a)), float(-math.sqrt(D)) / (2 * a));
        print alpha, beta;

#Question 4
def CGPA(n, credits, gpa):
    cgpa = 0;
    for i in range(n):
        cgpa = cgpa + (credits[i] * gpa[i]);
    cgpa = float(cgpa) / sum(credits);
    if cgpa < 5:
        print "sed_lyf";
    elif cgpa > 9:
        print "GGWP";
    print cgpa;

#Question 5
def roll_dice(n, m):
    if n < 4:
        print "error in number of sides";
        return False;
    for i in range(m):
        print random.randint(1, m);
    return "That's all";

#Question 6
def pygLatin_word(string):
    string.lower();
    string = list(string);
    vowels = ['a', 'e', 'i', 'o', 'u'];
    if(string[0] in vowels):
        string = ''.join(string);
        string = string + 'hay';
    else:
        string.append(string[0]);
        for i in range(0, len(string) - 1):
            string[i] = string[i + 1];
        string.pop();
        string = ''.join(string);
        string = string + 'ay';
    return string;

def pygLatin_sentence(string0):
    string0 = string0.split(' ');
    for i in range(len(string0)):
        print string0[i],
        print pygLatin_word(string0[i]);

def pygLatin_paragraph(string1):
    string1 = string1.split('.');
    for i in range(len(string1)):
        print pygLatin_sentence(string1[i]),
print pygLatin_sentence("i am madabhooshi padmanabha srinivasan");
    
    
