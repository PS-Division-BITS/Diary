from django.core.management.base import BaseCommand
from PS2.models import *
import csv, random
from django.contrib.auth.models import User

class Command(BaseCommand):
	def _create(self):
		rm -r /PS-Diary/databaseEntriesAsCsv.csv

	def handle(self, *args, **options):
		self._create()
