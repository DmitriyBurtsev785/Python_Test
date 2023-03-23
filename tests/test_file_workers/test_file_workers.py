from my_funcs.file_workers import read_from_file




def create_test_data(test_data):

    with open('testfile.txt', 'a') as f_o:
        f_o.writelines(test_data)



def test_read_from_file():
    # with open('testfile.txt', 'w'): # очищаем файл
    #     pass
    test_data = ['one\n', 'two\n', 'three\n']
    create_test_data(test_data)
    assert test_data == read_from_file('testfile.txt')


def test_read_from_file_2():
    # with open('testfile.txt', 'w'): # очищаем файл
    #     pass
    test_data = ['one\n', 'two\n', 'three\n']
    # with open('testfile.txt', 'a') as f_o:
    #     f_o.writelines(test_data)
    create_test_data(test_data)

    assert test_data == read_from_file('testfile.txt')