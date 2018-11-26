import pytest
import problem3

def test_operate():
	with pytest.raises(TypeError) as excinfo:
		problem3.operate(3,2,3)
	assert excinfo.value.args[0]=="oper must be a string"
	assert problem3.operate(3,4, "+")==7, "addition is incorrect"
	assert problem3.operate(3,4, "-")==-1, "subtraction is incorrect"
	assert problem3.operate(3,4, "*")==12, "multiplication is incorrect"
	with pytest.raises(ZeroDivisionError) as excinfo:
		problem3.operate(3,0,"/")
	assert excinfo.value.args[0]=="division by zero is undefined"
	assert problem3.operate(8,4, "/")==2, "multiplication is incorrect when result is integer"
	assert problem3.operate(4,8, "/")==0.5, "multiplication is incorrect when result is float"
	with pytest.raises(ValueError) as excinfo:
		problem3.operate(3,4,"add")
	assert excinfo.value.args[0]=="oper must be one of '+', '/', '-', or '*'"

