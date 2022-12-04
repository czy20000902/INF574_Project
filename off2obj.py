def read_off_file(input):
    vertex = []
    surface = []
    fin = open(input, 'r')
    if not fin:
        print('Fail to open the off file!')
        exit(1)

    output = input[:-3] + 'obj'
    fout = open(output, 'w')
    if not fout:
        print('Fail to open the obj file!')
        exit(1)

    content = fin.readlines()

    vertex_num, surface_num, other_num = content[1].split()
    vertex_num = int(vertex_num)
    surface_num = int(surface_num)
    other_num = int(other_num)
    for i in range(2, vertex_num + 2):
        vertex.append(content[i].split())

    for i in range(vertex_num + 2, vertex_num + surface_num + 2):
        surface.append(content[i].split())

    for i in range(vertex_num):
        fout.write('v')
        for j in range(3):
            fout.write(' ' + vertex[i][j])
        fout.write('\n')

    for i in range(surface_num):
        fout.write('f')
        fout.write(' ' + str(int(surface[i][1]) + 1) +
                   ' ' + str(int(surface[i][3]) + 1) +
                   ' ' + str(int(surface[i][2]) + 1))
        fout.write('\n')


if __name__ == '__main__':
    read_off_file('./data/star/bunny.off')
