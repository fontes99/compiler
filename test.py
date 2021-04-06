import subprocess
import pytest

# test sum
def test_1_sum():
    with open('conta.c', 'w') as f:
        f.write('1+1')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 2

def test_2_sum():
    with open('conta.c', 'w') as f:
        f.write('1+1+1')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 3

def test_3_sum():
    with open('conta.c', 'w') as f:
        f.write('100+100+100')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 300

# test sub
def test_1_sub():
    with open('conta.c', 'w') as f:
        f.write('1-1')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 0

def test_2_sub():
    with open('conta.c', 'w') as f:
        f.write('1-1-1')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == -1

def test_3_sub():
    with open('conta.c', 'w') as f:
        f.write('100-100-100')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == -100

# test mult
def test_1_mult():
    with open('conta.c', 'w') as f:
        f.write('4*2')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 8

def test_2_mult():
    with open('conta.c', 'w') as f:
        f.write('2*2*2')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 8

# test div
def test_1_div():
    with open('conta.c', 'w') as f:
        f.write('20/2')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 10

def test_2_div():
    with open('conta.c', 'w') as f:
        f.write('20/2/2')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 5

# test comments
def test_comment1():
    with open('conta.c', 'w') as f:
        f.write('/*aa*/ 1')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 1

def test_comment2():
    with open('conta.c', 'w') as f:
        f.write('1 + 1/*aa*/1')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 12

def test_comment3():
    with open('conta.c', 'w') as f:
        f.write('1 - /*2+4* / */ 1')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 0

# Factor
def test_factor_m_m():
    with open('conta.c', 'w') as f:
        f.write('--77')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 77

def test_factor_p_m_m_p_p():
    with open('conta.c', 'w') as f:
        f.write('+--++3')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 3

def test_parenteses1():
    with open('conta.c', 'w') as f:
        f.write('(3 + 2) /5')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 1

def test_factor_meio():
    with open('conta.c', 'w') as f:
        f.write('3 - -2/4')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 3           #??

def test_parenteses2():
    with open('conta.c', 'w') as f:
        f.write('4/(1+1)*2')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 4

# Misc
def test_sum_sub_space():
    with open('conta.c', 'w') as f:
        f.write('100 + 100 -  100+1')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 101

def test_big_spaces():
    with open('conta.c', 'w') as f:
        f.write('100 + 100 -  100+1                                               -101                  - 900')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == -900

