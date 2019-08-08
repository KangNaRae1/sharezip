class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save) # 해당 이름으로 컴퓨터에 저장
        img = Image.open(self.path)     # 이미지 객체로 열기
        size = (128, 128)
        img.thumbnail(size, Image.ANTIALIAS) # Thumb 이미지 만들기

        background = Image.new('RGBA', size, (255, 255, 255, 0))
        background.paste(img, (int((size[0]-img.size[0])/2), int((size[1]-img.size[1])/2) ))
        background.save(self.thumb_path, 'JPEG')   # thumb 저장

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)

class ThumbnailImageField(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=128, thumb_height=128, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageField, self).__init__(*args, **kwargs)