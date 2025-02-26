import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from crud_blog_web.models import Article


class Command(BaseCommand):
    help = "Czyści tabelę i generuje przykładowe produkty"
    dataset = [
        {
            "title": "02 April 2001",
            "content": "Analiza trendów w e-commerce",
            "year": 2025,
            "image": None,
        },
    ]

    def random_date(self, start_date, end_date):
        """
        Generowanie losowej daty w przedziale od start_date do end_date
        """
        start = datetime.strptime(start_date, '%Y-%m-%d')
        end = datetime.strptime(end_date, '%Y-%m-%d')
        delta = end - start
        random_days = random.randint(0, delta.days)
        return start + timedelta(days=random_days)

    def handle(self, *args, **kwargs):
        # Czyszczenie tabeli
        self.stdout.write("Czyszczenie tabeli ScientificResearch...")
        Article.objects.all().delete()
        self.stdout.write("Tabela została wyczyszczona.")

        # Generowanie nowych danych
        for item in self.dataset:
            random_date = self.random_date('2001-01-01', '2025-01-01')
            Article.objects.create(
                title=item["title"],
                content=item["content"],
                year=item["year"],
                image=item["image"],
                created_at=random_date,
                updated_at=random_date,
            )

        self.stdout.write(self.style.SUCCESS("Utworzono przykładowy artykul!"))