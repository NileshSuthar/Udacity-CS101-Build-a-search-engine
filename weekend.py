def weekend(day):
    # your code here
    if(day == 'Sunday' or day == 'Saturday'):
        return True
    else:
        return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False
