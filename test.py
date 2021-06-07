import subprocess
import pytest
'''
To fix:

return de op booleanas esta byte, precisa retornar bool
'''

# test geral
def test_geral():
    with open('conta.c', 'w') as f:
        f.write('''int main(){
                    int x;
                    int y;
                    int z; 
                    x /*asdasda*/ = 3;
                    y = 4;
                    z = x + y + 100;
                    println(x + y /*asdasda*/ + z); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 114


def test_soma_simples():
    with open('conta.c', 'w') as f:
        f.write('''int main(){
                    int x;
                    x = 3;
                    println(x); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 3


def test_soma_varias():
    with open('conta.c', 'w') as f:
        f.write('''int main(){
                    int x;
                    int y;
                    int z;

                    x = 3;
                    y = 5;
                    z = 3 + 5;
                    println(z); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 8


def teste_issue():
    with open('conta.c', 'w') as f:
        f.write('''int main(){

                    int x1;
                    int y2;
                    int z_final;

                    x1 = 8;
                    y2 = 5;



                    z_final = (x1 + y2) * ---37;;
                    println(z_final); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == -481


def teste_input_igual_2():
    with open('conta.c', 'w') as f:
        f.write('''int main(){

                    int x_1;
                    int y;
                    int z_final_;

                    x_1 = 8;
                    y = 57;



                    z_final_ = (x_1 + y) * readln();;
                    println(z_final_); 
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c < input.txt", shell=True)) == 130


def teste_eq():
    with open('conta.c', 'w') as f:
        f.write('''int main(){

                    int x;
                    int y;
                    bool z;

                    x = 8;
                    y = 57;



                    z = x == y;;;
                    println(z); 
                }''')
    assert subprocess.check_output("python3 main.py conta.c", shell=True) == b'False\n'


def teste_block():
    with open('conta.c', 'w') as f:
        f.write('''int main(){

                        int x; 
                        int y;
                        int z;

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
        f.write('''int main(){
                    int x;
                    int y;

                    x = 3;
                    y = 6;

                    if (x+y < 10) 
                        println(1); 
                    println(0);
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 1

def teste_if_else():
    with open('conta.c', 'w') as f:
        f.write('''int main(){
                    int x;
                    int y;

                    x = 3;
                    y = 7;

                    if (x+y < 10) {
                        println(1); 
                    } else {
                        println(0);
                    }
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 0

def teste_if_alone():
    with open('conta.c', 'w') as f:
        f.write('''int main(){

                    int x;
                    int y;

                    x = 3;
                    y = 7;

                    if (x+y < 10) {
                        println(1); 
                    } 
                
                    println(0);
                
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 0

def teste_if_elseif():
    with open('conta.c', 'w') as f:
        f.write('''int main(){

                    int x;
                    int y;

                    x = 3;
                    y = 7;

                    if (x+y < 10) {
                        println(1); 
                    } else if (x == 3) {
                        println(0);
                    }
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 0

def teste_if_elseif_else():
    with open('conta.c', 'w') as f:
        f.write('''int main(){

                    int x;
                    int y;

                    x = 3;
                    y = 7;

                    if (x+y < 10) {
                        println(0); 
                    } else if (x == 2) {
                        println(1);
                    } else {
                        println(2);
                    }

                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 2

def teste_while():
    with open('conta.c', 'w') as f:
        f.write('''int main(){
                    int x;
                    x = 0;

                    while (x < 10) {
                        x = x + 1;
                    }

                    println(x);

                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 10

def teste_string():
    with open('conta.c', 'w') as f:
        f.write('''int main(){
                    string x;
                    x = "oi";
                    println(x);
                }''')
    assert subprocess.check_output("python3 main.py conta.c", shell=True) == b'oi\n'

def teste_bool():
    with open('conta.c', 'w') as f:
        f.write('''int main(){
                    bool x;
                    x = 1 > 0;
                    println(x);
                }''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 1

def teste_bool_true_false():
    with open('conta.c', 'w') as f:
        f.write('''int main(){
    bool x;
    int y;
    x = false+1;
    y = x;
    println(y);
}''')
    assert int(subprocess.check_output("python3 main.py conta.c", shell=True)) == 1

    