# Password Strength Checker

A Python command-line tool that evaluates password strength based on length and character diversity.

## Features
- Checks for minimum length (8 characters)
- Validates presence of uppercase letters, lowercase letters, numbers, and special characters
- Scores passwords from Weak to Very Strong
- Interactive loop allows multiple password attempts
- Provides immediate feedback on password quality

## How to Run
```bash
python password_checker.py
```

## Scoring System
- **Very Strong**: 12+ characters with all character types
- **Strong**: Contains 3+ character types
- **Medium**: Contains 2 character types
- **Weak**: Contains fewer than 2 character types or is too short

## What I Learned
- Using `any()` with generator expressions for efficient checking
- Implementing a scoring system with boolean logic
- Building interactive CLI applications with user feedback loops

## Future Improvements
- Add common password dictionary check
- Implement entropy calculation
- Create GUI version
- Add password generation feature