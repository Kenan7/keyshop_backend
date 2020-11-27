from django.core.management.base import BaseCommand, CommandError
from product.models import Category, Compability, Product

categories = ["Ofis", "Eğlence"]
compabilities = ["Windows", "MacOS", "Android", "iOS", "Linux"]


class Command(BaseCommand):

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)

    def handle(self, *args, **options):
        print("Creating categories...")
        for item in categories:
            Category.objects.create(name=item)
        print("Categories created")
        print("-" * 10)
        print("Creating compabilities...")
        for item in compabilities:
            Compability.objects.create(name=item)
        print("Compabilities created")
