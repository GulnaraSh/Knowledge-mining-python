from mypackage.functions import power
from mypackage.greet import SayHello

def test_functions(): 
	SayHello("Mark")
	x=power(3,2)
	assert x == 9