import subprocess
import pytest


def test_soma_simples():
    with open('conta.c', 'w') as f:
        f.write('''
                    x = 3;
                    println(x); 
                ''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 3


def test_soma_varias():
    with open('conta.c', 'w') as f:
        f.write('''
                    x = 3;
                    y = 5;
                    z = 3 + 5;
                    println(z); 
                ''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 8


# test geral
def test_geral():
    with open('conta.c', 'w') as f:
        f.write(''' 
                    x /*asdasda*/ = 3;
                    y = 4;
                    z = x + y + 100;
                    println(x + y /*asdasda*/ + z); 
                ''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 114
