def jungle_animal(animal, my_speed):
    # YOUR CODE HERE
    if animal == 'zebra':
        print "Try to ride a zebra!"
    elif animal == 'cheetah' and my_speed>115:
        print "Run!"
    elif animal == 'cheetah' and my_speed<=115:
        print "Stay calm and wait!"
    else:
        print "Introduce yourself!"
