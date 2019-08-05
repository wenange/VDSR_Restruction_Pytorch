import numpy as np
def psnr(ori,gro):
    x_x=ori
    y_y=gro
    x=np.array(x_x)
    y=np.array(y_y)
    if len(x.shape)!=len(y.shape):
        raise Exception("x.shape!=y.shape")
    for i,s in enumerate(x.shape):
        if s!=y.shape[i]:
            raise Exception("x.shape!=y.shape")
    MSE=np.sum(np.power(x-y,2))/(x.shape[0]*x.shape[1])
    psnr=10*np.log10(255*255/MSE)
    return psnr


mat = np.array(
    [[65.481, 128.553, 24.966],
     [-37.797, -74.203, 112.0],
     [112.0, -93.786, -18.214]])
mat_inv = np.linalg.inv(mat)
offset = np.array([16, 128, 128])


def rgb2ycbcr(rgb_img):
    ycbcr_img = np.zeros(rgb_img.shape)
    for x in range(rgb_img.shape[0]):
        for y in range(rgb_img.shape[1]):
            ycbcr_img[x, y, :] = np.round(np.dot(mat, rgb_img[x, y, :] * 1.0 / 255) + offset)
    return ycbcr_img


def ycbcr2rgb(ycbcr_img):
    rgb_img = np.zeros(ycbcr_img.shape, dtype=np.uint8)
    for x in range(ycbcr_img.shape[0]):
        for y in range(ycbcr_img.shape[1]):
            [r, g, b] = ycbcr_img[x, y, :]
            rgb_img[x, y, :] = np.maximum(0, np.minimum(255,np.round(np.dot(mat_inv, ycbcr_img[x, y, :] - offset) * 255.0)))
    return rgb_img
