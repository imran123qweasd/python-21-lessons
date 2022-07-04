#                                   Работа с файлами
try:
    file = open('test.txt')
    output = file.readline()
    output2 = file.readline()

except:
    pass
finally:
    file.close()
    print(output)
    print(output2)
