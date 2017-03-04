import string
import random
import base64

def base64ToImage(string_b64, file_dir):
	if string_b64 != '':
		random_name = ''.join(random.choice(string.ascii_uppercase+string.digits) for _ in range(20))
		dir_name = 'TuCocinas/static/img/'+file_dir+'/'+random_name+'.jpeg'
		image_result = open(dir_name, 'wb')
		image_result.write(base64.b64decode(str(string_b64)))
		image_result.close()
	else:
		dir_name = None
	return dir_name