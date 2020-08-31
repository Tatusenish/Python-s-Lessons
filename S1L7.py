class Matrix:
    def __init__(self, first_list, second_list):

        self.first_list = first_list
        self.second_list = second_list

    def __add__(self):
        list_of_list = [[0, 0, 0, 0],
                        [0, 0, 0, 0]]

        for i in range(len(self.first_list)):

            for j in range(len(self.second_list[i])):
                list_of_list[i][j] = self.first_list[i][j] + self.second_list[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in list_of_list]))

    def __str__(self):
        list_of_list = [[0, 0, 0, 0],
                        [0, 0, 0, 0]]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in list_of_list]))


user_matrix = Matrix([[3, 5, 8, 3],
                      [8, 3, 7, 1]],
                     [[2, 15, 52, 23],
                      [7, 9, 79, 63]])

print(user_matrix.__add__())
