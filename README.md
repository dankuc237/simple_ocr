To run:
```bash
git clone https://github.com/dankuc237/simple_ocr
cd simple_ocr
sudo docker build --tag simple-ocr .
sudo docker images
sudo docker run --network host -p 5000:5000 simple-ocr
```
