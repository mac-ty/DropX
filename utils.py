import socket
import qrcode
import os


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
    except Exception:
        ip = "127.0.0.1"
    finally:
        s.close()
    return ip


def generate_qr(url: str, output_path: str = "static/qr_code.png"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    qr = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#22C55E", back_color="transparent")
    img.save(output_path)
    return output_path


if __name__ == "__main__":
    print(f"Local IP address: {get_local_ip()}")