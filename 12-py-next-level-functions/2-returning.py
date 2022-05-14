#-----------------------------------#
print('-'*50)
def checkPage(page):
    def checkRole(role):
        role = role.lower()
        if role == 'admin':
            return f"'{role}' can see the '{page}' page"
        else:
            return f"'{role}' can't see the '{page}' page"
    return checkRole

adminUser = checkPage('Analytics')
result = adminUser('Admin')
print(result)

user1 = checkPage('Administrator')
result = user1('User')
print(result)

#-----------------------------------#
print('-'*50)
def operator(operate):
    def plus(*args):
        result=0
        for i in args:
            result += i
        return result

    def multiple(*args):
        result=1
        for i in args:
            result *= i
        return result
    
    operate=operate.lower()
    if operate == 'plus' :
        return plus
    else:
        return multiple
    
value = operator("plus")
print(value(1,2,3,4,5))