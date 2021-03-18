import subprocess

def test_1_sum():
    assert int(subprocess.check_output("python3 main.py '1+1'", shell=True)) == 2

def test_2_sum():
    assert int(subprocess.check_output("python3 main.py '1+1+1'", shell=True)) == 3

def test_3_sum():
    assert int(subprocess.check_output("python3 main.py '100+100+100'", shell=True)) == 300

def test_1_sub():
    assert int(subprocess.check_output("python3 main.py '1-1'", shell=True)) == 0

def test_2_sub():
    assert int(subprocess.check_output("python3 main.py '1-1-1'", shell=True)) == -1

def test_3_sub():
    assert int(subprocess.check_output("python3 main.py '100-100-100'", shell=True)) == -100

def test_1_mult():
    assert int(subprocess.check_output("python3 main.py '4*2'", shell=True)) == 8

def test_2_mult():
    assert int(subprocess.check_output("python3 main.py '2*2*2'", shell=True)) == 8

def test_1_div():
    assert int(subprocess.check_output("python3 main.py '20/2'", shell=True)) == 10

def test_2_div():
    assert int(subprocess.check_output("python3 main.py '20/2/2'", shell=True)) == 5

# tests given

def test_sum_sub_space():
    assert int(subprocess.check_output("python3 main.py '100 + 100 -  100+1'", shell=True)) == 101

def test_big_spaces():
    assert int(subprocess.check_output("python3 main.py '100 + 100 -  100+1                                               -101                  - 900'", shell=True)) == -900
