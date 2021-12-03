def start():
	print(r"""
~====================================================================~
            _             __           _           _               _ 
           | |            \ \         | |         | |             (_)
  ___    __| |    ______   \ \      __| |   __ _  | |__    _ __    _ 
 / _ \  / _` |   |______|   > >    / _` |  / _` | | '_ \  | '_ \  | |
|  __/ | (_| |             / /    | (_| | | (_| | | | | | | | | | | |
 \___|  \__,_|            /_/      \__,_|  \__,_| |_| |_| |_| |_| |_|

 ~====================================================================~
Encoder - Decoder by dahni
V -> 1.2		                                                                     
		""")

codificación = {
    '1' : '3TKA',
    '2' : '9qh6',
    '3' : 'aSÑc',
    '4' : '4llh',
    '5' : 'f2vt',
    '6' : 'pQKA',
    '7' : 'yÑI7',
    '8' : 'XOXW',
    '9' : 'kXÑr',
    '0' : 'EXj8',
    'a' : 'Efw9',
    'b' : 'SCV6',
    'c' : 'FZbE',
    'd' : 'Xi8x',
    'e' : 'bHDg',
    'f' : 'Vd8K',
    'g' : '2qaj',
    'h' : 'jRWI',
    'i' : '7xuM',
    'j' : 'WMiN',
    'k' : 'L0vT',
    'l' : 'cZVO',
    'm' : '9Fnñ',
    'n' : 'ip6I',
    'ñ' : 'tbXi',
    'o' : 'Dy1W',
    'p' : 'gevC',
    'q' : 'Kvu2',
    'r' : 'VpkZ',
    's' : 'SsWR',
    't' : 'V1IQ',
    'u' : 'vpsm',
    'v' : 'SkoN',
    'w' : 'kLQd',
    'x' : 'jLLi',
    'y' : '5b2B',
    'z' : '4XD3',
    'A' : 'FnX9',
    'B' : 'IMTR',
    'C' : 'wJtY',
    'D' : '93D2',
    'E' : 'iMyZ',
    'F' : '9VjÑ',
    'G' : 'Zhla',
    'H' : 'SISZ',
    'I' : 'n8UÑ',
    'J' : 'ojEM',
    'K' : 'OGqy',
    'L' : 'RuT9',
    'M' : 'nNjI',
    'N' : 'EqhJ',
    'Ñ' : '3ñcn',
    'O' : '5tUo',
    'P' : 'JxLg',
    'Q' : 'OqR4',
    'R' : 'sla8',
    'S' : 'WFdÑ',
    'T' : 'N9Pf',
    'U' : '0IUe',
    'V' : 'ERCT',
    'W' : 'bRV1',
    'X' : 'ubJñ',
    'Y' : 'dP6R',
    'Z' : '7ZvT',
    '!' : 'HT1q',
    '"' : 'xñQf',
    '·' : '7Rxz',
    '$' : 'z6Wi',
    '%' : 'tHMa',
    '&' : 'V9hS',
    '/' : 'U7pI',
    '(' : 'tLt3',
    ')' : 'XWX5',
    '=' : 'LDP4',
    '?' : 'JÑ9e',
    '¿' : '1c1M',
    '^' : '9iDi',
    '*' : 'swO7',
    '¨' : 'sILB',
    'Ç' : 'R2ih',
    '_' : 'lOVI',
    ':' : 't3uX',
    ';' : 'p0DQ',
    '>' : '4YuR',
    '<' : 'PhXA',
    ',' : 'QpW0',
    '.' : '1Mg9',
    '´' : '8Ñlñ',
    'ç' : '78bñ',
    '`' : 'df62',
    '+' : 'MfMR',
    '¡' : 'OHlD',
    "'" : 'EVwW',
    '"' : 'LKRS',
    'º' : 'nnBn',
    " " : 'ackD',
    'ª' : 'vjEj',
    '|' : 'Q3An',
    '@' : 'MgNb',
    '#' : 'pey4',
    '~' : 'aeñG',
    '€' : 'heHF',
    '¬' : 'iBmR',
    '{' : 'mUSZ',
    '}' : '02TF',
    '[' : '3b2Ñ',
    ']' : 'jADg'
}
decodificación = {
    '3TKA' : '1', 
    '9qh6' : '2', 
    'aSÑc' : '3', 
    '4llh' : '4', 
    'f2vt' : '5', 
    'pQKA' : '6', 
    'yÑI7' : '7', 
    'XOXW' : '8', 
    'kXÑr' : '9', 
    'EXj8' : '0', 
    'Efw9' : 'a', 
    'SCV6' : 'b', 
    'FZbE' : 'c', 
    'Xi8x' : 'd', 
    'bHDg' : 'e', 
    'Vd8K' : 'f', 
    '2qaj' : 'g', 
    'jRWI' : 'h', 
    '7xuM' : 'i', 
    'WMiN' : 'j', 
    'L0vT' : 'k', 
    'cZVO' : 'l', 
    '9Fnñ' : 'm', 
    'ip6I' : 'n', 
    'tbXi' : 'ñ', 
    'Dy1W' : 'o', 
    'gevC' : 'p', 
    'Kvu2' : 'q', 
    'VpkZ' : 'r', 
    'SsWR' : 's', 
    'V1IQ' : 't', 
    'vpsm' : 'u', 
    'SkoN' : 'v', 
    'kLQd' : 'w', 
    'jLLi' : 'x', 
    '5b2B' : 'y', 
    '4XD3' : 'z', 
    'FnX9' : 'A', 
    'IMTR' : 'B', 
    'wJtY' : 'C', 
    '93D2' : 'D', 
    'iMyZ' : 'E', 
    '9VjÑ' : 'F', 
    'Zhla' : 'G', 
    'SISZ' : 'H', 
    'n8UÑ' : 'I', 
    'ojEM' : 'J', 
    'OGqy' : 'K', 
    'RuT9' : 'L', 
    'nNjI' : 'M', 
    'EqhJ' : 'N', 
    '3ñcn' : 'Ñ', 
    '5tUo' : 'O', 
    'JxLg' : 'P', 
    'OqR4' : 'Q', 
    'sla8' : 'R', 
    'WFdÑ' : 'S', 
    'N9Pf' : 'T', 
    '0IUe' : 'U', 
    'ERCT' : 'V', 
    'bRV1' : 'W', 
    'ubJñ' : 'X', 
    'dP6R' : 'Y', 
    '7ZvT' : 'Z', 
    'HT1q' : '!', 
    'xñQf' : '"', 
    '7Rxz' : '·', 
    'z6Wi' : '$', 
    'tHMa' : '%', 
    'V9hS' : '&', 
    'U7pI' : '/', 
    'tLt3' : '(', 
    'XWX5' : ')', 
    'LDP4' : '=', 
    'JÑ9e' : '?', 
    '1c1M' : '¿', 
    '9iDi' : '^', 
    'swO7' : '*', 
    'sILB' : '¨', 
    'R2ih' : 'Ç', 
    'lOVI' : '_', 
    't3uX' : ':', 
    'p0DQ' : ';', 
    '4YuR' : '>', 
    'PhXA' : '<', 
    'QpW0' : ',', 
    '1Mg9' : '.', 
    '8Ñlñ' : '´', 
    '78bñ' : 'ç', 
    'df62' : '`', 
    'MfMR' : '+', 
    'OHlD' : '¡', 
    'EVwW' : "'", 
    'LKRS' : '"', 
    'nnBn' : 'º', 
    'ackD' : " ", 
    'vjEj' : 'ª', 
    'Q3An' : '|', 
    'MgNb' : '@', 
    'pey4' : '#', 
    'aeñG' : '~', 
    'heHF' : '€', 
    'iBmR' : '¬', 
    'mUSZ' : '{', 
    '02TF' : '}', 
    '3b2Ñ' : '[', 
    'jADg' : ']'
}

def encode(text : str):
	lista = []
	try:
		for letters in text:
			lista.append(codificación[letters])
		lista.append("~~")
		final = "".join(lista)
		print("~---------------------------------------~")
		print(final)
		print("~---------------------------------------~")
	except:
		print("[?] This encoder doesn´t handle letters with accent marks")

def decode(text : str):
	lista = []
	num_one = 0
	num_two = 4
	prg = text
	for x in range(len(prg)):
		try:
			lista.append(decodificación[prg[num_one:num_two]])
			num_one += 4
			num_two += 4
		except:
			pass
	final = "".join(lista)
	print("~---------------------------------------~")
	print(final)
	print("~---------------------------------------~")

if __name__ == "__main__":
	start()
	print("[+] Write 1 to encode")
	print("[+] Write 2 to decode")
	prg = input("[?]Number>> ")
	if prg == '1':
		prg_2 = str(input("[+] Encode>> "))
		encode(prg_2)
	elif prg == '2':
		prg_3 = str(input("[+] Decode>> "))
		decode(prg_3)
	else:
		pass