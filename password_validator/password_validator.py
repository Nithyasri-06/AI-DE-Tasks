def check_character(password):
  is_upper=False
  is_lower=False
  is_digit=False
  is_special=False
  for ch in password:
    if ch.isspace():
        return None,None,None,None,"invalid"
    elif ch.isupper():
        is_upper=True
    elif ch.islower():
        is_lower=True
    elif ch.isdigit():
        is_digit=True
    else:
        is_special=True
  return is_upper,is_lower,is_digit,is_special,"valid"

def password_strength(password,upper,lower,digit,special):
    score=0
    if len(password)<8:
        print("Weak password")
        return
    if len(password)>=8:
      score+=1
    if upper:
      score+=1
    if lower:
      score+=1
    if digit:
      score+=1
    if special:
      score+=1
    
    if score==5:
      print("Strong password")
    elif score>=3:
      print("Medium password")
    else:
      print("Weak password")

def main():
    password=input("Enter the password : ")
    if password=="":
        print("Error:Empty password")
    else:
        upper,lower,digit,special,status=check_character(password)
        if status=="valid":
           password_strength(password,upper,lower,digit,special)
        else:
            print("Error:Password contains invalid characters(tabs/spaces not allowed)")
        
main()

