p_list = [
    {
        'stt': 1,
        'Ten Nv': "Huy",
        'Gio': 30,
        'Luong': 50,
    },
    {
        'stt': 2,
        'Ten Nv': "Quan",
        'Gio': 20,
        'Luong': 40,
    },
    {
        'stt': 3,
        'Ten Nv': "Duc",
        'Gio': 15,
        'Luong': 35,
    },
]
# s = 0
# for p in p_list:
#     print(p['Gio'], sep=".")
    
# luong = input("Ten nguoi nhan luong")
# for p in p_list:
#     print(p['Luong'], sep=".")

total_salary = 0

for p in p_list:
    salary = p['Gio'] * p['Luong']
    total_salary += salary
