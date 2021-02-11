"""A vaccination calculator."""

__author__ = "730325562"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
today: datetime = datetime.today()
Population = int(input("Population: "))
Doses_administered = int(input("Doses administered: "))
Doses_per_day = int(input("Doses per day: "))
Target_vaccinations = int(input("Target percent vaccinated: "))
Population_left_to_vaccinate = Population - (Doses_administered / 2)
Days_left_to_vaccinate_everyone: int = (Population_left_to_vaccinate / (Doses_per_day / 2))
Days_left: int = round(Days_left_to_vaccinate_everyone * Target_vaccinations / 100)
Days_til_completion: timedelta = timedelta(Days_left)
Day_of_completion: datetime = today + Days_til_completion
print("We will reach " + str(Target_vaccinations) + "% vaccination in " + str(Days_left) + " days, which falls on " + Day_of_completion.strftime("%B %d %Y"))
