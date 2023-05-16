from unittest import TestLoader, TextTestRunner


suite = TestLoader().discover(start_dir="Tests")
TextTestRunner().run(suite)
