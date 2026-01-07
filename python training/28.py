def access(user):
	match user:
		case "admin" | "manager": return "Full access"
		case "guest": return "limited access"
		case _: return "no access"
print(access("admin"))
print(access("guest"))
print(access("employee"))