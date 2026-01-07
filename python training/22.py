def checkvowel(n):
	match n:
		case 'a': return "vowel alphabet"
		case 'e': return "vowel alphabet"
		case 'i': return "vowel alphabet"
		case 'o': return "vowel alphabet"
		case 'u': return "vowel alphabet"
		case _: return "simple alphabet"

print(checkvowel('a'))
print(checkvowel('m'))
print(checkvowel('u'))
	