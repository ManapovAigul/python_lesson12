# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':


   string = "молочник раз месяц привозит молоко в совхоз из молочных остатков"

array = [1, 2, 5, 6, 'string', [1, 2], 1.2]

array_1 = [1, 2,2,2,2,2,2, 5, 6, 'string', [1, 2], 1.2]
array_2 = [1,432,46,68,23,2,3]

if __name__ == '__main__':
    array.remove(6)
    print(array)
    array.remove('string')
    print(array)
    array.pop(0)
    print(array)
    print(array_1.index('string'))
    print(array_1.count(2))
    array_2.sort()
    print(array_2)
    array_2.reverse()
    print(array_2)
    array_1.copy(1)
    print(array_1)
    array_1.clear(4)
    print(array_1)













