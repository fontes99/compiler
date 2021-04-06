import sys
import pytest
import subprocess
import main as calculator


def capture(command: [str]):
    proc = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    out, err = proc.communicate()
    return out, err, proc.returncode


@pytest.mark.parametrize(
    "input_str",
    [
        "0+0",
        "0+1",
        "1+1",
        "10+10",
        "11+11",
        "11-11",
        "11-12",
        "1+1-1+1",
        "1+1-1+1+1*1",
        "1+1-1+1+1*1-1/1",
        "2*2",
        "2*2*2",
        "2*2*2+1",
        "1+2*2*2+1",
        "1+2*2*2+1",
        "2*2/4+1",
        "2 * 2 / 4 + 1",
        "     2 * 2 / 4 + 1       ",
        "2*2*2*2*2+1",
        "2*2*2*2*2+1+2*2*2*2*2",
        "2*2*2*2*2+1+2*2*2*2*2+1+2*2*2*2*2",
        "32/2/2/2/2/2+1",
        "32/2/2/2/2/2+1+32/2/2/2/2/2",
        "32/2/2/2/2/2+1+32/2/2/2/2/2+1+32/2/2/2/2/2",
        "3-2",
        "4/2+3",
        "3+4/2",
        "(3 + 2) /5",
        "--77",
        "+--++3",
        "3 - -2/4",
        "4/(1+1)*2",
        "(1+1) * (2+2)",
        "(2 * 3) + 4",
        "(1)",
        "2*-3",
        "4/-2",
    ],
)
def test_valid(input_str: str, capsys) -> None:
    command = ["python3", "./main.py", "./test.c"]
    with open("./test.c", "w") as f:
        f.write(input_str)
    out, err, exitcode = capture(command)
    assert int(out) == int(eval(input_str))


@pytest.mark.parametrize(
    "input_str, expected_result",
    [
        ("/*A*/ 0 + 0", 0),
        ("0 /*A*/ + 1", 1),
        ("1 + /*A*/ 1", 2),
        ("10 + 10 /*A*/", 20),
        ("/*A*/ 11 /*A*/ + 11", 22),
        ("10 /*A*/ + /*A*/ 0", 10),
        ("10 + /*A*/ 1 /*A*/", 11),
        ("/*A*/ 100 + /*A*/ 0", 100),
        ("/*A*/ 100 + 1 /*A*/", 101),
        ("/*A*/ 100 + /*A*/ 10 /*A*/", 110),
    ],
)
def test_with_comment(input_str: str, expected_result: str, capsys) -> None:
    command = ["python3", "./main.py", "./test.c"]
    with open("./test.c", "w") as f:
        f.write(input_str)
    out, err, exitcode = capture(command)
    assert int(out) == int(expected_result)


@pytest.mark.parametrize(
    "input_str",
    [
        "",
        "+",
        "-",
        "A",
        "1A+1B",
        "1 1",
        "1 10",
        "10 1",
        "10 10",
        "+1 1",
        "-1 1",
        "1 1+",
        "1 1-",
        "1 1++1",
        "1 1--1",
        "1 1**1",
        "1 1//1",
        "2-*3",
        "2+*3",
        "2*/3",
        "2/*3",
        "4-/2",
        "/*A*/1+1/*/*A*/*/",
        "/*A*/1+1/*B/*C*/*/",
        "3+ /* a */",
        "/* a */",
        "3- 3 /* a",
        "(1",
        "1)",
        "(",
        ")",
        "()",
        "(()",
        "())",
        "(1+1",
        "1+1)",
        "((1+1)",
        "(1+1))",
        "()1+1",
        "()1+1()",
        "1+1()",
        "1()+1",
    ],
)
def test_invalid(input_str: str, capsys) -> None:
    command = ["python3", "./main.py", "./test.c"]
    with open("./test.c", "w") as f:
        f.write(input_str)
    out, err, exitcode = capture(command)
    assert exitcode == 1