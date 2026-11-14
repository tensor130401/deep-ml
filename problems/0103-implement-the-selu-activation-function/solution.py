def selu(x: float) -> float:
    """
    Implements the SELU (Scaled Exponential Linear Unit) activation function.

    Args:
        x: Input value

    Returns:
        SELU activation value
    """
    alpha = 1.6732632423543772
    scale = 1.0507009873554804
    # Your code here
    val=0
    if x>0:
        val=scale*x
    else:
        val=scale*alpha*(2.718281828459045**x-1)
    return round(val,4)
    pass