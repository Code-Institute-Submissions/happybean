from django.db import models


# ------------------------------------------- #
#               CATEGORY MODEL                #
# ------------------------------------------- #
class Category(models.Model):
    """
    Model for categories in products.
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
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
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    intensity = models.CharField(max_length=20, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


# ------------------------------------------- #
#               SIZE MODEL                    #
# ------------------------------------------- #
class Size(models.Model):
    """
    Model for the size names of products.
    """

    class Meta:
        verbose_name_plural = 'Size'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


# ------------------------------------------- #
#           PRODUCT, SIZE & PRICE MODEL       #
# ------------------------------------------- #
class ProductSizePrice(models.Model):
    """
    Model for the linking products to specific pricing related to
    their sizes.
    """
    product = models.ForeignKey('Product', null=True, blank=True,
                                on_delete=models.SET_NULL)
    size = models.ForeignKey('Size', null=True, blank=True,
                               on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
