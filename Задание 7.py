def password_level(password):
    if len(password) < 6:
        return "Недопустимый пароль"

    has_digit = any(char.isdigit() for char in password)
    has_lower = any(char.islower() for char in password)
    has_upper = any(char.isupper() for char in password)

    if has_digit and not has_lower and not has_upper:
        return "Ненадежный пароль"
    elif not has_digit and (has_lower or has_upper):
        return "Ненадежный пароль"
    elif has_digit and (has_lower or has_upper):
        if has_lower and has_upper:
            return "Надежный пароль"
        else:
            return "Слабый пароль"
    else:
        return "Ненадежный пароль"