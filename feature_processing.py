# Mapping
laptop_compartment_map = {"Yes": [1], "No": [-1], "Unknown": [0]}
waterproof_map = {"Yes": [1], "No": [-1], "Unknown": [0]}
size_map = {"Small": [1], "Medium": [2], "Large": [3], "Unknown": [-1]}

brand_list = ["Adidas", "Jansport", "Nike", "Puma", "Under Armour", "Unknown"]
material_list = ["Canvas", "Leather", "Nylon", "Polyester", "Unknown"]
style_list = ["Backpack", "Messenger", "Tote", "Unknown"]
color_list = ["Black", "Blue", "Gray", "Green", "Pink", "Red", "Unknown"]


def make_map_vector(categories: list):
    return {
        category: [1 if i == index else 0 for i in range(len(categories))]
        for index, category in enumerate(categories)
    }


brand_map = make_map_vector(brand_list)
material_map = make_map_vector(material_list)
style_map = make_map_vector(style_list)
color_map = make_map_vector(color_list)

# Feature order
#   "Size",
#   "Compartments",
#   "Laptop Compartment",
#   "Waterproof",
#   "Weight Capacity (kg)",
#   "Brand",
#   "Material",
#   "Style",
#   "Color",


def make_feature_vector(
    brand,
    material,
    size,
    compartments,
    laptop_compartment,
    waterproof,
    style,
    color,
    weight_capacity,
):
    return (
        size_map[size]
        + [compartments]
        + laptop_compartment_map[laptop_compartment]
        + waterproof_map[waterproof]
        + [weight_capacity]
        + brand_map[brand]
        + material_map[material]
        + style_map[style]
        + color_map[color]
    )


if __name__ == "__main__":

    vector = make_feature_vector(
        brand="Unknown",
        material="Canvas",
        size="Medium",
        compartments=8,
        laptop_compartment="Yes",
        waterproof="No",
        style="Unknown",
        color="Pink",
        weight_capacity=11,
    )

    print(vector)
