token_dict = dict()

token_dict['A'] = [0,4,4,9,1,4,8,5,9,7]
token_dict['B'] = [3,2,2,5,1,8,1,1,3,0]
token_dict['C'] = [9,6,8,4,3,0,6,6,9,9]
token_dict['D'] = [3,2,5,8,2,3,5,1,6,9]
token_dict['E'] = [6,0,0,7,8,2,9,2,2,3]
token_dict['F'] = [0,5,6,7,1,8,7,6,8,4]
token_dict['G'] = [1,7,5,4,2,1,0,7,5,4]
token_dict['H'] = [5,4,7,6,1,9,8,3,9,4]
token_dict['J'] = [6,7,3,7,1,0,3,0,2,5]
token_dict['K'] = [6,7,4,8,8,0,5,3,2,9]

print (token_dict)
token = ''
while True:
	for i in range(4):
		question =  input('Please input\n')
		key = question[0].upper()
		value = int(question[1])
		print ('your input is %s%s'%(key,value))
		code = token_dict[key][value]
		token += str(code)

	print (token) 

	cont = input('finished?')
	if cont in ['y','Y','']:
		break
	else:
		token =''
		print("\n")
