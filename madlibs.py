word_list = list()
from termcolor import colored

def madLibs():

    object = input("Enter an object: ")
    word_list.append(object)
    noun1 = input("Enter a noun(person or thing): ")
    word_list.append(noun1)
    noun2 =input("Enter a noun: ")
    word_list.append(noun2)
    plural_noun = input("Enter a plural noun: ")
    word_list.append(plural_noun)
    noun4 = input("Same noun without plural: ")
    word_list.append(noun4)
    place = input("Enter a place: ")
    word_list.append(place)
    number = input("Enter a number: ")
    word_list.append(number)
    number2 = input("Enter a number: ")
    word_list.append(number2)
    length_of_time = input("Enter in a length of time: ")
    word_list.append(length_of_time)
    length_of_time_2 = input("Enter in a length of time: ")
    word_list.append(length_of_time_2)
    verb = input("Enter a verb: ")
    word_list.append(verb)
    adjective = input("Enter a adjective: ")
    word_list.append(adjective)
    adjective2 = input("Enter a adjective: ")
    word_list.append(adjective2)
    body_part = input("Enter a part of the body: ")
    word_list.append(body_part)
    emotion = input("Enter a emotion: ")
    word_list.append(emotion)
    object2 = input("Enter a object: ")
    word_list.append(object2)

madLibs()
print("There once was a little boy whose name was Johnny and had always lost his " + colored(word_list[0],'red') + ".")
print("His " + colored(word_list[1],'cyan') + " gave him a bag of " + colored(word_list[3],'yellow') + " and told him that every time he lost his " + colored(word_list[0],'red') + ", he must hammer a " + colored(word_list[3],'yellow')  + " into the back of a " + colored(word_list[5],'green') + ".")
print("The first day, the boy had driven " + colored(word_list[6],'magenta') + " " + colored(word_list[4],'grey') + " into the " + colored(word_list[5],'green') + ".")
print("Over the next few " + colored(word_list[8],'magenta') + ", as he learned to control his " + colored(word_list[0],'red') + " the number of " + colored(word_list[3],'yellow') + " hammered daily gradually dwindled down.")
print("He discovered it was easier to " + colored(word_list[10],'yellow') + " his " + colored(word_list[0],'red') + " than to drive those " + colored(word_list[3],'yellow') + " into the " + colored(word_list[5],'green') + ".")
print("Finally the day came when the boy didn't lose his " + colored(word_list[0],'red') + " at all.")
print("He told his " + colored(word_list[1],'cyan') + " about it and the " + colored(word_list[1],'cyan') + " suggested that the boy now ")
print( colored(word_list[10],'green') + " " + colored(word_list[7],'magenta') + " " + colored(word_list[2], 'yellow') + " for each day that he was able to hold his " + colored(word_list[1],'cyan'))
print("The " + word_list[8] + " passed and the boy was finally able to tell his " + colored(word_list[1],'cyan') + " that all the " + colored(word_list[3],'yellow') + " were " + colored(word_list[11],'green') + ".")
print("The " + colored(word_list[1],'cyan') + " took him by the " + colored(word_list[13],'cyan') + " and led him to the " + colored(word_list[5],'green') + ".")
print("He said, You have done " + colored(word_list[13],'green') + " , Johnny, but look at the holes in the " + colored(word_list[5],'green') + ". The " + colored(word_list[5],'green') + " will never be the same.")
print("When you say things in " + colored(word_list[14],'yellow') + ", they leave a scar just like this one.")
print("You can put a " + colored(word_list[15],'red') + " in a man and draw it out. It wont matter how many times you say I'm sorry. The " + colored(word_list[15],'magenta') + " is still there.")
