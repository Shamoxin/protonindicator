from xyz import read_xyz, write_xyz
# xyz read/write functionality from https://github.com/pele-python/pele/blob/master/pele/utils/xyz.py
import numpy as np
def main():
    infile_name = 'h5o2_2cc_scan_sum.xyz'
    # Variables needed for calculations
    all_steps = []
    h_x = 0
    h_y = 0
    h_z = 0
    o1_x = 0
    o1_y = 0
    o1_z = 0
    o2_x = 0
    o2_y = 0
    o2_z = 0
    disto1_square = 0
    dist_o1 = 0
    disto2_square = 0
    dist_o2 = 0
    proton_coords = []
    np.asarray(proton_coords)
    with open(infile_name) as file:
        while True:
            try:
                all_steps.append(read_xyz(file))
            except ValueError:
                break
        for i in range(0, 880):
            h_x = all_steps[i].coords[1, 0]
            h_y = all_steps[i].coords[1, 1]
            h_z = all_steps[i].coords[1, 2]
            o1_x = all_steps[i].coords[0, 0]
            o1_y = all_steps[i].coords[0, 1]
            o1_z = all_steps[i].coords[0, 2]
            disto1_square = (((((h_x)-(o1_x))**2)+((h_y)-(o1_y))**2)+((h_z)-(o1_z))**2)
            dist_o1 = disto1_square**.5
            print('The distance from first oxygen atom is', dist_o1)
            o2_x = all_steps[i].coords[4, 0]
            o2_y = all_steps[i].coords[4, 1]
            o2_z = all_steps[i].coords[4, 2]
            disto2_square = (((((h_x) - (o2_x))**2) + ((h_y) - (o2_y))**2) + ((h_z) - (o2_z))**2)
            dist_o2 = disto2_square**.5
            print('The distance from second oxygen atom is', dist_o2)
            if dist_o1 < 1:
                proton_coords.append([o1_x, o1_y, o1_z])
            elif dist_o1 > 1 and dist_o2 > 1:
                proton_coords.append([h_x, h_y, h_z])
            elif dist_o2 < 1:
                proton_coords.append([o2_x, o2_y, o2_z])
        print('Proton indicator list:', proton_coords)
    outfile_name = "output_test.xyz"
    with open(outfile_name, 'w') as out_file:
        for step, proton in zip(all_steps, proton_coords):
            coords_out = []
            for atom in zip(step.coords):
                coords_out += atom
            coords_out += (proton, )
            coords_out = np.asarray(coords_out)
            atomtypes_out = step.atomtypes + ["He", ]
            title_out = step.title
            write_xyz(out_file, coords_out, title_out, atomtypes_out)


# --------------------------------------------------------------------
if __name__ == '__main__':
    main()