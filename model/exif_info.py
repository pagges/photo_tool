class ExifInfo(object):
    # 相机制造厂商
    cameraMaker = ""
    # 相机型号
    cameraModel = ""
    # 拍摄时间
    shotTime = ""
    # 焦距
    focalLength = ""
    # iso
    iSOSpeedRatings = ""
    # 快门
    exposureTime = ""
    # 镜头厂商
    lensMake = ""
    # 镜头型号
    lensModel = ""
    # 光圈
    fNumber = ""
    # 照片方向
    orientation = 0

    def __init__(self, cameraMaker, cameraModel, shotTime, focalLength, iSOSpeedRatings, exposureTime, fNumber,
                 orientation):
        self.cameraMaker = cameraMaker
        self.cameraModel = cameraModel
        self.shotTime = shotTime
        self.focalLength = focalLength
        self.iSOSpeedRatings = iSOSpeedRatings
        self.exposureTime = exposureTime
        self.fNumber = fNumber
        self.orientation = orientation

    def getExifMessage(self):
        camearMakerMsg = self.cameraMaker
        camerModelMsg = self.cameraModel
        focalLengthMsg = "@{}mm".format(
            self.focalLength) if self.focalLength != None and int(self.focalLength) >= 0 else None
        exposureTimeMsg = "{}Sec".format(self.exposureTime) if self.exposureTime != None else None
        fNumberMsg = "F/{}".format(self.fNumber) if self.fNumber != None and self.fNumber != '0' else None
        isoMsg = "ISO{}".format(self.iSOSpeedRatings) if self.iSOSpeedRatings != None else None
        msgList = list([camearMakerMsg, camerModelMsg, focalLengthMsg, exposureTimeMsg, fNumberMsg, isoMsg])
        return ' '.join(list(filter(None, msgList)))
