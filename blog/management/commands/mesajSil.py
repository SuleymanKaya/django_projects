from django.core.management.base import BaseCommand
from blog.models import IletisimModel

class Command(BaseCommand):
    help = "Verilen emaillere göre iletişime gelen mailleri sil"

    def add_arguments(self, parser):
        parser.add_argument('--email', help='email adresi giriniz')

    def handle(self, **options):
        if options.get('email') is None:
            IletisimModel.objects.all().delete()
            self.stdout.write('Tüm maillere ait mesajlar silindi')
        else:
            IletisimModel.objects.filter(email = options.get('email')).delete()
            self.stdout.write(options.get('email') + ' mailine ait tüm mesajlar silindi') 
        