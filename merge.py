def merge(n1, n2):
	"""Merge two descending numbers into one large number in descending order."""
	if n1 == 0 or n2 == 0:
		return n1 + n2
	def keep_mergin(n1, n2, new=0, k=0):
		base = 10 ** k
		num1 = n1 % 10
		num2 = n2 % 10
		if n1 == 0 and n2 == 0:
		    return new
		elif n1 == 0 and n2 != 0:
                    new = new + (num2 * base)
                    n2 = (n2 - num2) // 10
		elif n1 != 0 and n2 == 0:
		    new = new + (num1 * base)
		    n1 = (n1 - num1) // 10
		elif num1 >= num2:
		    new = new + (num2 * base)
		    n2 = (n2 - num2) // 10
		else:
		    new = new + (num1 * base)
		    n1 = (n1 - num1) // 10
		return keep_mergin(n1, n2, new, k+1)
	return keep_mergin(n1, n2)
