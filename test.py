import subprocess
import pytest

# test sum
def test_1_sum():
    assert int(subprocess.check_output("python3 main.py '1+1'", shell=True)) == 2

def test_2_sum():
    assert int(subprocess.check_output("python3 main.py '1+1+1'", shell=True)) == 3

def test_3_sum():
    assert int(subprocess.check_output("python3 main.py '100+100+100'", shell=True)) == 300

# test sub
def test_1_sub():
    assert int(subprocess.check_output("python3 main.py '1-1'", shell=True)) == 0

def test_2_sub():
    assert int(subprocess.check_output("python3 main.py '1-1-1'", shell=True)) == -1

def test_3_sub():
    assert int(subprocess.check_output("python3 main.py '100-100-100'", shell=True)) == -100

# test mult
def test_1_mult():
    assert int(subprocess.check_output("python3 main.py '4*2'", shell=True)) == 8

def test_2_mult():
    assert int(subprocess.check_output("python3 main.py '2*2*2'", shell=True)) == 8

# test div
def test_1_div():
    assert int(subprocess.check_output("python3 main.py '20/2'", shell=True)) == 10

def test_2_div():
    assert int(subprocess.check_output("python3 main.py '20/2/2'", shell=True)) == 5

# test comments
def test_comment1():
    assert int(subprocess.check_output("python3 main.py '/*aa*/ 1'", shell=True)) == 1

def test_comment2():
    assert int(subprocess.check_output("python3 main.py '1 + 1/*aa*/1'", shell=True)) == 12

def test_comment3():
    assert int(subprocess.check_output("python3 main.py '1 - /*2+4* / */ 1'", shell=True)) == 0

# Factor
def test_factor_m_m():
    assert int(subprocess.check_output("python3 main.py '--77'", shell=True)) == 77

def test_factor_p_m_m_p_p():
    assert int(subprocess.check_output("python3 main.py '+--++3'", shell=True)) == 3

def test_parenteses1():
    assert int(subprocess.check_output("python3 main.py '(3 + 2) /5'", shell=True)) == 1

def test_factor_meio():
    assert int(subprocess.check_output("python3 main.py '3 - -2/4'", shell=True)) == 3           #??

def test_parenteses2():
    assert int(subprocess.check_output("python3 main.py '4/(1+1)*2'", shell=True)) == 4

# Misc
def test_sum_sub_space():
    assert int(subprocess.check_output("python3 main.py '100 + 100 -  100+1'", shell=True)) == 101

def test_big_spaces():
    assert int(subprocess.check_output("python3 main.py '100 + 100 -  100+1                                               -101                  - 900'", shell=True)) == -900

