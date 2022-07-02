import lorem

# parag = lorem.paragraph()
parag = 'Sed tempora amet be was was was was was was was dolor dolorem labore. Tempora est etincidunt non dolore eius sed.' \
        ' Consectetur quaerat am am is neque ut velit. Ipsum quaerat dolore sit consectetur. Aliquam non ' \
        'tempora aliquam quaerat ipsum voluptatem quiquia. Amet is are are sed ipsum est labore dolor.'
# print(parag)
par_list = list(parag.split(' '))
total_len = len(par_list)
set_parag = set(par_list)
unique_len = len(set(par_list))
# print(len(set(list(parag.split(' ')))))

print(f'total len : {total_len}')
print(f'unique len : {unique_len}')
be_count = 0
for char in par_list:
    if char in 'be,am,is,are,was,were':
        be_count += 1
        # print(parag[char])
print(f'be_count : {be_count}')
be_dict = {'be': 0, 'am': 0, 'is': 0, 'are': 0, 'was': 0, 'were': 0}
# be_dict = {}
for char in par_list:
    if char in 'be,am,is,are,was,were':
        be_dict[char] += 1
print(be_dict)