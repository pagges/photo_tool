import exifread
from loguru import logger
import re
from model.exif_info import ExifInfo


def get_exif_info(image_file):
    try:
        f = open(image_file, 'rb')
        tagsDict = exifread.process_file(f)
        cameraMakerKey = 'Image Make'
        cameraModelKey = 'Image Model'
        shotTimeKey = 'Image DateTime'
        exposureTimeKey = 'EXIF ExposureTime'
        fNumberKey = 'EXIF FNumber'
        isoKey = 'EXIF ISOSpeedRatings'
        focalLength = 'EXIF FocalLength'
        orientationTag = 'Image Orientation'

        # 相机厂商
        cameraMaker = str(tagsDict[cameraMakerKey]).strip() if (cameraMakerKey in tagsDict) else None
        # 相机型号
        cameraModel = str(tagsDict[cameraModelKey]).strip() if (cameraModelKey in tagsDict) else None
        # 拍摄时间
        shotTime = str(tagsDict[shotTimeKey]).strip() if (shotTimeKey in tagsDict) else None
        # 快门
        exposureTime = str(tagsDict[exposureTimeKey]).strip() if (exposureTimeKey in tagsDict) else None
        # 光圈
        fNumberTag = str(tagsDict[fNumberKey]).strip() if (fNumberKey in tagsDict) else None
        fNumber = _get_float_form_exif_value(fNumberTag)
        # iso
        iso = str(tagsDict[isoKey]).strip() if (fNumberKey in tagsDict) else None
        # 焦距
        focalLengthTag = str(tagsDict[focalLength]).strip() if (focalLength in tagsDict) else None
        focalLength = _get_float_form_exif_value(focalLengthTag)
        # 拍摄方向
        orientationTag = str(tagsDict[orientationTag]).strip() if (orientationTag in tagsDict) else ""
        numItem = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(orientationTag))]
        orientation = numItem[0] if (len(numItem) > 0) else 0

        return ExifInfo(cameraMaker, cameraModel, shotTime, focalLength, iso, exposureTime,
                        fNumber, orientation)
    except Exception as e:
        logger.error("get_exif_info error {}", e)


def _get_float_form_exif_value(str_value):
    if str_value == None:
        return None
    elif str_value == '0':
        return 0
    elif str_value.index('/') > 0:
        index = str_value.index('/')
        left_v = float(str_value[index - 1:index])
        right_v = float(str_value[index + 1:index + 2])
        return float(left_v / right_v)


if __name__ == '__main__':
    f = open("/Users/admin/Downloads/test_image/DSCF1081.JPG", 'rb')
    orientationTag = 'Image Orientation'
    tagsDict = exifread.process_file(f)
    fNumberKey = 'EXIF FNumber'
    fNumber = str(tagsDict[fNumberKey]).strip() if (fNumberKey in tagsDict) else None
    orientationTag = str(tagsDict[orientationTag]).strip() if (orientationTag in tagsDict) else "0"
    print(orientationTag)
    numItem = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(orientationTag))]
    orientation = numItem[0] if (len(numItem) > 0) else 0
    print(orientation)
    print(fNumber)
