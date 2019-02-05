from xyz import read_xyz, write_xyz
# xyz read/write functionality from https://github.com/pele-python/pele/blob/master/pele/utils/xyz.py
import numpy as np
dist = []
def donorf(h_coords, o_coords):
    for atom in o_coords:
        for h_atom in h_coords:
            dist = []
            all_dist = np.subtract(o_coords, h_coords)
            all_distsq = all_dist ** 2
            dist = ((np.sum(all_distsq, axis=2)) ** 0.5)
            bonds = 0
            donor = []
            for count, unit in enumerate(dist):
                bonds = len([1 for h in unit if h <= 1])
                if bonds == 3:
                    donor = (o_coords[count])
    print("Donor coordinates:", donor)
    acceptorf(donor, o_coords)

def distance(h_coords, o_coords):
    global dist
    for atom in o_coords:
        for h_atom in h_coords:
            dist = []
            all_dist = np.subtract(o_coords, h_coords)
            all_distsq = all_dist ** 2
            dist = ((np.sum(all_distsq, axis=1)) ** 0.5)
def main():
    infile_name = 'h5o2_test.xyz'
    # Variables needed for calculations
    all_steps = []
    proton_coords = []
    np.asarray(proton_coords)
    with open(infile_name) as file:
        while True:
            try:
                all_steps.append(read_xyz(file))
            except ValueError:
                break
        for step in all_steps:
            oxygen(step)
    outfile_name = "output_test.xyz"
    with open(outfile_name, 'w') as out_file:
        for step, proton in zip(all_steps, proton_coords):
            coords_out = []
            for atom in zip(step.coords):
                coords_out += atom
            coords_out += (proton, )
            coords_out = np.asarray(coords_out)
            atomtypes_out = step.atomtypes + ["DUM", ]
            title_out = step.title
            write_xyz(out_file, coords_out, title_out, atomtypes_out)
def oxygen(step):
    # Find oxygen atoms in step
    o_coords = []
    h_coords = []
    for ox_index, (ox, coords) in enumerate(zip(step.atomtypes, step.coords)):
        dist_between = []
        if ox == "O":
            o_coords.append([step.coords[ox_index]])
            # Find bonded hydrogen atoms in step
    for h_index, (h, coords) in enumerate(zip(step.atomtypes, step.coords)):
        if h == "H":
            h_coords.append(coords)
    donorf(h_coords, o_coords)
def acceptorf(donor, o_coords):
    acceptor = []
    for count, coords in enumerate(o_coords):
        distance(donor, coords)
        if dist <= 2.8 and dist > 0:
            acceptor.append(o_coords[count])
        print("Acceptor:", acceptor)


# --------------------------------------------------------------------
if __name__ == '__main__':
    main()