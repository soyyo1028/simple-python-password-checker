# Simple Python Password Checker

A simple Python-based password strength checker that analyzes password security using different validation rules and a scoring system.

## Features

* Checks minimum password length
* Detects uppercase and lowercase letters
* Detects numbers
* Detects special characters
* Detects common passwords
* Password score system from 0 to 10
* Strength classification:

  * Very Weak
  * Weak
  * Moderate
  * Strong

## Requirements

* Python 3

## How to Run

Open a terminal in the project folder and run:

```
python password_checker.py
```

## Example

```
Enter your password: SecurePass

➔  Your password must contain at least one number.
➔  Your password must contain at least one special character.
⬆️ Flags found. ⬆️

Score: 6/10 (Moderate password)
```

## Technologies Used

* Python
* os
* time

## Author

soyyo1028
