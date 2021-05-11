import subprocess
import pytest
'''
To fix:

return de op booleanas esta byte, precisa retornar bool
'''

# test geral
def test_geral():
    with open('conta.c', 'w') as f:
        f.write('''{ 
                    x /*asdasda*/ = 3;
                    y = 4;
                    z = x + y + 100;
                    println(x + y /*asdasda*/ + z); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 114


def test_soma_simples():
    with open('conta.c', 'w') as f:
        f.write('''{
                    x = 3;
                    println(x); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 3


def test_soma_varias():
    with open('conta.c', 'w') as f:
        f.write('''{
                    x = 3;
                    y = 5;
                    z = 3 + 5;
                    println(z); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 8


def teste_issue():
    with open('conta.c', 'w') as f:
        f.write('''{
                    x1 = 8;
                    y2 = 5;



                    z_final = (x1 + y2) * ---37;;
                    println(z_final); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == -481


def teste_input_igual_2():
    with open('conta.c', 'w') as f:
        f.write('''{
                    x_1 = 8;
                    y = 57;



                    z_final_ = (x_1 + y) * readln();;
                    println(z_final_); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c < input.txt", shell=True)) == 130


def teste_eq():
    with open('conta.c', 'w') as f:
        f.write('''{
                    x = 8;
                    y = 57;



                    z = x == y;;;
                    println(z); 
                }''')
    assert subprocess.check_output("python3 main.py conta.c", shell=True) == b'False\n'


def teste_block():
    with open('conta.c', 'w') as f:
        f.write('''{
                        {
                            x = 8;
                            y = 57;
                        }

                    z = x * y;;;
                    println(z); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 456

def teste_if():
    with open('conta.c', 'w') as f:
        f.write('''{
                    x = 3;
                    y = 6;

                    if (x+y < 10) 
                        println(1); 
                    println(0);
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 1

def teste_if_else():
    with open('conta.c', 'w') as f:
        f.write('''{
                    x = 3;
                    y = 7;

                    if (x+y < 10) {
                        println(1); 
                    } else {
                        println(0);
                    }
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 0

def teste_if_else():
    with open('conta.c', 'w') as f:
        f.write('''{
                    x = 3;
                    y = 7;

                    if (x+y < 10) {
                        println(1); 
                    } 
                
                    println(0);
                
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 0