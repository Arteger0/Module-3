calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    len_str = len(string)
    up_str = string.upper()
    low_str = string.lower()
    return len_str, up_str, low_str

def is_countains(string, list_to_search):
    count_calls()
    list_to_search = [list.lower() for list in list_to_search]
    str_to_list = string.lower() in list_to_search
    return str_to_list

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_countains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_countains('cycle', ['recycling', 'cyclic']))
print(calls)