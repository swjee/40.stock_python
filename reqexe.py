import requests
url='https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA1MDRfMzcg%2FMDAxNjIwMDkxMzAwMzQy.ZiY3z_omHFItR8uedmp-6ECBw-3TwmyT7lV0mPta_DYg.f2aunFrFfZgG6akhE96nZt9Pg5g5DNCJpRVKKSwKfHog.JPEG.knocking1%2F1620091202023.jpg&type=sc960_832'
r = requests.get(url,stream=True).raw

from PIL import Image
img = Image.open(r)
print(img.get_format_mimetype)
img.show()
img.save('src.png')

BUF_SIZE=1024
with open('src.png','rb') as sf , open('dst.png','wb') as df:
    while True:
        data = sf.read(BUF_SIZE)
        if not data:
            break;
        df.write(data)


# sha-256  으로 파일 복사검증.

import hashlib

sha_src = hashlib.sha256()
sha_dst = hashlib.sha256()

with open('src.png','rb') as sf ,  open('dst.png','rb') as df:
    sha_src.update(sf.read())
    sha_dst.update(df.read())

print( "src.png's hash: {}".format(sha_src.hexdigest()))
print( "dst.png's hash: {}".format(sha_dst.hexdigest()))

import matplotlib.pyplot as plt
import matplotlib.image as mpimg


dst_img = mpimg.imread('dst.png')

plt.suptitle('Image Processing',fontsize=10)
plt.subplot(1,2,1)
plt.title('Original Image')
plt.imshow(mpimg.imread('src.png') )

plt.subplot(122)
plt.title('Pseudocolor Image')
pseudo_img = dst_img[:,:,0]
plt.imshow(pseudo_img)

plt.show()


