"""
Models for Products, Categories and Orgins.
"""
from django.db import models


# ------------------------------------------- #
#               CATEGORY MODEL                #
# ------------------------------------------- #
class Category(models.Model):
    """
    Model for categories in products.
    """

    class Meta:
        """
        To ensure the plural of Catergory is correcrly specified.
        """
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Return category friendly names
        """
        return self.friendly_name


# ------------------------------------------- #
#               ORGIN MODEL                   #
# ------------------------------------------- #
class Origin(models.Model):
    """
    Model for orgin in products. It will indicate from where the
    coffee products orginate from (country).
    """

    name = models.CharField(max_length=50)
    friendly_name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        """
        Return Orgin friendly names
        """
        return self.friendly_name


# ------------------------------------------- #
#               PRODUCTS MODEL                #
# ------------------------------------------- #
class Product(models.Model):
    """
    Model for the products. It links to the above to models by
    foreign key. Other fields include the product id, product name,
    product description, the price, intensity for coffee products and
    an image.
    """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    origin = models.ForeignKey('Origin', null=True, blank=True,
                               on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    intensity = models.CharField(max_length=20, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
