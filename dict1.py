student_data = {
    'id1': {
        'name': ['Nikhil'], 
        'class': ['8'], 
        'sub_integration': ['English', 'Maths', 'Science'] 
    }, 
    'id2': {
        'name': ['Sharan'], 
        'class': ['8'], 
        'sub_integration': ['English', 'Social', 'Science'] 
    }, 
    'id3': {
        'name': ['Jathin'], 
        'class': ['8'], 
        'sub_integration': ['Maths', 'Social', 'Science'] 
    }, 
    'id4': {
        'name': ['Ayansh'], 
        'class': ['8'], 
        'sub_integration': ['English', 'Social', 'Maths'] 
    }
}

# print(student_data['id1']['name'])

result = {}

for key, value in student_data.items():
    if (value not in result.values()):
        result[key] = value
    
print(result['id1']['name'])