from sys import argv



if len (argv) <= 1:
    print('Usage: python packmol.py <Solute> <Solvent> <Solvent> ...')
    exit()

class packmol():


    def __init__(self):
        self.inputs()
        self.write_data('pack.inp')


    def inputs(self):
        self.tolerance = float(input('Tolerance: '))
        self.filetype = input('Filetype: ')
        self.output = input('Output Name: ')
        self.structures= [x for x in argv[1:]]
        print('The following structures will be used:', self.structures)
        print('Molecule {} will be considered a solute'.format(self.structures[0]))
        self.center = (lambda x: True if x == 'y' else False)(input('Is Solute at the center of the box? (y/n): ').lower())
        # self.choose_center = input('Which molecule is at the center of the box?')
        self.number_mol_solute = int(input('Number of solute molecules: '))
        self.number_mol_sovent = int(input('Number of solvent molecules: '))
        self.box_coordinates_x = float(input('X coordinate of box: '))
        self.box_coordinates_y = float(input('Y coordinate of box: ')) 
        self.box_coordinates_z = float(input('Z coordinate of box: '))


    def write_data(self, file):


        with open(file, 'w') as file:
            file.write('tolerance {}\n'.format(self.tolerance))
            file.write('randominitialpoint\n')
            file.write('seed 1 \n')
            file.write('filetype {} \n'.format(self.filetype))
            file.write('output {}.{} \n'.format(self.output, self.filetype))
            print(self.structures)

            
            for i in range(len(self.structures)):
                if self.center == True:
                    if i == 0:
                        file.write('\nstructure {}\n'.format(self.structures[i]))
                        file.write('    number {} \n'.format(self.number_mol_solute/self.number_mol_solute))
                        file.write('    inside box 0. 0. 0. 0. 0. 0. \n')
                        file.write('    centerofmass\n')
                        file.write('    radius 1.5 \n')
                        file.write('end structure\n')
                    else:
                        self.box_coordinates_x -= 0.25
                        self.box_coordinates_y -= 0.25
                        self.box_coordinates_z -= 0.25
                        file.write('\nstructure {}\n'.format(self.structures[i]))
                        file.write('    number {} \n'.format(self.number_mol_sovent))
                        file.write('    inside box {} {} {} {} {} {} \n'.format(-self.box_coordinates_x/2, -self.box_coordinates_y /2,-self.box_coordinates_z /2, self.box_coordinates_x /2, self.box_coordinates_y /2, self.box_coordinates_z /2 ))
                        file.write('end structure\n')

                else:
                    if i == 0:
                        file.write('\nstructure {}\n'.format(self.structures[i]))
                        file.write('    number {} \n'.format(self.number_mol_solute))
                        file.write('    inside box 0. 0. 0. {} {} {} \n'.format(self.box_coordinates_x, self.box_coordinates_y ,self.box_coordinates_z))
                        file.write('end structure\n')
                    if self.structures[i] != self.structures[0]:
                        self.box_coordinates_x -= 0.25
                        self.box_coordinates_y -= 0.25
                        self.box_coordinates_z -= 0.25
                        file.write('\nstructure {}\n'.format(self.structures[i]))
                        file.write('    number {} \n'.format(self.number_mol_sovent))
                        file.write('    inside box 0. 0. 0. {} {} {} \n'.format(self.box_coordinates_x, self.box_coordinates_y ,self.box_coordinates_z))
                        file.write('end structure\n')




    

    def cli(self):
        pass
    
if __name__ == '__main__':
    packmol()
