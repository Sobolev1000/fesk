import math


class Fesk:
	def convert_sec(sec):
		sec = sec % (24 * 3600) 
		hour = sec // 3600 
		sec %= 3600 
		min = sec // 60 
		sec %= 60 
		return "%02d:%02d:%02d" % (hour, min, sec)
	def human_read_format(size):
    	pwr = math.floor(math.log(size, 1024))
    	suff = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ", "ЭБ", "ЗБ", "ЙБ"]
    	if size > 1024 ** (len(suff) - 1):
       	 return "не знаю как назвать такое число :)"
    	return f"{size / 1024 ** pwr:.0f}{suff[pwr]}"