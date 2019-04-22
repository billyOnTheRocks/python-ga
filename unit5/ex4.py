#method to take transactions in cvs.txt file loop over them creating a dictionary and writing to a new file

def read_data(file):

    data ={}

    try:
        data_file = open(file, 'r')

        for line in data_file:
            col = line.split(';')
            data[col[0]] =[col[1], float(col[2])]
            return data


    except FileExistsError:
        print("error")
    finally:
        data_file.close()

if __name__ == '__main__':
    read_data("cvs.txt")
