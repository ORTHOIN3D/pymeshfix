# get location of the example meshes
from os.path import dirname, join, realpath
pth = dirname(realpath(__file__))
bunny_scan = join(pth, 'StanfordBunny.ply')
planar_mesh = join(pth, 'planar_mesh.ply')

from pymeshfix.examples.fix import *

# use numpy arrays

def load_bunny_arrays():
    """Return the faces and points arrays from the Stanford bunny"""
    import numpy as np
    np_file = np.load(join(pth, 'bunny.npz'))
    return np_file['points'], np_file['faces']
