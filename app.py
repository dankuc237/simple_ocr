from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import pytesseract
import io
import base64

app = Flask(__name__)

def ocr_image(image):
    # Funkcja do wykonywania OCR na obrazie
    extracted_text = pytesseract.image_to_string(image,lang='pol+eng')
    return extracted_text

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' in request.files:
            
            image_files = request.files.getlist('image')

            extracted_texts=[]
            image_datas=[]
            
            for image_file in image_files:
                if image_file.filename != '':
                    # Odczyt obrazka przekazanego przez formularz
                    image = Image.open(image_file)
                    # Wywołanie funkcji OCR
                    extracted_text = ocr_image(image)
                    extracted_texts.append(extracted_text)
                    
                    # wyswietlenie obrazu
                    data = io.BytesIO()
                    image.save(data, "JPEG")
                    encoded_img = base64.b64encode(data.getvalue())
                    decoded_img = encoded_img.decode('utf-8')
                    image_data = f"data:image/jpeg;base64,{decoded_img}"
                    image_datas.append(image_data)
            data=zip(image_datas,extracted_texts)        
            return render_template('index.html', data=data)

    return render_template('index.html', data=None)

if __name__ == '__main__':
    app.run(debug=True)




