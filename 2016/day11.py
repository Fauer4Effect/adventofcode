'''
NOT COMPLETE
'''
entity = ["HG","HM","LG","LM"]
path = []

def irradiate(x,y):
	if x =="HG" and y=="HM": return False
	elif x=="LG" and y=="LM": return False
	else: return True

def safe_pair(x,y):
	if irradiate(x,y) or irradiate(y,x): return False
	else: return True

def state_of(who, state):
	try: return state[who]
	except KeyError:
		state[who] = False
		return False
