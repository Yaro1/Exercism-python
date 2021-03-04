def transform(legacy_data):
    return {i.lower(): j for j in legacy_data for i in legacy_data[j]}
