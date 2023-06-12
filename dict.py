data = {
    'Vazgen': 320000,
    'July': 2500,
    'Simon': 3500
}

data.update({
    'Vazgen': 5000, 
    'July': 10000
             })

# # print(data['July'])
# data['July'] = 3500
# print(data)
print(data.keys())
print(data.values())
# ----------------------------------------------------------------------



data2 = {
    'boys':['Arman', 'Vazgen', 'Karen'],
    'girls': ['Anna', 'Ani', 'Armine']

}
# print(data2['girls'])
# print(data.get('Arman'))
data2['girls'].append('karine')
# print(data2)