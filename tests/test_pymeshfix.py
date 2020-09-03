import numpy as np
import pytest

import pymeshfix
from pymeshfix.examples import bunny_scan
from pymeshfix.meshfix import PV_INSTALLED


@pytest.mark.skipif(not PV_INSTALLED, reason='Requires pyvista')
def test_repair_vtk():
    import pyvista as pv
    meshin = pv.PolyData(bunny_scan)
    meshfix = pymeshfix.MeshFix(meshin)
    meshfix.repair()

    # check arrays and output mesh
    assert np.any(meshfix.v)
    assert np.any(meshfix.f)
    meshout = meshfix.mesh
    assert meshfix.mesh.n_points

    # test for any holes
    pdata = meshout.extract_edges(non_manifold_edges=False, feature_edges=False,
                                  manifold_edges=False)
    assert pdata.n_points == 0


def test_repair_array():
    points, faces = pymeshfix.examples.load_bunny_arrays()
    meshfix = pymeshfix.MeshFix(meshin)

    meshfix.repair()

    # check arrays and output mesh
    assert np.any(meshfix.v)
    assert np.any(meshfix.f)
    meshout = meshfix.mesh
    assert meshfix.mesh.n_points

    # test for any holes
    pdata = meshout.extract_edges(non_manifold_edges=False, feature_edges=False,
                                  manifold_edges=False)
    assert pdata.n_points == 0
