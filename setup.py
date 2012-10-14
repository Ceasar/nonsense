from distutils.core import setup
import nonsense

setup(
    name="nonsense",
    version=nonsense.__version__,
    description="A stationary source object, suitable for creating" + \
        " sequences of random data with fixed conditional probabilities.",
    author="Ceasar Bautista",
    author_email="cbautista2010@gmail.com",
    url="http://www.github.com/Ceasar/Nonsense",
    py_modules=['nonsense'],
)

    
