from django.db import migrations

def create_initial_products(apps, schema_editor):
    # We can't import the models directly as they may be a newer
    # version than this migration expects. We use the historical version.
    Brand = apps.get_model('main', 'Brand')
    Product = apps.get_model('main', 'Product')

    # Create Brands first
    nike = Brand.objects.create(name='Nike')
    adidas = Brand.objects.create(name='Adidas')
    puma = Brand.objects.create(name='Puma')

    # Create Products
    # --- Featured Products ---
    Product.objects.create(
        name="Manchester United 24/25 Home Kit",
        price=1200000,
        description="The official home jersey for Manchester United for the 2024/2025 season. Made with AEROREADY technology.",
        thumbnail="https://placehold.co/600x600/DA291C/FFFFFF?text=MUFC+Jersey",
        category="Jerseys",
        is_featured=True,
        stock=50,
        rating=4.8,
        brand=adidas
    )

    Product.objects.create(
        name="Nike Phantom Luna II Elite",
        price=3500000,
        description="Engineered for precision and control. The ultimate boot for playmakers.",
        thumbnail="https://placehold.co/600x600/000000/FFFFFF?text=Nike+Boots",
        category="Boots",
        is_featured=True,
        stock=25,
        rating=4.9,
        brand=nike
    )

    # --- Other Products ---
    Product.objects.create(
        name="Real Madrid 24/25 Away Kit",
        price=1150000,
        description="The official away jersey for Real Madrid. Clean, crisp, and classic design.",
        thumbnail="https://placehold.co/600x600/FEBE10/00529F?text=Real+Madrid",
        category="Jerseys",
        is_featured=False,
        stock=40,
        rating=4.7,
        brand=adidas
    )
    
    Product.objects.create(
        name="Puma Orbita 1 Serie A Ball",
        price=950000,
        description="The official match ball of the Italian Serie A. High-frequency molded for excellent shape retention.",
        thumbnail="https://placehold.co/600x600/FFFFFF/000000?text=Puma+Ball",
        category="Equipment",
        is_featured=False,
        stock=100,
        rating=4.6,
        brand=puma
    )


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),  # Make sure this matches your previous migration file
    ]

    operations = [
        migrations.RunPython(create_initial_products),
    ]