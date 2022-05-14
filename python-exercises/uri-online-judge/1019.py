#include <stdio.h>

import datetime

N = 556

formatted = str(datetime.timedelta(seconds=N))

print(formatted)