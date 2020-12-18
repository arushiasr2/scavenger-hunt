import qrcode
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        phrase = "Together we build University of Tomorrow"
        phrase_list = phrase.split(' ')
        url = "https://localhost:8002/?"
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=6,
            border=4,
        )
        count = 1
        for phrase in phrase_list:
            qr.data_list = []
            qr.add_data(url+'input{}='.format(count)+phrase)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save('image_{}.png'.format(count))
            count += 1
            print('--------------QR code created--------------')
