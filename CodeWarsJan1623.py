# Who remembers back to their time in the schoolyard, when girls would take a flower and tear its petals, saying each of the following phrases each time a petal was torn:
# "I love you"
# "a little"
# "a lot"
# "passionately"
# "madly"
# "not at all"
# If there are more than 6 petals, you start over with "I love you" for 7 petals, "a little" for 8 petals and so on.
# When the last petal was torn there were cries of excitement, dreams, surging thoughts and emotions.
# Your goal in this kata is to determine which phrase the girls would say at the last petal for a flower of a given number of petals. The number of petals is always greater than 0.

def how_much_i_love_you(nb_petals):
    petals  = nb_petals % 6
    if petals == 0:
        return 'not at all'
    elif petals == 1:
        return "I love you"
    elif petals == 2:
        return "a little"
    elif petals == 3:
        return "a lot"
    elif petals == 4:
        return "passionately"
    elif petals == 5:
        return "madly"
    elif petals == 6:
        return "not at all"

# Nathan loves cycling.
# Because Nathan knows it is important to stay hydrated, he drinks 0.5 litres of water per hour of cycling.
# You get given the time in hours and you need to return the number of litres Nathan will drink, rounded to the smallest value.
# For example:
# time = 3 ----> litres = 1
# time = 6.7---> litres = 3
# time = 11.8--> litres = 5

def litres(time):
    water_drank = time * 0.5
    return int(water_drank)