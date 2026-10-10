# # language: Python, file: crack_test.py, target: MyTestX-style test EXEs
# # Forces the answer-correct flag (byte at [ebp-49h]) to always 1

# import sys
# from pathlib import Path

# def crack(data: bytes) -> bytes:
#     data = data.replace(b"\xc6\x45\xb7\x00", b"\xc6\x45\xb7\x01")
#     return data

# def main():
#     if len(sys.argv) < 2:
#         print(f"Usage: {sys.argv[0]} <input.exe> [output.exe]")
#         sys.exit(1)

#     src = Path(sys.argv[1])
#     dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("Cracked.exe")

#     raw = src.read_bytes()
#     patched = crack(raw)

#     print(f"flag=0 stores: {raw.count(b'\xc6\x45\xb7\x00')} → {patched.count(b'\xc6\x45\xb7\x00')}")
#     print(f"flag=1 stores: {raw.count(b'\xc6\x45\xb7\x01')} → {patched.count(b'\xc6\x45\xb7\x01')}")

#     dst.write_bytes(patched)
#     print(f"Wrote {dst} ({dst.stat().st_size} bytes)")

# if __name__ == "__main__":
#     main()


import sys
from pathlib import Path

def crack(data: bytes) -> bytes:
    return data.replace(b"\xc6\x45\xb7\x00", b"\xc6\x45\xb7\x01")

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <input.exe> [output.exe]")
        sys.exit(1)

    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("Cracked.exe")

    if not src.is_file():
        print(f"Error: file not found: {src}")
        sys.exit(1)

    raw = src.read_bytes()
    patched = crack(raw)

    count_before = raw.count(b"\xc6\x45\xb7\x00")
    count_after = patched.count(b"\xc6\x45\xb7\x01")

    print(f"Replaced {count_before - count_after} occurrence(s) of \\xc6\\x45\\xb7\\x00 -> \\xc6\\x45\\xb7\\x01")
    print(f"Wrote {dst} ({dst.stat().st_size} bytes)" if dst.exists() else "File written successfully.")

    dst.write_bytes(patched)

if __name__ == "__main__":
    main()