
import sys

def is_alpha(char):
	if ord('a') <= ord(char.lower()) <= ord('z'):
		return True
	return False

def is_digit(val):
	try:
		int(val)
		return True
	except ValueError:
		return False

def format_num(num):
	if(int(float(num)) == 0):
		return int(float(num))
	if((float(num) % int(float(num))) == 0):
		num = int(float(num))
		return num
	return num

def parse_string(input_raw):
	#print("parsing string")

	input_raw = input_raw.replace(' ','')
	dict_chars = {}

	for char in input_raw:
		if not is_alpha(char):
			continue
		if char in dict_chars:
			dict_chars[char] = dict_chars[char] + 1
		else:
			dict_chars[char] = 1

	for key in sorted(dict_chars):
		print(str(key) + ": " + str(dict_chars[key]))

def parse_num_seq(user_input):
	#print("parsing num sequence")
	
	summation = 0
	dict_nums = {}

	mode_val = sys.maxsize
	mode_count = 0
	median = 0
	mean = 0

	try:
		user_input = list(map(int, user_input))
		#print("to ints: " + str(user_input))
	except ValueError:
		print("Looks like you have an element in your sequence that is not a number. Please try again")
		return

	user_input.sort()
	#print("sorted: " + str(user_input))

	for element in user_input:
		summation = summation + element

		if element in dict_nums:
			dict_nums[element] = dict_nums[element] + 1
			if dict_nums[element] > mode_count:
				mode_count = dict_nums[element]
				mode_val = element
				#print("mode val: " + str(mode_val) + "  |  mode count: " + str(mode_count))
		else:
			dict_nums[element] = 1

	if (len(user_input) % 2) > 0:
		median = user_input[(len(user_input)/2)]
	else:
		median = (user_input[(len(user_input)/2)] + user_input[(len(user_input)/2 - 1)])/float(2)

	median = format_num("{0:.1f}".format(median))
	mean = format_num("{0:.1f}".format(summation/float(len(user_input))))
	rangeval = user_input[len(user_input)-1] - user_input[0]

	if mode_val == sys.maxsize:
		mode_val = 'none'

	print("mean: " + str(mean))
	print("median: " + str(median))
	print("mode: " + str(mode_val))
	print("range: " + str(rangeval))

def parse_input(user_input):
	if len(user_input) > 0:

		input_raw = user_input
		user_input = user_input.split()
		#print("split: " + str(user_input))

		digit = is_digit(user_input[0])
		#print("element: " + str(user_input[0]))

		if digit:
			parse_num_seq(user_input)
		else:
			parse_string(input_raw)

def main():
	 print('Welcome to the Zenfolio assignment')

	 user_input = raw_input("Please enter a numerical sequence or a literal string: ").replace('"','').strip()

	 while user_input != 'quit':
	 	#print(str(user_input))
	 	parse_input(user_input)
		user_input = raw_input("Please enter a numerical sequence or a literal string: ").replace('"','').strip()


if __name__ == "__main__":
    main()