import random, numpy

def convert_base(dec_num, base, length):
    res = []
    while dec_num >= base:
        res.append(dec_num % base)
        dec_num //= base
    else:
        res.append(dec_num)
    if len(res) < length:
        res += [0] * (length - len(res))
    res.reverse()
    return res

def create_array(r, n, q):
    array = numpy.zeros((r, n), int)
    for i in range(r):
        array[i][i] = 1
        array[i][r:] = [random.randint(0, q-1) for k in range(n-r)]
    return array

def get_code(q, array, r):
    """ Возвращает код, созданный с помощью порождающей матрицы array. """
    code = []
    for i in range(q ** r):
        #print(convert_base(i, q, r))
        code.append(numpy.dot(convert_base(i, q, r), array) % q)
    return code

def get_spectrum(n, code):
    """ Возвращает спектр кода: n - длина кода, code - код. """
    spectrum = [0 for i in range(n)]
    for el in code:
        spectrum[n - list(el).count(0) - 1] += 1
    spectrum[-1] -= 1
    spectrum[0] = 1
    return spectrum

#параметры порождающей матрицы
r = 5
start_n = 10
stop_n = 21
step = 2
q = 5

filename = "E:/Documents/ГУАП/магистратура/1 курс/2 семестр/Афанасьева/lab1/output.csv"
try:
    output_file = open(filename, 'w')

    for n in range(start_n, stop_n, step):
        print(n)
        array = create_array(r, n, q)
        # print(array)
        code = get_code(q, array, r)
        # print('\n'.join(str(el) for el in code))
        code_spectrum = get_spectrum(n, code)
        for i in range(len(code_spectrum)):
            output_file.write("{};".format(round(code_spectrum[i] / (q**r), 2)))
        output_file.write('\n')
        print(q ** r)

    output_file.close()
except(PermissionError):
    print("Файл недоступен")