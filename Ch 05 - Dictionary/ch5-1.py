dict = {
    'pace': "in a faster manner",
    'prag': "a runner",
    'marks': [1, 5, 29],
    'moreDict': {"Bill": 'Swimmer'}
}
print("pace: ", dict['pace'])
print("Prag: ", dict['prag'])
print('marks: ', dict['marks'])
# print('Bill: ', dict['moreDict'])
print('Bill: ', dict['moreDict']["Bill"])
dict["Marks"] = [56, 75, 34]
print('marks: ', dict['Marks'])