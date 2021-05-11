import pandas as p
data = p.read_csv('countries.csv', sep=',')
franch_speaking = data[data.languages == 'French'][['name', 'capital', 'area', 'currencies', 'latlng']]
largest = data.nlargest(10, 'area')[['name', 'capital', 'area', 'currencies', 'latlng']]
smallest = data.nsmallest(10, 'area')[['name', 'capital', 'area', 'currencies', 'latlng']]
islands = data[data.borders.isnull()][['name', 'capital', 'area', 'currencies', 'latlng']]
southern = data.latlng
frame = p.DataFrame()

for i in range(0, len(southern)):
    if(southern[i][0]=='-'):
        frame = frame.append(data[data.name == data['name'][i]][['name', 'capital', 'area', 'currencies', 'latlng']])
print(frame)
try:
    writer = p.ExcelWriter('ResultInfo.xlsx', engine='xlsxwriter')
    data.to_excel(writer, 'all')
    franch_speaking.to_excel(writer, 'French-speaking')
    print('French-speaking countries added')
    largest.to_excel(writer, 'Largest countries')
    print('The largest countries added')
    smallest.to_excel(writer, 'Smallest countries')
    print('The smallest countries added')
    islands.to_excel(writer, 'Island countries')
    print('The island countries added')
    frame.to_excel(writer, 'Southern countries')
    writer.save()
except:
    pass
