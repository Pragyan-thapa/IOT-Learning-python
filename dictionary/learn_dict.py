sedial_codes = [                                       
    (880, 'Bangladesh'),
    (55,  'Brazil'),
    (86,  'China'),
    (91,  'India'),
    (62,  'Indonesia'),
    (81,  'Japan'),
    (234, 'Nigeria'),
    (92,  'Pakistan'),
    (7,   'Russia'),
    (1,   'United States'),
]

dial_codes = {country:code for code,country in sedial_codes if code > 80}

dial_codes.update({"Nepal":977,"Australia":61})
print(dial_codes.get("Nepal"))
dial_codes['United States'] = 232
dial_codes['honkong'] = 3243
dial_codes.pop('Nigeria')
print(dial_codes)


# numbers_cube = {a:a**4 for a in range(1,11)}
# print(numbers_cube)
