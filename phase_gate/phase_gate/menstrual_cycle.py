from datetime import datetime, timedelta
def my_menstrual_cycle_calculator(cycle_length, last_period_date):
	if cycle_length < 21 or cycle_length > 35:
		return "please seek medical attention."

	last_period = datetime.strptime(last_period_date, "%d-%m-%Y")
	next_menstrual_period = last_period + timedelta(days=cycle_length)
	ovulation_date = next_menstrual_period - timedelta(days=14)
	fertile_start = ovulation_date + timedelta(days=5)
	fertile_end = ovulation_date - timedelta(days=2)

	return {
        "Your next menstrual cycle": next_menstrual_period.strftime("%d-%m-%Y"),
        "Your ovulation date": ovulation_date.strftime("%d-%m-%Y"),
        "Fertile window start": fertile_start.strftime("%d-%m-%Y"),
        "Fertile window end": fertile_end.strftime("%d-%m-%Y"),
        "Safe days are before": fertile_start.strftime("%d-%m-%Y"),
        "Safe days after": next_menstrual_period.strftime("%d-%m-%Y")
    }

cycle_length = int(input("What is the length of your cycle: "))
last_period_date = input("When was your last period (date-month-year): ")
print(my_menstrual_cycle_calculator(cycle_length, last_period_date))
		