import json
import base64
import qrcode
import uuid

def main():
    data = read_and_process_data()
    generate_qr(data)

def read_and_process_data(data_file = "data.json"):
    with open(data_file, 'r') as data:
            reader = json.load(data)
            json_string = json.dumps(reader)
            base64_data = base64.b64encode(json_string.encode('utf-8'))
            return base64_data

def generate_qr(data, error_correct_level = qrcode.constants.ERROR_CORRECT_H, fill = "black", back = "white"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=error_correct_level,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color = fill, back_color = back)
    random_id = str((uuid.uuid4()))[:5]
    img.save(f'generated/qr-{random_id}.png')

if __name__ == "__main__":
    main()