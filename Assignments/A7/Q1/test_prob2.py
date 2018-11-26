import problem2

def test_month():
	assert problem2.month_length("June")==30, "Wrong number of days for a month with 30 days"
	assert problem2.month_length("November")==30, "Wrong number of days for a month with 30 days"		
	assert problem2.month_length("December")==31, "Wrong number of days for a month with 31 days"
	assert problem2.month_length("May")==31, "Wrong number of days for a month with 31 days"
	assert problem2.month_length("February")==28, "Leap year was not specified, but calculation was done on the basis of leap years"
	assert problem2.month_length("February", leap_year=True)==29, "Leap year was specified, but calculation was done on the basis of non-leap years"
	assert problem2.month_length(None)==None, "Blank response did not generate None type"
	assert  problem2.month_length("june")==None, "Incorrect capitalization was treated as correct spelling"
	assert  problem2.month_length("Septembre")==None, "Incorrect spelling was treated as correct spelling"

