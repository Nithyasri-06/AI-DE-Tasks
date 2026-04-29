# Password Validator

## Overview

The Password Validator is a Python-based application that evaluates user-provided passwords based on predefined security rules. It validates input and classifies password strength as Weak, Medium, or Strong.

## Features

* Validates password input (rejects empty values and spaces/tabs)
* Checks for:

  * Uppercase letters
  * Lowercase letters
  * Digits
  * Special characters
* Enforces minimum length requirement (8 characters)
* Classifies password strength using a scoring mechanism
* Provides clear error messages for invalid inputs

## Password Strength Criteria

Password strength is determined using a score based on the following:

* +1 → Length ≥ 8
* +1 → Contains uppercase letters
* +1 → Contains lowercase letters
* +1 → Contains digits
* +1 → Contains special characters

**Classification:**

* **Strong** → Score = 5
* **Medium** → Score ≥ 3
* **Weak** → Score < 3

## Example Output

```id="h12k9f"
Enter the password : Hello@123
Strong password
```

```id="c4l2nb"
Enter the password : hello123
Medium password
```

```id="z8q1ra"
Enter the password : hello
Weak password
```

```id="x7m3pl"
Enter the password : hello 123
Error: Password contains invalid characters (tabs/spaces not allowed)
```

```id="r5u8yn"
Enter the password :
Error: Empty password
```

## Summary

This project demonstrates a structured approach to password validation and strength evaluation using rule-based logic, promoting secure password practices.
