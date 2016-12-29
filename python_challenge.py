def arr(lower, upper):
    num_list = []
    for i in range(lower, upper + 1):
        if i % 2 == 0:
            num_list.append(i)
    return num_list

def combine_and_sort(list1, list2):
    combined_list = list1 + list2
    combined_list.sort()
    return combined_list

def create_dictionary(lower, upper):
    dict = {'odd' : [], 'even' : []}
    for i in range(lower, upper + 1):
        if i % 2 == 0:
            dict['even'].append(i)
        else:
            dict['odd'].append(i)
    return dict

def string_reverse(string):
    return string[::-1]

def check_anagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

def to_roman(num):
    if num > 1000:
        print 'Number too high'
    elif num == 0:
        print 'Nulla'
    else:
        roman = ""
        while num > 0:
            if num == 1000:
                roman += 'M'
                num -= 1000
            elif num >= 900:
                roman += 'CM'
                num -= 900
            elif num >= 500:
                roman += 'D'
                num -= 500
            elif num >= 400:
                roman += 'CD'
                num -= 400
            elif num >= 100:
                roman += 'C'
                num -= 100
            elif num >= 90:
                roman += 'XC'
                num -= 90
            elif num >= 50:
                roman += 'L'
                num -= 50
            elif num >= 40:
                roman += 'XL'
                num -= 40
            elif num >= 10:
                roman += 'X'
                num -= 10
            elif num >= 9:
                roman += 'IX'
                num -= 9
            elif num >= 5:
                roman += 'V'
                num -= 5
            elif num >= 4:
                roman += 'IV'
                num -= 4
            else:
                roman += 'I'
                num -= 1
        return roman
