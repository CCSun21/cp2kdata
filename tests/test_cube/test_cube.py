from cp2kdata import Cp2kCube
import os
import pytest
import numpy as np


path_prefix = "tests/test_cube/"
cube_list = [Cp2kCube(os.path.join(path_prefix, "Si_bulk8-v_hartree-1_0.cube"))]
answer_dir_list = [os.path.join(path_prefix, "answer_Si_bulk8-v_hartree-1_0.cube")]

test_params = list(zip(cube_list, answer_dir_list))


@pytest.fixture(params=test_params, scope='class')
def cube_and_answer(request):
    return request.param

class TestCp2kCube():
    def test_num_atoms(self, cube_and_answer):
        cube = cube_and_answer[0]
        answer_dir = cube_and_answer[1]
        num_atoms = cube.num_atoms
        num_atoms_answer = np.load(os.path.join(answer_dir, "num_atoms.npy"))
        assert num_atoms == num_atoms_answer
    def test_grid_size(self, cube_and_answer):
        cube = cube_and_answer[0]
        answer_dir = cube_and_answer[1]
        grid_size = cube.grid_size
        grid_size_answer = np.load(os.path.join(answer_dir, "grid_size.npy"))
        assert np.all(grid_size == grid_size_answer)
    def test_grid_space(self, cube_and_answer):
        cube = cube_and_answer[0]
        answer_dir = cube_and_answer[1]
        grid_space = cube.grid_space
        grid_space_answer = np.load(os.path.join(answer_dir, "grid_space.npy"))
        assert np.all(grid_space == grid_space_answer)
    def test_cube_vals(self, cube_and_answer):
        cube = cube_and_answer[0]
        answer_dir = cube_and_answer[1]
        cube_vals = cube.cube_vals
        cube_vals_answer = np.load(os.path.join(answer_dir, "cube_vals.npy"))
        assert np.all(cube_vals == cube_vals_answer)
    def test_pav(self, cube_and_answer):
        cube = cube_and_answer[0]
        answer_dir = cube_and_answer[1]
        pav = cube.get_pav()
        pav_answer = np.load(os.path.join(answer_dir, "pav.npy"))
        assert np.all(pav == pav_answer)
    def test_mav(self, cube_and_answer):
        cube = cube_and_answer[0]
        answer_dir = cube_and_answer[1]
        mav = cube.get_mav(l1=1, l2=1, ncov=2)
        mav_answer = np.load(os.path.join(answer_dir, "mav.npy"))
        assert np.all(mav == mav_answer)



