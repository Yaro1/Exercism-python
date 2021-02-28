def slices(series, length):
    if length > len(series) or length <= 0 or not series.isdigit():
        raise ValueError("Error in second arg.\nI am sorry!\n")
    return [series[i:i+length] for i in range(len(series) - length + 1)]

