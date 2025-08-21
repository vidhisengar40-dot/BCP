def triangle_type(angles):
    """
    angles: iterable of three numbers (degrees)
    returns: string "Right triangle", "Obtuse triangle", "Acute triangle"
    or raises ValueError for invalid angles
    """
    a, b, c = map(float, angles)
    eps = 1e-6

    # Validate angles: positive and sum == 180 (within tolerance)
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Angles must be positive.")
    total = a + b + c
    if abs(total - 180.0) > eps:
        raise ValueError(f"Angles must sum to 180°. Sum is {total}°.")

    # Determine type
    # Right: any angle == 90
    # Obtuse: any angle > 90
    # Acute: all angles < 90
    if abs(a - 90.0) <= eps or abs(b - 90.0) <= eps or abs(c - 90.0) <= eps:
        return "Right triangle"
    if a > 90.0 + eps or b > 90.0 + eps or c > 90.0 + eps:
        return "Obtuse triangle"
    return "Acute triangle"


if __name__ == "__main__":
    try:
        raw = input("Enter three angles in degrees separated by spaces: ").strip().split()
        if len(raw) != 3:
            raise ValueError("Please enter exactly three values.")
        print(triangle_type(raw))
    except Exception as e:
        print("Error:", e)