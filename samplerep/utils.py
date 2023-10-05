
"""General utilities.
"""


from typing import Union

import numpy as np


def square(value : Union[int, float, np.ndarray]) -> Union[float, np.ndarray]:
	"""Return the square of a given number
	This will accept any input that support the ** operator.
	   
	Function will raise a TypeError for incompatible types such as strings
	   
	Arguments
	---------
	value: number, ndarray
	The input value to square, each element in the ndarray is squared,
	   	
	   	
	Return
	------
	   	The square of the input value : float or ndarray.
	"""

	return value**2
	
	


