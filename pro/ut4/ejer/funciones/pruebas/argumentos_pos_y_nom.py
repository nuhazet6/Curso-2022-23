def build_cpu(vendor, num_cores, freq):
    return dict(
        vendor=vendor,
        num_cores=num_cores,
        freq=freq
    )

print(build_cpu('AMD',num_cores=6,freq=3.1))