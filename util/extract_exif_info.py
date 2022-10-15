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
        fNumber = str(tagsDict[fNumberKey]).strip() if (fNumberKey in tagsDict) else None
        # iso
        iso = str(tagsDict[isoKey]).strip() if (fNumberKey in tagsDict) else None
        # 焦距
        focalLength = str(tagsDict[focalLength]).strip() if (focalLength in tagsDict) else None
        # 拍摄方向
        orientationTag = str(tagsDict[orientationTag]).strip() if (orientationTag in tagsDict) else ""
        numItem = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(orientationTag))]
        orientation = numItem[0] if (len(numItem) > 0) else 0

        return ExifInfo(cameraMaker, cameraModel, shotTime, focalLength, iso, exposureTime,
                        fNumber, orientation)
    except Exception as e:
        logger.error("get_exif_info error {}", e)


if __name__ == '__main__':
    f = open("./input/3.JPG", 'rb')
    orientationTag = 'Image Orientation'
    tagsDict = exifread.process_file(f)
    orientationTag = str(tagsDict[orientationTag]).strip() if (orientationTag in tagsDict) else "0"
    print(orientationTag)
    numItem = [int(s) for s in re.findall(r'-?\d+\.?\d*', str(orientationTag))]
    orientation = numItem[0] if (len(numItem) > 0) else 0
    print(orientation)
