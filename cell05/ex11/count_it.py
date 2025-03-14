import sys

if len(sys.argv) == 1:
    print("none")
else:
    num_params = len(sys.argv) - 1
    print(f"parameters: {num_params}")
    for i in range(1, len(sys.argv)):
        print(f"{sys.argv[i]}: {len(sys.argv[i])}")