import warnings

warnings.filterwarnings("error", category=UserWarning)
try:
    warnings.warn("This is a warning!", UserWarning)
except UserWarning as e:
    print("Caught as error:", e)