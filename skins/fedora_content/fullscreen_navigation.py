request = container.REQUEST
RESPONSE = request.RESPONSE

def pad(base):
    x = base.split('_')
    try:
        return "%02d_%03d" % (int(x[0]), int(x[1]))
    except:
        return "XXX"

#this_letter = pad(context.id.split('.')[0])
this_letter = context.id.split('.')[0]

letters = []
navigation = {}

for doc in context.contentValues('FedoraDocument'):
    x = doc.id.split('.')
    base = x[0]
    #base = pad(base)
    ext = x[-1]
    if ext == 'html':
        letters.append(base)
        navigation[base] = doc


letters.sort()

#for letter in letters:
#    navigation[letter]['index'] = letters.index(letter)

this_no = letters.index(this_letter)
next_no = this_no + 1
previous_no = this_no -1
this = context
first = navigation[letters[0]]    
last = navigation[letters[-1]]    

if not previous_no < 0:
    previous = navigation[letters[previous_no]]
else:
    previous = None

if not next_no > len(letters) - 1:
    next = navigation[letters[next_no]] 
else:
    next = None
nav = {
    'this': this,
    'next': next,
    'previous':previous,
    'first': first,
    'last':last
    }
return nav

