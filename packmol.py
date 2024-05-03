from sys import argv


class packmol():


    def __init__(self):
        self.inputs()
        self.write_data('pack.inp')


    def inputs(self):
        self.tolerance = float(input('Tolerance: '))
        self.filetype = input('Filetype: ')
        self.output = input('Output Name: ')
        self.structures= [x for x in argv[1:]]
        self.center = str(input('Is one of the Molecules at the center of the box? (y/n)'))
        self.choose_center = input('Which molecule is at the center of the box? (1,2,3,4,5,6,7,8,9,10)')
        self.number_mol = int(input('Number of molecules: '))
        self.box_coordinates_x = float(input('X coordinate of box: '))
        self.box_coordinates_y = float(input('Y coordinate of box: '))
        self.box_coordinates_z = float(input('Z coordinate of box: '))


    def write_data(self, file):

        with open(file, 'w') as file:
            file.write('tolerance {}\n'.format(self.tolerance))
            file.write('randominitialpoint\n')
            file.write('filetype {} \n'.format(self.filetype))
            file.write('output {}.{} \n'.format(self.output, self.filetype))
            print(self.structures)
            for i in self.structures:
                if self.center == 'y':
                    file.write('structure {}\n'.format(argv[1]))
                    file.write('number {} \n'.format(self.number_mol))
                    file.write('inside box {} {} {} '.format(self.box_coordinates_x /2 ,self.box_coordinates_y /2,self.box_coordinates_z /2))



    

    def cli(self):
        pass
    
if __name__ == '__main__':
    packmol()