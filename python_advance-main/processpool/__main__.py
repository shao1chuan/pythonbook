import os.path
import time
from concurrent.futures import ProcessPoolExecutor
from urllib.request import urlopen, Request


def download_img(url: str):
    site_url = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(site_url) as web_file:
        img_data = web_file.read()

    if not img_data:
        raise Exception(f"Error: cannot load the image from {url}")

    file_name = os.path.basename(url)
    with open(file_name, 'wb') as file:
        file.write(img_data)

    return f"Download image successfully, {url}"


def main():
    with ProcessPoolExecutor() as executor:
        urls = [
            "https://cdn.pixabay.com/photo/2021/09/28/13/14/cat-6664412_1280.jpg",
            "https://cdn.pixabay.com/photo/2022/11/10/00/38/creative-7581718_640.jpg",
            "https://cdn.pixabay.com/photo/2022/11/19/11/53/rose-7601873_640.jpg",
            "https://cdn.pixabay.com/photo/2022/10/18/12/05/clouds-7530090_640.jpg"
        ]

        results = executor.map(download_img, urls)

        for res in results:
            print(res)


if __name__ == "__main__":
    main()

